from django.urls import path 
from .views import IndexPageView, navbarView 
urlpatterns = [ 
path('', IndexPageView.as_view(), name='index'), 
path('navbar/', navbarView, name='navbar'), 
] 