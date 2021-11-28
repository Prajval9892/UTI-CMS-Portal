from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_emp(request):
    return render(request,"add_emp.html")