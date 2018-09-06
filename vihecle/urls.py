from django.conf.urls import url, include
# from django.contrib import admin
from views import vihecle

urlpatterns = [
    url(r'^vihecle/$', vihecle, name='vihecle'),
]
