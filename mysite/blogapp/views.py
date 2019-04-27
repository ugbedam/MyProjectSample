from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requests):
	return HttpResponse("<marquee><h1>Welcome To Damian Website</h1></marquee>")