from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('catalog.urls', 'api'), namespace='api')),
    path('', include('catalog.urls')),
    path('healthz/', lambda r: HttpResponse('ok')),
]
if settings.DEBUG or getattr(settings, 'SERVE_MEDIA', False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
