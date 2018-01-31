from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .forms import farmerForm, farmForm, fieldForm
from .models import farmer, farm, field


def index(request):

	return HttpResponse("You are at the landing page for Krishiyog's demo module")

# Create your views here.
#Views generate here are very crude. Can be more efficient. 

def items_list(request):
	year_list  = field.objects.values('year').distinct()        #gets a list of unique 'years' entered into the database instead of a full list of years, TODO: needs to be sorted
	season_list = field.objects.values('season').distinct()     #gets a list of unique seasons. TODO: avoid calling the database, create a local choice since season are limited and are predefined in the model
	
	return render(request, 'krishiyog/items_list.html', {'year_list': year_list, 'season_list': season_list })

def farmers_list(request):
	farmers_list = farmer.objects.all()
	return render(request, 'krishiyog/farmers_list.html',{'farmers_list':farmers_list})

def add_farmer(request):
		
		if request.method == "POST":
				form = farmerForm(request.POST)

				if form.is_valid():
						farmer_item = form.save(commit=False)
						farmer_item.save()
						return redirect('/farmers_list/')

		else:
				form = farmerForm()

		return render(request, 'krishiyog/add_farmer.html',{'form':form})

				
def edit_farmer(request, pk=None):
		# Request is a GET method so it skips past to ELSE. POST request comes through when the save button is clicked. 
		print ('Method request for edit:', request.method)
		item=get_object_or_404(farmer, pk=pk)
		if request.method=="POST":
			
			form=farmerForm(request.POST, instance=item)
			if form.is_valid():
				item=form.save(commit=False)
				item.save()
				return redirect('/farmers_list/')

		else:

			form=farmerForm(instance=item)
			context = {

					"first_name" : item.first_name,
					"last_name" : item.last_name,
					"number_of_farms" : item.number_of_farms,
					"item" : item,
					"form": form,

					}
			return render(request, 'krishiyog/edit_farmer.html', context)


def delete_farmer(request, id=None):
		#HTML Form methods are limited to GET and POST, using the post method to identify delete call in delete view
		if request.method=="POST":
			farmer.objects.filter(id=id).delete()
			return redirect('/farmers_list/')

'''======================================================================================================='''
def farms_list(request):
	if request.method=='POST':
	
		farms_list = farm.objects.all()
		return render(request, 'krishiyog/farms_list.html',{'farms_list':farms_list})
		
	farms_list = farm.objects.all()
	
	return render(request, 'krishiyog/farms_list.html',{'farms_list':farms_list})

def add_farm(request):
		
		if request.method == "POST":
				form = farmForm(request.POST)

				if form.is_valid():
						farm_item = form.save(commit=False)
						farm_item.save()
						return redirect('/farms_list/')

		else:
			
			form= farmForm()
			
		return render(request, 'krishiyog/add_farm.html',{"form": form})

def edit_farm(request, pk=None):
		
		print ('Medthod request for edit:', request.method)
		item=get_object_or_404(farm, pk=pk)
		if request.method=="POST":

			
			print (item)
			form=farmForm(request.POST, instance=item)
			print (form)
			if form.is_valid():
				item=form.save(commit=False)
				item.save()
				return redirect('/farms_list/')

		else:		
			
			farm_geojson = item.geo_farm.geojson            
			
			form = farmForm(instance=item)
			context = {

					"owner" : item.owner,
					"farm_name" : item.farm_name,
					"geo_farm" : farm_geojson,
					"item" : item,
					"form" : form,

					}
		return render(request, 'krishiyog/edit_farm.html', context)


def delete_farm(request, id=None):

		if request.method=="POST":
			farm.objects.filter(id=id).delete()
			return redirect('/farms_list/')


'''============================================================================================'''
def fields_list(request):
	if request.method=='POST':
		year = request.POST['year']
		season = request.POST['season']
		fields_list = field.objects.filter(year=year, season=season)
		return render(request, 'krishiyog/fields_list.html',{'fields_list':fields_list})
		
		
	fields_list = field.objects.all()
	return render(request, 'krishiyog/fields_list.html',{'fields_list':fields_list})


def add_fields(request):
		if request.method == "POST":
				form = fieldForm(request.POST)

				if form.is_valid():
						field_item = form.save(commit=False)
						field_item.save()
						return redirect('/fields_list/')

		else:
				form = fieldForm()

		return render(request, 'krishiyog/add_fields.html',{'form':form})

def edit_fields(request, pk=None):
		
		print ('Medthod request for edit:', request.method)
		item=get_object_or_404(field, pk=pk)
		if request.method=="POST":

			
			print (pk,item)
			form=fieldForm(request.POST, instance=item)
			print ('checking if post is bound')
			if form.is_valid():
				item=form.save(commit=False)
				item.save()
				return redirect('/fields_list/', id=item.id)

		else:
			form =fieldForm(instance=item)
			#"year" : item.year,
			#"season":item.season,			
			
		return render( request, 'krishiyog/edit_fields.html', {'form':form})


def delete_fields(request, id=None):

		if request.method=="POST":
			field.objects.filter(id=id).delete()
			return redirect('/fields_list/')

'''================================================================================================'''


		
		
