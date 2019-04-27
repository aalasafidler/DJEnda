from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def gallery(request):
	return render(request, 'gallery.html')

def contact(request):
	return render(request, 'contact.html')

def events(request):
	return render(request, 'events.html')