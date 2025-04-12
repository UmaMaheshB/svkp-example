from django.http import HttpResponse
from django.shortcuts import render

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
