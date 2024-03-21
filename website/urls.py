from django.urls import path
from website.views import *
app_name='website'
urlpatterns = [
    path('',index_views,name='index'),
    path('about/',about_views,name='about'),
    path('service/',service_views,name='service')
]