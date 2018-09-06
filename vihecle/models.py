# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from driver.models import Driver
from sacco.models import Sacco
from django.db import models

CAR_MODEL_TYPE=(
	('BUS','BUS'),
	('NISSAN', 'NISSAN')

	)


class Vehicle(models.Model):
	car_reg= models.CharField(max_length=200, unique=True)
	car_type= models.CharField(max_length=200 ,choices=CAR_MODEL_TYPE)
	driver =models.ForeignKey(Driver, on_delete=models.CASCADE)
	sacco=models.ForeignKey(Sacco, on_delete=models.CASCADE)



