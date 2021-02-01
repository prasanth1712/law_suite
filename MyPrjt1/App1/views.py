from django.shortcuts import render

# Create your views here.

def appindex(request):
    return render(request,'app1/app1.html')
