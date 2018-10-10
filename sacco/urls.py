from django.conf.urls import url, include
from django.contrib import admin
from .models import Sacco
from .views import *

urlpatterns = [
    url(r'^sacco/$', sacco, name='sacco'),
    url(r'^official/$', official, name='official'),
    url(r'^route/$', route, name='route'),
    url(r'^home/$', home, name='home'),
    url(r'^index/$', index, name='index'),
    url(r'^login/$', llogin, name='login'),
    url(r'^logoutuser/$', logoutuser, name='logoutuser'),
    url(r'^register/$', register, name='register'),
    url(r'^sacco_list/$', sacco_list, name='sacco_list'),
    url(r'^delete_sacco/(?P<sacco_id>[0-9]+)/$',
        delete_sacco, name='delete_sacco'),

    url(r'^driver/$', driver, name='driver'),
    url(r'^success/$', success, name='success'),
    url(r'^driver_list/$', driver_list, name='driver_list'),
    url(r'^delete_driver/(?P<driver_id>[0-9]+)/$',
        delete_driver, name='delete_driver'),
    url(r'^approve/(?P<driver_id>[0-9]+)/$', approve, name='approve'),

    url(r'^vehicle/$', vehicle, name='vehicle'),
    url(r'^rating/(?P<pk>[0-9]+)/$', rating, name='rating'),
    url(r'^rate/(?P<vehicle>\d+)-(?P<score>\d+)', rate_vehicle, name="rate-vehicle"),
    url(r'^rate-driver/(?P<driver>\d+)-(?P<score>\d+)/(?P<vehicle_id>\d+)/', rate_driver, name="rate-driver"),
    url(r'^sacco_profile/(?P<id>\d+)/', sacco_profile, name="sacco-profile"),
    url(r'^create-qr/(?P<number_plate>[a-zA-Z0-9 ]+)/', create_qr, name="create-qr"),
    # url(r'^create_qr/(?P<number_plate>[a-zA-Z0-9 ]+)/', fake_create_qr, name="create-qr"),
    url(r'^download-driver/(?P<driver_id>[0-9]+)/', download_driverreport, name='download-driver'),
    # url(r'^download_driver/(?P<driver_id>[0-9]+)/', download_driverreport1, name='download_driver'),
    url(r'^sacco/profile/(?P<pk>[0-9]+)/$', sacco_profile, name="sacco-profile"),
    url(r'^vehicle_list/$', vehicle_list, name='vehicle_list'),
    url(r'^accident/$', accident, name='accident'),
    url(r'^aboutus/$', aboutus, name='aboutus'),



]
