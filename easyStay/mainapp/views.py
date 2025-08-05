from django.shortcuts import render
from django.views.generic import ListView
from .models import Building
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