from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_docter(request):
    return render(request,'register.html')
