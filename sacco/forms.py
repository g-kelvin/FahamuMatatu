from django import forms
from models import Sacco, Official, Route


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