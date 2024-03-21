from django.shortcuts import render
from django.http import HttpResponse
def index_views (request):
    return render(request,'website/index.html')
def about_views (request):
    return render(request,'website/about.html')
def service_views (request):
    return render(request,'website/service.html')

# Create your views here.
