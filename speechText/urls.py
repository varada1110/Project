from django.urls import path
from . import views
urlpatterns = [

    path('speechText', views.speechText, name='speechText'),
]