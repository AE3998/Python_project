from django.shortcuts import render

# Quiero saber para que es esto 
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to social book</h1>')