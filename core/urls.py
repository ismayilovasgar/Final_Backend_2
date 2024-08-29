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
from django.urls import path,include
from home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),                                        # http://127.0.0.1:8000/admin
    path("", home__page, name="home"),                                      # http://127.0.0.1:8000/
    path("pricing/", pricing__page, name="pricing"),                        # http://127.0.0.1:8000/pricing
    path("features/", features__page,name="features"),                      # http://127.0.0.1:8000/features
    path("download/", download__page,name="download"),                      # http://127.0.0.1:8000/download
    path("lifestyle/", lifestyle__page,name="lifestyle"),                   # http://127.0.0.1:8000/lifestyle
    path("singleblog/<int:id>/", singleblog__page,name="singleblog"),                # http://127.0.0.1:8000/singleblog
    path("class_01/", class01__page,name="class01"),                        # http://127.0.0.1:8000/class_01
    path("class_01_detail/<int:id>/", class01detail__page,name="class01detail"),     # http://127.0.0.1:8000/class_01_detail
    path("class_02/", class02__page,name="class02"),                        # http://127.0.0.1:8000/class_02
    path("class_02_detail/", class02detail__page,name="class02detail"),     # http://127.0.0.1:8000/class_02_detail
    path("trainer/", include("filter.urls")),                                 # http://127.0.0.1:8000/trainer/...
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)