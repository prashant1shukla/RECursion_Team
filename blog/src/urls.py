from django.urls import path, include
from src import views
from .views import *

urlpatterns = [
    path('', views.home , name="home"),
    path('login', views.login , name="login"),
    path('register', views.register , name="register"),
    path('detail', views.detail , name="detail")
] 