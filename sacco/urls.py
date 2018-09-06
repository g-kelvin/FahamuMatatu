from django.conf.urls import url, include
# from django.contrib import admin
from views import sacco, official, route

urlpatterns = [
    url(r'^sacco/$', sacco, name='sacco'),
    url(r'^official/$',official , name ='official'),
    url(r'^route/$',route, name ='route')

]
