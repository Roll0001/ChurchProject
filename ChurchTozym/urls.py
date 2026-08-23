"""
URL configuration for ChurchTozym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.static import serve
from TozymChurch_APP import views
from django.conf import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/add/', views.add_schedule_event, name='add_schedule_event'),
    path('', include('auth_system.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]