"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# MEDIA FILES CONFIG
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("pages.urls")),  # http://127.0.0.1:8000/...
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000/admin/
    path("courses/", include("courses.urls")),  # http://127.0.0.1:8000/courses/...
    path("trainers/", include("trainers.urls")),  # http://127.0.0.1:8000/trainers/...
    path("accounts/", include("accounts.urls")),  # http://127.0.0.1:8000/accounts/...
]
# handler404 = "pages.views.custom_404"  
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
