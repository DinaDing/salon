from django.urls import path
from . import views 


app_name='haircut' 5

urlpatterns=[
    path("", views.home_page, name='home_page'), 
]