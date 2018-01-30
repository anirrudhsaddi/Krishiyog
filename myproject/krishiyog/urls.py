from django.conf.urls import url
from .import views

urlpatterns=[

	url(r'^$', views.items_list, name='items_list'),
	url(r'^farmers_list/$', views.farmers_list, name='farmers_list'),
	url(r'^add/farmer/$', views.add_farmer, name='add_farmer'),
	url(r'^edit/farmer/(?P<pk>\d+)/$', views.edit_farmer, name='edit_farmer'),
	url(r'^delete/farmer/(?P<id>\d+)/$', views.delete_farmer, name='delete_farmer'),
	url(r'^farms_list/$', views.farms_list, name='farms_list'),
	url(r'^add/farm/$', views.add_farm, name='add_farm'),
	url(r'^edit/farm/(?P<pk>\d+)/$', views.edit_farm, name='edit_farm'),
	url(r'^delete/farm/(?P<id>\d+)/$', views.delete_farm, name='delete_farm'),
	url(r'^fields_list/$', views.fields_list, name='fields_list'),
	url(r'^add/fields/$', views.add_fields, name='add_fields'),
	url(r'^edit/fields/(?P<pk>\d+)/$', views.edit_fields, name='edit_fields'),
	url(r'^delete/fields/(?P<id>\d+)/$', views.delete_fields, name='delete_fields'),
	


]
