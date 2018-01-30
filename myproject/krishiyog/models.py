#from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.db.models.manager import GeoManager
from django.core.validators import MaxValueValidator, MinValueValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import GEOSGeometry



"""def ValidateField(multipolygon, farmname):

	geos_field = GEOSGeometry(multipolygon)
	farm_s = farm.objects.get(farm_name = farmname)

	geos_farm=GEOSGeometry(farm_s.geo_farm)
    
	if not(geos_field.within(goes_farm)):
		raise ValidationError(
		_('Field is not inside the selected farm %(farm)'),
		params={'farmname': farmname},
        )"""

# Create your models here.

class farmer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number_of_farms = models.IntegerField(default=0, validators=[MaxValueValidator(9999999), MinValueValidator(0)])

    def __str__(self):
	      return self.first_name

class farm(models.Model):

    owner = models.ForeignKey(farmer, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=30)
    geo_farm = models.MultiPolygonField(srid=4326)
    objects = models.Manager()
    def __str__(self):
		    return self.farm_name     
																										    
		
class field(models.Model):

    #Specifying choices for the season. The model will not accept any other season than those specified here. 
    RABI = 'RABI'
    KHARIF = 'KHARIF'
    SEASON_CHOICES = (
        (RABI, 'rabi'),
        (KHARIF, 'kharif'),
    )

    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    crop = models.CharField(max_length=200)
    year = models.IntegerField(default=0, validators=[MaxValueValidator(9999), MinValueValidator(1900)])
    season = models.CharField(max_length=6,default='rabi', choices = SEASON_CHOICES)
    geo_field = models.MultiPolygonField(srid=4326)
    """geo_field = models.MultiPolygonField(srid=4326, validators =[ValidateField(geo_field,farm)])"""
    objects = models.Manager()
    
    # Def save() is called by the model when you click the save button to the database. Validation of the multipolygon field is done here before being saved.	
    def clean(self, *args, **kwargs):
        # add custom validation here
        print (self.geo_field, '\n New line')
        geos_field = GEOSGeometry(self.geo_field)
        print (self.geo_field, '\n New line')
        farm_s = farm.objects.get(farm_name = self.farm)
	
        geos_farm=GEOSGeometry(farm_s.geo_farm)
     
    
        if not(geos_field.within(geos_farm)):              # GEOS method check if field is within the farm, returns a T or F. 
            raise ValidationError(
            _('Field is not inside the selected farm'),
            #params={'farm': farm_s.farm_name },
            )

        super(field, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(field, self).save(*args, **kwargs)






