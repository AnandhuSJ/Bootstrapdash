from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static, serve
from baseapp import views


urlpatterns = [
                re_path('admin/', admin.site.urls),
                re_path(r'^$', views.BootstrapDash, name='BootstrapDash'),
]
