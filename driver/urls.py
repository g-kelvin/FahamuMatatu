from django.conf.urls import url, include
# from django.contrib import admin
from views import driver 

urlpatterns = [
    url(r'^driver/$', driver, name='driver'),

]