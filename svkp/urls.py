from django.urls import path
from . import views

urlpatterns = [
	path('', views.svkp, name="svkp-home"),
	path('branches/', views.branches, name="branches"),
	path('address/', views.address, name="address"),
]