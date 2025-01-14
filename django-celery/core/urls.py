from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view)
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
