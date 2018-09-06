from __future__ import unicode_literals

from django.shortcuts import render
from forms import VihecleForm
from models import Vehicle,Driver, Sacco
from django.template import loader
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect

def vihecle (request):
	template= loader.get_template('vihecle/vihecle.html')
	if request.method== 'POST':
		form = VihecleForm(request.POST)
		driver = Driver.objects.get(pk=form.data.get('driver'))
		sacco = Sacco.objects.get(pk=form.data.get('sacco'))

		try:
			Vehicle.objects.create(car_reg =form.data.get('car_reg'), car_type= form.data.get('car_type'), driver=driver, sacco=sacco)
			return HttpResponseRedirect('/vihecle/vihecle/')

		except IntegrityError as err:
			context = {'message': "{} {} {}".format("SORRY!, The Vehicle with Registration Number ", form.data.get('car_reg'), " already exists, please try again!!")}
			temp = loader.get_template('vihecle/error.html')
			return HttpResponse(temp.render(context, request))
	else:
		# import pdb
		# pdb.set_trace()
		form = VihecleForm()
		vihecles= Vehicle.objects.all()
		driver = Driver.objects.all()
		sacco= Sacco.objects.all()
		context = {'vihecles': vihecles, 'drivers': driver, 'saccos': sacco}
		return HttpResponse(template.render(context, request))