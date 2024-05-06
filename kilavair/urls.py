"""
URL configuration for kilavair project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from kilavair import settings
from kilavair.views import home_page, header, footer,about, engineering


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('', include('contact.urls', namespace='contact')),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('about-us/', about, name='about-us'),
    path('engineering/', engineering, name='engineering'),
]

if settings.DEBUG:
    # add root statice files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)