from django.urls import path
from . import views
urlpatterns = [

    path('login_user', views.login_user, name='login_user'),
    path('', views.main, name='main'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('txt_sp', views.txt_sp, name='txt_sp'),
    path('dumb',views.dumb, name='dumb'),
    path('option',views.option,name='option'),
]