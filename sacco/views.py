# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SaccoForm, OfficialForm, RouteForm
from models import Sacco, Official, Route
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from models import OFFICIAL_POSITION


def sacco(request):
	template = loader.get_template('sacco/sacco.html')
	if request.method == 'POST':
		form = SaccoForm(request.POST)
		Sacco.objects.create(name=form.data.get('name'),contacts=form.data.get('contacts'))
		return HttpResponseRedirect('/sacco/sacco/')

	else:
		form = SaccoForm()
		saccos = Sacco.objects.all()
		context = {'saccos': saccos}
		return HttpResponse(template.render(context, request))

def official(request):
	template=loader.get_template('sacco/official.html')
	if request.method == 'POST':
		form = OfficialForm(request.POST)
		sacco = Sacco.objects.get(pk=form.data.get('sacco'))
		
		Official.objects.create(title=form.data.get('title'), sacco=sacco, fname=form.data.get('fname'),lname=form.data.get('lname'),id_number=form.data.get('id_number'),tel_number=form.data.get('tel_number'),email=form.data.get('email'),gender=form.data.get('gender'))
		return HttpResponseRedirect('/sacco/official/')

	else:
		form =OfficialForm()
		saccos = Sacco.objects.all()
		context = {'saccos': saccos}
		return HttpResponse (template.render(context,request))

def route (request):
	template=loader.get_template('sacco/route.html')
	if request.method== 'POST':
		form = RouteForm(request.POST)
		sacco = Sacco.objects.get(pk=form.data.get('sacco'))
		Route.objects.create(name=form.data.get('name'),county=form.data.get('county'), sacco=sacco)
		return HttpResponseRedirect('/sacco/route/')

	else:
		
		form = RouteForm()
		saccos= Sacco.objects.all()
		context={'saccos': saccos}
		return HttpResponse (template.render(context,request))

