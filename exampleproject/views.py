from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

API_KEY = "38afcde461bc4981ae9ff6622178f077"


def home(request):
	return redirect("svkp-home")

def hello(request):

	print("one")
	print("two")
	return HttpResponse("Hello world!")

def goodmorning(request):
	return HttpResponse('<p style="color:red">Good morning svkp students</p>')

def goodevening(request, college):
	html = f'''
	<body>
	<marquee>Good Evening: {college}</marquee>
	</body>
	'''
	return HttpResponse(html)

def numbers(request, rows, cols):
	data = []
	numbers = 1
	for rows_ in range(rows):
		temp = []
		for col in range(cols):
			temp.append(numbers)
			numbers += 1
		data.append(temp)
	return render(request, "numbers.html", {"data": data})

def weather(request):
	city = request.GET.get("city")
	print("City: ", city)
	if not city:
		return render(request, "weather.html", {"weather": ""})
	else:
		URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
		response = requests.get(URL)
		data = response.json()

		weather_info = {}
		if response.status_code == 200:
			weather_info = {
				"city": city,
				"tempreature": data["main"]['temp'],
				"description": data['weather'][0]['description'],
				"icon": data['weather'][0]['icon']
			}

		return render(request, "weather.html", {"weather": weather_info})