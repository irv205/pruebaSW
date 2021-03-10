from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.urls import path, include
from apps.user import views

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #module-router
    path('v1/', include('apps.user.urls')),
    path('v1/', include('apps.courses.urls')),
    path('v1/', include('apps.assignCourse.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
