from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Building, BuildingImage
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


from .forms import BuildingImageForm
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
    return render(request,template,context)
class AddBuilding(CreateView):
    model = Building
    template_name = 'add_building.html'
    fields = '__all__'
    success_url = '/'
    
    
    

    
class BuildingDetails(DetailView):
    model = Building
    template_name = 'building_details.html'
    context_object_name = 'building'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        images = BuildingImage.objects.filter(building = self.object)
        context['images'] = images
        return context

class UpdateBuilding(UpdateView):
    model = Building
    template_name = 'update_building.html'
    fields = '__all__'
    success_url = '/'

class DeleteBuilding(DeleteView):
    model = Building
    template_name = 'delete_building.html'
    success_url = '/'
    
class AddBuildingPictures(CreateView):
    model = BuildingImage
    template_name = 'add_pictures.html'
    form_class = BuildingImageForm
    # success_url = '/'
    
    
    
    def form_valid(self, form):
        form.instance.building = Building.objects.get(id = self.kwargs['building_id'])
        return super().form_valid(form)

def searchView(request):
    query=request.GET.get('q')
    result_building=Building.objects.filter(name_icontains = query)
    context = {
        'buildings' : result_building,
        'query' : query,
        'search_bar' : True
    }
    template = loader.get_template('search_result.html')
    return HttpResponse(template.render(context,request))