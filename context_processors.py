from django.conf import settings

def static_media(request):
    return {'STATIC_MEDIA_URL': settings.STATIC_MEDIA_URL}