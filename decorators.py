from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import mail_admins
from django.conf import settings
from django.utils.translation import ugettext as _
import sys
import sitemanager.menus

def menu_decorator(menu_id):
    def _decorator(func):
        def change(*args, **kwargs):
            sitemanager.menus.current_menu = menu_id
            return func(*args, **kwargs)
        return change
    return _decorator

def json_view(func):
    def wrap(request, *a, **kw):
        response = None
        try:
            response = func(request, *a, **kw)
            assert isinstance(response, dict)
            if 'result' not in response:
                response['result'] = 'ok'
        except KeyboardInterrupt:
            # Allow keyboard interrupts through for debugging.
            raise
        except Exception, e:
            # Mail the admins with the error
            exc_info = sys.exc_info()
            subject = 'JSON view error: %s' % request.path
            try:
                request_repr = repr(request)
            except:
                request_repr = 'Request repr() unavailable'
            import traceback
            message = 'Traceback:\n%s\n\nRequest:\n%s' % (
                '\n'.join(traceback.format_exception(*exc_info)),
                request_repr,
                )
            mail_admins(subject, message, fail_silently=True)

            # Come what may, we're returning JSON.
            if hasattr(e, 'message'):
                msg = e.message
            else:
                msg = _('Internal error')+': '+str(e)
            if settings.DEBUG:
                response = {'result': 'error',
                            'text': msg}
            else:
                response = {'result': 'error'}

        json = simplejson.dumps(response, ensure_ascii=False)
        return HttpResponse(json, mimetype='application/json')
    return wrap
