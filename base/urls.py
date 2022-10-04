from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('overview', views.overview, name='overview'),
    path('register', views.register, name='register'),
    path('change_password', views.change_password, name='change_password'),
]
