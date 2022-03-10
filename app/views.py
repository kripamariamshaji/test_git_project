from django.shortcuts import render, loader
from django.shortcuts import HttpResponse

# from app.models import new

# Create your views here.

def form(request):
    return render(request, 'form.html')

def save(request):
    member = new(name=request.POST['name'], dob=request.POST['dob'], password=request.POST['password'], email=request.POST['email'], 
    select=request.POST['select'])

    member.save()
    return render(request, 'form.html')
def jishnu(request):
    return render(request,'emil.html')

def jishnu(request):
    return render(request,'emil.html')

def maria(request):
    return render(request,'maria.html')


def althaf(request):
    return render(request,'althaf.html')


