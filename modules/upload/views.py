import uuid
from django.http import HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_img(request):
    if request.user.is_authenticated() and request.user.is_staff and request.FILES['file'] and request.FILES['file'].content_type in ['image/png', 'image/jpeg', 'image/gif']:
        data = request.FILES['file']
        name = 'upload/'+str(uuid.uuid4()).replace('-', '') + '.jpg';
        fd = open(settings.MEDIA_ROOT + name, 'wb')
        fd.write(data.file.getvalue())
        fd.close()
        return HttpResponse(settings.MEDIA_URL + name)
    return HttpResponseForbidden()
