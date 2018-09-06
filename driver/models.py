# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

YOUR_GENDER=(

	('MALE','MALE'),
	('FEMALE','FEMALE'),
	)

class Persons(models.Model):
	fname= models.CharField(max_length=200, null=True)
	lname=models.CharField(max_length=200, null=True)
	id_number =models.IntegerField(null=True)
	tel_number =models.IntegerField(null=True)
	email =models.CharField(max_length=200, null=True)
	gender =models.CharField(max_length=200, null=True, choices=YOUR_GENDER)

	class Meta:
		abstract = True


class Driver(Persons):
	license_no= models.CharField(max_length=200, null=False)



