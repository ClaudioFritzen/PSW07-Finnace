from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# tentando pergar o view
from perfil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    path("/", include("perfil.urls")),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)