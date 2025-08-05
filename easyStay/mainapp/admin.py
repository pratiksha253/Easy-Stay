from django.contrib import admin
from .models import Building, BuildingType, Address, Facility

# Register your models here.
admin.site.register(Building)
admin.site.register(Address)
admin.site.register(BuildingType)
admin.site.register(Facility)
