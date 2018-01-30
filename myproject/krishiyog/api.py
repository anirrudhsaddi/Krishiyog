from django.contrib.auth.models import User

from tastypie import fields

from tastypie.resources import ModelResource

from krishiyog.models import farmer, farm,field



class UserResource(ModelResource):
		class Meta:
			queryset = User.objects.all()
			resource_name = 'user'
			fields = ['username']
										
										

class farmerResource(ModelResource):

		user = fields.ForeignKey(UserResource,'user')

		class Meta:
			queryset= farmer.objects.all()
			resouce_name='farmer'
			"authorization = Authorization()"

class farmResource(ModelResource):

		user = fields.ForeignKey(UserResource,'user')

		class Meta:
			queryset = farm.objects.all()
			resource_name = 'farm'
			"authorization =  Authorization()"


class fieldResource(ModelResource):

		user = fields.ForeignKey(UserResource,'user')

		class Meta:
			queryset = field.objects.all()
			resource_field = 'field'
			"authorization = Authorization()"

