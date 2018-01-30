from django.contrib.gis import admin
from .models import farm, farmer, field

# Register your models here.
admin.site.register(farmer)
admin.site.register(farm, admin.GeoModelAdmin)
admin.site.register(field, admin.GeoModelAdmin)

