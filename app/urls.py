"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#Import package dokumentasi API
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


#Setting dokumentasi API ( judul, deskripsi dll)
schema_view = get_schema_view(
    openapi.Info(
        title= "Lampost News App API",
        default_version='v1',
        description="An API for Lampost News App",
        terms_of_service="/terms/",
        contact=openapi.Contact(email="contact@tokomob.net"),
        license=openapi.License(name="BSD License"),
    ),
    public= True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
   # dokumentasi API dengan Swagger
    path('', schema_view.with_ui('swagger',
                    cache_timeout=0), name='schema-swagger-ui'),
    # dokumentasi API dengan Redoc
    path('redoc/', schema_view.with_ui('redoc',
                        cache_timeout=0), name='schema-redoc'),
]