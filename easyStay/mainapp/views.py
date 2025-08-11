from django.shortcuts import render
from django.views.generic import ListView
from .models import Building, BuildingImage
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.


class HomeView(ListView):
    model = Building
    template_name = 'home.html'
    context_object_name = 'buildings'
    
    
def contactView(request):
    template='contact.html'
    context={
        
    }
    return render(request,template,context)
def aboutView(request):
    template='about.html'
    context={
        
        
    }
class AddBuilding(CreateView):
    model = Building
    template_name = 'add_building.html'
    fields = '__all__'
    success_url = '/'
    
def addBuildingImage(request, building_id):
    if request.method == 'GET':
        template = 'add_building_image.html'
        # form = 
        context = {
            
        }
    elif request.method == 'POST':
        img = request.POST.get('img')
        title = request.POST.get('title')
        this_building = Building.objects.get(id = building_id)
        building_image = BuildingImage.objects.create(building=this_building)
    
    
class BuildingDetails(DetailView):
    model = Building
    template_name = 'building_details.html'
    context_object_name = 'building'

class UpdateBuilding(UpdateView):
    model = Building
    template_name = 'update_building.html'
    fields = '__all__'
    success_url = '/'

class DeleteBuilding(DeleteView):
    model = Building
    template_name = 'delete_building.html'
    success_url = '/'