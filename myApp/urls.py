from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('getProfile', views.getProfile, name="getProfile"),
    path('createProfile', views.createProfile, name="Create"),
]