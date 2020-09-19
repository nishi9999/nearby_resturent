# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Resturent

from django.views import generic
from django.views.generic.list import ListView

from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from .forms import ResturentSearchForm

from search_views.search import SearchListView

from django.contrib.auth.mixins import LoginRequiredMixin

class ResturentSearchList(LoginRequiredMixin, SearchListView):
	login_url = '/login/'
	model = Resturent
	paginate_by = 10
	template_name= 'main/resturant_list.html'
	form_class = ResturentSearchForm

	def get_queryset(self):
		form = self.form_class(self.request.GET)
		if 'location' in form.data and form.data['location']: 
			location = eval(form.data['location'])
			longitude = location['coordinates'][0]
			latitude = location['coordinates'][1]
			user_location = Point(longitude, latitude, srid=4326)
			queryset = Resturent.objects.annotate(distance=Distance('location',
			user_location)
			).order_by('distance')[0:100]
			return queryset
		else:
			queryset = Resturent.objects.all()[0:100]
			return queryset
