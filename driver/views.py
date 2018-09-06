# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from form import DriverForm
from models import Driver,Persons
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def driver (request):
	template =loader.get_template('driver/driver.html')
	if  request.method== 'POST':
		form = DriverForm(request.POST)
		# driver = Driver.objects.get(pk=form.data.get('driver'))
		Driver.objects.create(license_no=form.data.get('license_no'),fname=form.data.get('fname'), lname=form.data.get('lname'),id_number= form.data.get('id_number'),tel_number=form.data.get('tel_number'),email=form.data.get('email'), gender=form.data.get('gender'))
		return HttpResponseRedirect ('/driver/driver/')

	else:
		form = DriverForm()
		drivers = Driver.objects.all()
		contetx = {'drivers': drivers}
		return HttpResponse (template.render(contetx, request))