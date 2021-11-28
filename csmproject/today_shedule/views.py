from django.shortcuts import render

# Create your views here.
def tod_shed(request):
    return render(request,"today_shedule.html")