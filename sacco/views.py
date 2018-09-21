from __future__ import unicode_literals
from django.shortcuts import render, redirect
from sacco.forms import SaccoForm, OfficialForm, RouteForm, DriverForm, VehicleForm
from sacco.models import Sacco, Official, Route, Driver, Vehicle
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from sacco.models import OFFICIAL_POSITION
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .gen_pdf import render_to_pdf
from django.template.loader import get_template
from xhtml2pdf import pisa

@permission_required('sacco.add_sacco', raise_exception=True)
def sacco(request):
    template = loader.get_template('sacco/sacco.html')
    if request.method == 'POST':
        form = SaccoForm(request.POST)
        try:
            Sacco.objects.create(name=form.data.get('name'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), sacco_no=form.data.get(
            'sacco_no'), postal_address=form.data.get('postal_address'), postal_code=form.data.get('postal_code'), town=form.data.get('town'))
            return HttpResponseRedirect('/sacco/official/')
        except IntegrityError as err:
            context = {'message': "{} {} {}".format("SORRY!,  ", form.data.get(
                'name'), " already exists, please enter another valid sacco name")}
            temp = loader.get_template('sacco/error.html')
            return HttpResponse(temp.render(context, request))


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


@permission_required('sacco.add_official', raise_exception=True)
def official(request):
    template = loader.get_template('sacco/official.html')
    if request.method == 'POST':
        form = OfficialForm(request.POST)
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))

        Official.objects.create(title=form.data.get('title'), sacco=sacco, fname=form.data.get('fname'), lname=form.data.get(
            'lname'), id_number=form.data.get('id_number'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), gender=form.data.get('gender'))
        return HttpResponseRedirect('/sacco/route/')

    else:
        form = OfficialForm()
        saccos = Sacco.objects.all()
        context = {'saccos': saccos}
        return HttpResponse(template.render(context, request))

@permission_required('sacco.add_route', raise_exception=True)
def route(request):
    template = loader.get_template('sacco/route.html')
    if request.method == 'POST':
        form = RouteForm(request.POST)
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))
        Route.objects.create(name=form.data.get('name'), county=form.data.get(
            'county'), sacco=sacco, route_number=form.data.get('route_number '))
        context = {
            'message': 'You have successfully Registered Sacco, Official and Route',
            'link': '/sacco/vehicle'
        }
        temp = loader.get_template('sacco/success.html')
        return HttpResponse(temp.render(context, request))

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


    routes=Route.objects.all()
    context={ 'saccos': saccos, 'r': routes}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/sacco/login/')
def index(request):
    template = loader.get_template('sacco/index.html')
    return HttpResponse(template.render({}, request))


def llogin(request):
    template = loader.get_template('sacco/login.html')
    temp = loader.get_template('sacco/success.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/sacco/index/')
        else:
            context = {
                'message': 'SORRY!!! INVALID CREDENTIALS, TRY AGAIN.',
            }
        return HttpResponse(temp.render(context, request))
    else:
        return HttpResponse(template.render({}, request))



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/sacco/login/')
    


def sacco_list(request):
    template = loader.get_template('sacco/sacco_list.html')
    hold = Sacco.objects.all()
    context = {'hold': hold}
    return HttpResponse(template.render(context, request))

@permission_required('sacco.delete_sacco', raise_exception=True)
def delete_sacco(request, sacco_id):
    template = loader.get_template('sacco/success.html')
    sacco = Sacco.objects.get(pk=sacco_id)
    sacco.delete()
    context = {
        'message': 'Sacco has been Deleted successfully.',
    }
    return HttpResponse(template.render(context, request))

@permission_required('sacco.add_driver', raise_exception=True)
def driver(request):
    template = loader.get_template('sacco/driver.html')
    if request.method == 'POST':
        form = DriverForm(request.POST)
        vehicle = Vehicle.objects.get(pk=form.data.get('vehicle'))
        Driver.objects.create(license_no=form.data.get('license_no'), fname=form.data.get('fname'), lname=form.data.get('lname'), id_number=form.data.get(
            'id_number'), tel_number=form.data.get('tel_number'), email=form.data.get('email'), gender=form.data.get('gender'), vehicle=vehicle)
        context = {'message': "{} {} {} {} {} ".format("CONGRATULATION!!  ", form.data.get(
                'fname'), " of license number " ,form.data.get('license_no'), "has been successfully Registered" )}
        temp = loader.get_template('sacco/success.html')
        return HttpResponse(temp.render(context, request))
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

@permission_required('sacco.delete_driver', raise_exception=True)
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

@permission_required('sacco.change_driver', raise_exception=True)
def approve(request, driver_id):
    driver = Driver.objects.get(pk=driver_id)
    driver.status = True
    driver.save()
    return HttpResponseRedirect('/sacco/driver_list/')

@permission_required('sacco.add_vehicle', raise_exception=True)
def vehicle(request):
    template = loader.get_template('sacco/vehicle.html')
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        # driver = Driver.objects.get(pk=form.data.get('driver'))
        sacco = Sacco.objects.get(pk=form.data.get('sacco'))

        try:
            car_reg = form.data.get('car_reg')
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
            vehicle.rating = round(vehicle.rating, 1)
            driver.rating = round(driver.rating, 1)
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


def rate_driver(request, driver, score, vehicle_id):
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
        
        return redirect('../../../rating/{}'.format(vehicle_id))
    except driver.DoesNotExist:
        return redirect('../home')

def sacco_profile(request, id):
    temp = loader.get_template('sacco/sacco_profile.html')

    sacco = Sacco.objects.get(pk=id)
    vehicles = Vehicle.objects.filter(sacco_id = id)
    for vehicle in vehicles:
        vehicle.driver = Driver.objects.get(vehicle = vehicle)
    total_ratings = 0.0
    drivers = [Driver.objects.get(vehicle=vehicle) for vehicle in vehicles]
    total_ratings = 0.0
    
    for driver in drivers:
        total_ratings += driver.rating
    try:      
        sacco_rating = total_ratings / len(drivers)
    except Exception as e:
        sacco_rating = 0.0

    context = {
            'sacco': sacco,
            'sacco_rating': round(sacco_rating, 1),
            'vehicles': vehicles
        }
    return HttpResponse(temp.render(context, request))



def create_qr(request, number_plate):
    """ create a qr code using the number plate"""
    temp = loader.get_template('sacco/create_qr.html')

    vehicle = Vehicle.objects.get(car_reg=number_plate)
    rating_url  = 'http://localhost:8000/sacco/rating/{}/'.format(vehicle.id)
    context = {
        'url': rating_url,
        'vehicle': vehicle
    }
    html=temp.render(context)
    # pdf= render_to_pdf('sacco/create_qr.html',context)
    import pdfkit
    create_qr_url = 'http://localhost:8000/sacco/create_qr/{}/'.format(vehicle.car_reg.replace(" ", "%20"))
    pdf = pdfkit.from_url(create_qr_url, False)
    return HttpResponse(pdf,content_type='application/pdf')
    # return HttpResponse(temp.render(context, request))

def fake_create_qr(request, number_plate):
    """ create a qr code using the number plate"""
    temp = loader.get_template('sacco/create_qr.html')

    vehicle = Vehicle.objects.get(car_reg=number_plate)
    rating_url  = 'http://localhost:8000/sacco/rating/{}/'.format(vehicle.id)
    context = {
        'url': rating_url,
        'vehicle': vehicle
    }
    # html=temp.render(context)
    # pdf= render_to_pdf('sacco/create_qr.html',context)
    # return HttpResponse(pdf,content_type='application/pdf')
    return HttpResponse(temp.render(context, request))


def download_driverreport(request, driver_id):
    """ return the driver info"""
    temp = loader.get_template('sacco/driver_report.html')
    driver = Driver.objects.get(pk=driver_id)

    context = {
        'driver': driver
    }
    # html=temp.render(context)
    # pdf= render_to_pdf('sacco/driver_report.html',context)
    # return HttpResponse(pdf,content_type='application/pdf')

    return HttpResponse(temp.render(context, request))

def register (request):
    if request.method =='POST':
        user=User.objects.create_user(
            request.POST ['username'],
            request.POST['email'],
            request.POST['password']
        )
        user.username = request.POST['username']
        user.save()
        return HttpResponseRedirect('/sacco/login/')

    else:
        temp = loader.get_template('sacco/register.html')
        return HttpResponse(temp.render({}, request))

        
