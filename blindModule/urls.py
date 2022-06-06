from django.urls import path
from . import views
urlpatterns = [

    path('blindModule', views.blindModule, name='blindModule'),
    
]