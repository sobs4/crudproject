from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,You're at the polls index.")

def indexAgain(request):
    return HttpResponse("Hello,You're at the polls again index.")