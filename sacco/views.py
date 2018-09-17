from __future__ import unicode_literals
from django.shortcuts import render, redirect
from sacco.forms import SaccoForm, OfficialForm, RouteForm, DriverForm, VehicleForm
from sacco.models import Sacco, Official, Route, Driver, Vehicle
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from sacco.models import OFFICIAL_POSITION
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

def sacco(request):
    template = loader.get_template('sacco/sacco.html')
    if request.method == 'POST':
        form = SaccoForm(request.POST)
        Sacco.objects.create(name=form.data.get('name'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), sacco_no=form.data.get(
            'sacco_no'), postal_address=form.data.get('postal_address'), postal_code=form.data.get('postal_code'), town=form.data.get('town'))
        return HttpResponseRedirect('/sacco/route/')

    else:
        form = SaccoForm()
        saccos = Sacco.objects.all()
        context = {'saccos': saccos}
        return HttpResponse(template.render(context, request))


def sacco_list(request):
    template = loader.get_template('sacco/sacco_list.html')
    hold = Driver.objects.all()
    context = {'hold': hold}
    return HttpResponse(template.render(context, request))


def official(request):
    template = loader.get_template('sacco/official.html')
    if request.method == 'POST':
        form = OfficialForm(request.POST)
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))

        Official.objects.create(title=form.data.get('title'), sacco=sacco, fname=form.data.get('fname'), lname=form.data.get(
            'lname'), id_number=form.data.get('id_number'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), gender=form.data.get('gender'))
        return HttpResponseRedirect('/sacco/official/')

    else:
        form = OfficialForm()
        saccos = Sacco.objects.all()
        context = {'saccos': saccos}
        return HttpResponse(template.render(context, request))


def route(request):
    template = loader.get_template('sacco/route.html')
    if request.method == 'POST':
        form = RouteForm(request.POST)
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))
        Route.objects.create(name=form.data.get('name'), county=form.data.get(
            'county'), sacco=sacco, route_number=form.data.get('route_number '))
        return HttpResponseRedirect('/sacco/vehicle/')

    else:

        form = RouteForm()
        saccos = Sacco.objects.all()
        context = {'saccos': saccos}
        return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('sacco/home.html')

    saccos = Sacco.objects.all().order_by('-id')
    vehicles = Vehicle.objects.all()

    for sacco in saccos:
        sacco.vehicles = [v for v in vehicles if v.sacco == sacco]

    # sacco = Sacco.objects.get(pk=form.data.get('sacco'))
    # vehicle=Vehicle.objects.get(pk=form.data.get('vehicle'))

    routes=Route.objects.all()
    context={ 'saccos': saccos, 'r': routes}
    return HttpResponse(template.render(context, request))


def llogin(request):
    template = loader.get_template('sacco/login.html')
    import pdb
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        import pdb
        pdb.set_trace()
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/sacco/route/')
        else:
            return HttpResponseRedirect('/sacco/official/')
    else:
        return HttpResponse(template.render({}, request))


def sacco_list(request):
    template = loader.get_template('sacco/sacco_list.html')
    hold = Sacco.objects.all()
    context = {'hold': hold}
    return HttpResponse(template.render(context, request))


def delete_sacco(request, sacco_id):
    template = loader.get_template('sacco/success.html')
    sacco = Sacco.objects.get(pk=sacco_id)
    sacco.delete()
    context = {
        'message': 'Sacco has been Deleted successfully.',
    }
    return HttpResponse(template.render(context, request))


def driver(request):
    template = loader.get_template('sacco/driver.html')
    if request.method == 'POST':
        form = DriverForm(request.POST)
        vehicle = Vehicle.objects.get(pk=form.data.get('vehicle'))
        Driver.objects.create(license_no=form.data.get('license_no'), fname=form.data.get('fname'), lname=form.data.get('lname'), id_number=form.data.get(
            'id_number'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), gender=form.data.get('gender'), vehicle=vehicle)
        return HttpResponseRedirect('/sacco/driver/')

    else:
        form = DriverForm()
        vehicles = Vehicle.objects.all()
        context = {'vehicles': vehicles}
        return HttpResponse(template.render(context, request))


def driver_list(request):
    template = loader.get_template('sacco/driver_list.html')
    hold = Driver.objects.all()
    context = {'hold': hold}
    return HttpResponse(template.render(context, request))


def delete_driver(request, driver_id):
    template = loader.get_template('sacco/success.html')
    driver = Driver.objects.get(pk=driver_id)
    driver.delete()
    context = {
        'message': 'Driver has been Deleted successfully.',
    }
    return HttpResponse(template.render(context, request))


def success(request):
    template = loader.get_template('sacco/success.html')
    return HttpResponse(template.render({}, request))


def approve(request, driver_id):
    driver = Driver.objects.get(pk=driver_id)
    driver.status = True
    driver.save()
    return HttpResponseRedirect('/sacco/driver_list/')


def vehicle(request):
    template = loader.get_template('sacco/vehicle.html')
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        # driver = Driver.objects.get(pk=form.data.get('driver'))
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))

        try:
            Vehicle.objects.create(car_reg=form.data.get(
                'car_reg'), car_type=form.data.get('car_type'), sacco=sacco)
            return HttpResponseRedirect('/sacco/driver/')

        except IntegrityError as err:
            context = {'message': "{} {} {}".format("SORRY!, The Vehicle with Registration Number ", form.data.get(
                'car_reg'), " already exists, please try again!!")}
            temp = loader.get_template('sacco/error.html')
            return HttpResponse(temp.render(context, request))
    else:
        form = VehicleForm()
        vehicles = Vehicle.objects.all()
        driver = Driver.objects.all()
        sacco = Sacco.objects.all()
        context = {'vehicles': vehicles, 'drivers': driver, 'saccos': sacco}
        return HttpResponse(template.render(context, request))


def rating(request, pk):

    try:
        vehicle = Vehicle.objects.get(pk=pk)
        temp = loader.get_template('sacco/rating.html')
        if request.method == "GET":
            driver = Driver.objects.get(vehicle=vehicle)
            sacco = Sacco.objects.get(pk=vehicle.sacco_id)
            context = {
                'vehicle': vehicle,
                'sacco': sacco,
                'driver': driver
            }
            return HttpResponse(temp.render(context, request))

        elif request.method == 'POST':
        	vehicle= Vehicle.objects.all()
        	context ={'vehicle':vehicle}
        	return HttpResponse(temp.render(context, request))
    except Vehicle.DoesNotExist:
        # // return error page or page not found
        return HttpResponse("Vehicle does not Exist")


def rate_vehicle(request, vehicle, score):
    try:
        vehicle = int(vehicle)
        score = int(score)
        v = Vehicle.objects.get(pk=vehicle)
        no_raters = v.no_raters
        rating = v.rating

        total_ratings = float(no_raters) * rating
        new_no_raters = no_raters + 1
        new_total_ratings = total_ratings + score
        new_rating = new_total_ratings / float(new_no_raters)
        v.rating = new_rating
        v.no_raters = new_no_raters
        v.save()
        return redirect('../rating/{}'.format(vehicle))
    except Vehicle.DoesNotExist:
        return redirect('../home')


def rate_driver(request, driver, score):
    try:
        vehicle = int(driver)
        score = int(score)
        v = Driver.objects.get(pk=driver)
        no_raters = v.no_raters
        rating = v.rating

        total_ratings = float(no_raters) * rating
        new_no_raters = no_raters + 1
        new_total_ratings = total_ratings + score
        new_rating = new_total_ratings / float(new_no_raters)
        v.rating = new_rating
        v.no_raters = new_no_raters
        v.save()
        return redirect('../rating/{}'.format(driver))
    except driver.DoesNotExist:
        return redirect('../home')