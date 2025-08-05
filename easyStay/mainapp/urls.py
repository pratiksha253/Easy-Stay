from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomeView.as_view(),name='homepage'),
    path('contact',views.contactView,name='contactpage'),
    path('about',views.aboutView,name='aboutpage'),
]
