# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from driver.models import Persons
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


class  Sacco(models.Model):
	name = models.CharField(max_length=200, null=False)
	contacts =models.CharField(max_length=400, null=False)

	def __str__(self):
		return self.name


class Official(Persons):
	title =models.CharField(max_length=200, null=False , choices=OFFICIAL_POSITION)
	sacco=models.ForeignKey(Sacco, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Route (models.Model):
	name= models.CharField(max_length=200, null=False)
	county = models.CharField(max_length=200, null=False)
	sacco=models.ForeignKey(Sacco, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

