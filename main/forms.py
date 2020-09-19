from .models import Resturent
from django import forms

from django.forms import ModelForm

# import floppyforms as forms


# class GMapPointWidget(forms.gis.BaseGMapWidget, forms.gis.PointWidget):
#     google_maps_api_key = 'my-key'


class ResturentSearchForm(ModelForm):
	class Meta:
		model = Resturent
		fields = ['location']
		# widgets = {'location': GMapPointWidget(attrs={'map_width': 1000,
  #                                              'map_height': 500,
  #                                              'is_point': True,
  #                                              'mouse_position': True,
  #                                              'point_zoom': 1})}