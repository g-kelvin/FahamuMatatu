from django import forms
from models import Vehicle

class VihecleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields ="__all__"