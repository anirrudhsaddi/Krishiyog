from django.forms import ModelForm, ModelChoiceField
from django.contrib.gis import forms
#import floppyforms as forms
from .models import farm, farmer, field

'''class MultiPolygonWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    google_maps_api_key ='AIzaSyAAp4omklROH-xmZ29A5IH2VZCFL5BHPOw'''

class farmForm(ModelForm):
	

	#geo_farm = forms.MultiPolygonField(widget=forms.OSMWidget(attrs = {'map_width':800, 'map_height': 500}))
	
	class Meta:
			model=farm
			fields=['owner', 'farm_name','geo_farm']
	

class farmerForm(ModelForm):

		
		class Meta:
				model=farmer
				fields= ['first_name','last_name','number_of_farms']

class fieldForm(ModelForm):

		class Meta:
				model=field
				fields=['farm','crop', 'year', 'season', 'geo_field']



																																																																							
