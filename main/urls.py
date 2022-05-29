from django.urls import path
from . import views
urlpatterns = [

    path('login_user', views.login_user, name='login_user'),
    path('login_user1', views.login_user1, name='login_user1'),
    path('login_user2', views.login_user2, name='login_user2'),
    path('', views.main, name='main'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('txt_sp', views.txt_sp, name='txt_sp'),
    path('dumb',views.dumb, name='dumb'),
]