from optparse import make_option
import sys
import sitemanager

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.management.color import no_style
from django.core.management.sql import custom_sql_for_model, emit_post_sync_signal
from django.db import connections, router, transaction, models, DEFAULT_DB_ALIAS
from django.utils.datastructures import SortedDict
from django.utils.importlib import import_module
from sitemanager.sites import site

def create_models():

    verbosity = 1
    interactive = None
    show_traceback = True

    style = no_style()

    # Import the 'management' module within each installed app, to register
    # dispatcher events.
    for app_name in settings.SITEMANAGER_MODULES:
        try:
            print app_name
            import_module('.management', app_name)
        except ImportError, exc:
            # This is slightly hackish. We want to ignore ImportErrors
            # if the "management" module itself is missing -- but we don't
            # want to ignore the exception if the management module exists
            # but raises an ImportError for some reason. The only way we
            # can do this is to check the text of the exception. Note that
            # we're a bit broad in how we check the text, because different
            # Python implementations may not use the same text.
            # CPython uses the text "No module named management"
            # PyPy uses "No module named myproject.myapp.management"
            msg = exc.args[0]
            if not msg.startswith('No module named') or 'management' not in msg:
                raise

    db = DEFAULT_DB_ALIAS
    connection = connections[db]
    cursor = connection.cursor()

    # Get a list of already installed *models* so that references work right.
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    created_models = set()
    pending_references = {}
    modules_models = []

    for module in settings.SITEMANAGER_MODULES:
        appmodel = models.loading.load_app(module)
        print appmodel
        if appmodel != None:
            modules_models.append(appmodel)

    # Build the manifest of apps and models that are to be synchronized
    all_models = [
        (app.__name__.split('.')[-2],
            [m for m in models.get_models(app, include_auto_created=True)
            if router.allow_syncdb(db, m)])
        for app in modules_models
    ]

    def model_installed(model):
        opts = model._meta
        converter = connection.introspection.table_name_converter
        return not ((converter(opts.db_table) in tables) or
            (opts.auto_created and converter(opts.auto_created._meta.db_table) in tables))

    manifest = SortedDict(
        (app_name, filter(model_installed, model_list))
        for app_name, model_list in all_models
    )

    count = 0
    # Create the tables for each model
    for app_name, model_list in manifest.items():
        for model in model_list:
            # Create the model's database table, if it doesn't already exist.
            if verbosity >= 2:
                print "Processing %s.%s model" % (app_name, model._meta.object_name)
            sql, references = connection.creation.sql_create_model(model, style, seen_models)
            seen_models.add(model)
            created_models.add(model)
            for refto, refs in references.items():
                pending_references.setdefault(refto, []).extend(refs)
                if refto in seen_models:
                    sql.extend(connection.creation.sql_for_pending_references(refto, style, pending_references))
            sql.extend(connection.creation.sql_for_pending_references(model, style, pending_references))
            if verbosity >= 1 and sql:
                if count == 0:
                    print "Create tables for models in sitemanager.modules:"
                print "Creating table %s" % model._meta.db_table
                count += 1
            for statement in sql:
                cursor.execute(statement)
            tables.append(connection.introspection.table_name_converter(model._meta.db_table))


    transaction.commit_unless_managed(using=db)

    if len(created_models) > 0:

        # Send the post_syncdb signal, so individual apps can do whatever they need
        # to do at this point.
        emit_post_sync_signal(created_models, verbosity, interactive, db)

        # The connection may have been closed by a syncdb handler.
        cursor = connection.cursor()

        # Install SQL indicies for all newly created models
        for app_name, model_list in manifest.items():
            for model in model_list:
                if model in created_models:
                    index_sql = connection.creation.sql_indexes_for_model(model, style)
                    if index_sql:
                        if verbosity >= 1:
                            print "Installing index for %s.%s model" % (app_name, model._meta.object_name)
                        try:
                            for sql in index_sql:
                                cursor.execute(sql)
                        except Exception, e:
                            sys.stderr.write("Failed to install index for %s.%s model: %s\n" % \
                                                (app_name, model._meta.object_name, e))
                            transaction.rollback_unless_managed(using=db)
                        else:
                            transaction.commit_unless_managed(using=db)

    #    from django.core.management import call_command
    #    call_command('loaddata', 'initial_data', verbosity=verbosity, database=db)

def add_data():
    for app_name in settings.SITEMANAGER_MODULES:
        try:
            import_module('.data', app_name)
        except ImportError, msg:
            print app_name, "|",msg
            pass

create_models()
add_data()
