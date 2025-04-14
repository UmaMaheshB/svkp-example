from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def svkp(request):
	return render(request, "svkp_home.html")

def branches(request):
	# static branches data
	temp = ["cse", "ece", "it", "eee", "civil", "mech"]
	return render(request, "branches_list.html", {"branches": temp})

def address(request):
	return render(request, "address.html")