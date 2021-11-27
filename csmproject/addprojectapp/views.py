from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def css(request):
    return render(request,"dashboard.html")

def table(request):
    return render(request,"tables.html")