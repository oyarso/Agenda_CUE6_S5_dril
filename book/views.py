from django.views.generic import TemplateView 
from django.shortcuts import render 
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Bienvenidos a mi sitio de libros") 

class IndexPageView(TemplateView): 
    template_name = "index.html" 

def navbarView(request): 
    template_name = 'navbar.html' 
    return render(request, template_name)