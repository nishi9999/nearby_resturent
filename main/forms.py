from .models import Resturent
from django import forms
from django.contrib.gis import forms as frm
from django.forms import ModelForm

class ResturentSearchForm(ModelForm):
	class Meta:
		model = Resturent
		fields = ['location']
		widgets = {'location': frm.OSMWidget(attrs={'map_width': 800, 
			'map_height': 500,}
)}
