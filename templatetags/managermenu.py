#from django.template import Library
#from django.utils.encoding import iri_to_uri
#
#register = Library()
#
#def manager_media_prefix():
#    try:
#        from django.conf import settings
#    except ImportError:
#        return ''
#    return iri_to_uri(settings.MANAGER_MEDIA_PREFIX)
#manager_media_prefix = register.simple_tag(manager_media_prefix)
