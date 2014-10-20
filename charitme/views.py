from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Charit.me => This is the current HomePage")

def example(request):
	context = {}
	return render(request, 'example.html', context)


