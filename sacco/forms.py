from django import forms
from sacco.models import Sacco, Official, Route, Vehicle, Driver


class SaccoForm(forms.ModelForm):
	class Meta:
		model = Sacco
		fields="__all__"


class OfficialForm(forms.ModelForm):
	class Meta:
		model =Official
		fields ="__all__"


class RouteForm (forms.ModelForm):
	class Meta:
		model =Route 
		fields="__all__"


class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields= '__all__'

class VehicleForm(forms.ModelForm):
	class Meta:

		model = Vehicle
		fields ="__all__"