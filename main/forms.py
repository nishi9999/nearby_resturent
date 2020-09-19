from .models import Resturent
from django import forms

from django.contrib.gis import forms as frm


from django.forms import ModelForm

# import floppyforms as forms


# class GMapPointWidget(forms.gis.BaseGMapWidget, forms.gis.PointWidget):
#     google_maps_api_key = 'my-key'


class ResturentSearchForm(ModelForm):
	class Meta:
		model = Resturent
		fields = ['location']
		widgets = {'location': frm.OSMWidget(attrs={'map_width': 800, 
			'map_height': 500,
			})
			}
		# widgets = {'location': GMapPointWidget(attrs={'map_width': 1000,
  #                                              'map_height': 500,
  #                                              'is_point': True,
  #                                              'mouse_position': True,
  #                                              'point_zoom': 1})}