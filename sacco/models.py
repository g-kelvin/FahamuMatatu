from __future__ import unicode_literals
from django.db import models

OFFICIAL_POSITION=(
	('chairman' ,'chairman'),
	('vice chairman', 'v_chairman'),
	('Treasurer', 'Treasurer'),
	('Secretary', 'Secretary'),
	('Office Manager', 'Office_Manager'),
	('Office Clerk', 'Office_Clerk'),
	('Route Inspector','Route_Inspector'),

	)

YOUR_GENDER=(
	('MALE','MALE'),
	('FEMALE','FEMALE'),
	)

CAR_MODEL_TYPE=(
	('BUS','BUS'),
	('NISSAN', 'NISSAN')

	)


class Sacco(models.Model):
	name = models.CharField(max_length=200, null=False , unique = True)
	tel_number =models.CharField(max_length=400, null=True )
	email = models.CharField(max_length=400, null=False)
	sacco_no = models.CharField(max_length=200, null= False , unique = True)
	postal_address=models.CharField(max_length=400, null=False)
	postal_code=models.CharField(max_length=400, null=False)
	town=models.CharField(max_length=400, null=False)

	def __str__(self):
		return self.name.title()


class Persons(models.Model):
	fname= models.CharField(max_length=200, null=True)
	lname=models.CharField(max_length=200, null=True)
	id_number =models.CharField(max_length=200, null=True ,unique=True)
	tel_number =models.CharField(max_length=200, null=True)
	email =models.CharField(max_length=200, null=True)
	gender =models.CharField(max_length=200, null=True, choices=YOUR_GENDER)

	class Meta:
		abstract = True

	def get_full_name(self):
		return "{} {}".format(self.fname.title(), self.lname.title())


class Vehicle(models.Model):
	car_reg= models.CharField(max_length=200, unique=True)
	car_type= models.CharField(max_length=200 ,choices=CAR_MODEL_TYPE)
	rating= models.FloatField(default=0.0)
	no_raters = models.IntegerField(default=0)
	sacco=models.ForeignKey('Sacco', related_name="vehicle_sacco", on_delete=models.CASCADE)

	def __str__(self):
		return self.car_reg.upper()

		




class Driver(Persons):
	license_no= models.CharField(max_length=200, null=False)
	status= models.CharField(max_length=200, null= True, default=False)
	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	rating= models.FloatField(default=0.0)
	no_raters = models.IntegerField(default=0)
 
	def __str__(self):
		return u'%s %s' % (self.fname.title(), self.lname.title())

	def get_sacco(self):
		return self.vehicle.sacco


class Official(Persons):
	title =models.CharField(max_length=200, null=False , choices=OFFICIAL_POSITION)
	sacco=models.ForeignKey('Sacco', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Route (models.Model):
	name= models.CharField(max_length=200, null=False)
	county = models.CharField(max_length=200, null=False)
	sacco=models.ForeignKey('Sacco', on_delete=models.CASCADE)
	route_number = models.CharField(max_length=200, null= False)

	def __str__(self):
		return self.name

