
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('App01.urls')),
    path('app2/', include('App02.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
