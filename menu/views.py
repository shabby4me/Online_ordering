from django.shortcuts import render
from django.http import HttpResponse
from .models import Menus

# Create your views here.

def menu(request):
	menu = Menus.objects.all()
	context = { 'menu':menu }
	return render(request, 'menu/home.html', context)
	
def order(request):
	menu = Menus.objects.all()
	context = { 'menu':menu }
	return render(request, 'menu/order.html', context)
