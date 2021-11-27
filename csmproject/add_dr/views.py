from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_docter(request):
    return  HttpResponse("Dr added")
