from django.urls import path
from . import views

urlpatterns = [
	path('', views.svkp),
	path('branches/', views.branches),
	path('address/', views.address),

]