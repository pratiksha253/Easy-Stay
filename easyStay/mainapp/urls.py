from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomeView.as_view(),name='homepage'),
    path('contact',views.contactView,name='contactpage'),
    path('about',views.aboutView,name='aboutpage'),
    path('building/add', views.AddBuilding.as_view(), name = 'addbuilding'),
    path('building/<int:pk>', views.BuildingDetails.as_view(), name= 'building_details'),
    path('building/update/<int:pk>', views.UpdateBuilding.as_view(), name = 'updatebuilding'),
    path('building/delete/<int:pk>', views.DeleteBuilding.as_view(), name = 'deletebuilding'),
]
