"""depressiondetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('authentication.urls')),
    path('signup', include('authentication.urls')),
    path('signin', include('authentication.urls')),
    path('passwordreset', include('authentication.urls')),
    path('about', include('authentication.urls')),
    path('myaccount', include('authentication.urls')),
    path('edit',include('authentication.urls')),
    path('data', include('authentication.urls')),
    path('prediction/', include('imageprediction.urls')),
    path('prediction/', include('textprediction.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)