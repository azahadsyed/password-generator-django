from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
#	return HttpResponse("Hello World")
	return render(request,'generator/home.html')

def password(request):
	length= int(request.GET.get('length'))
	characters = list('abcdefghijklmnopqrstuvwxyz')
	thePassword=''

	if request.GET.get('uppers'):
		characters+= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

	if request.GET.get('nums'):
		characters+= list('0123456789')

	if request.GET.get('specials'):
		characters+= list('~!@#$%^&*()')


	for x in range(length):
		thePassword+=random.choice(characters)

	return render(request,'generator/password.html',{'password':thePassword})


def about(request):
#	return HttpResponse("Hello World")
	return render(request,'generator/about.html')

