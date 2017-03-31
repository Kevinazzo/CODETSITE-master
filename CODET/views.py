from django.shortcuts import render

def home(request):
    return render(request,'Home.html')

def contacto(request):
    return render(request,'Contacto.html')

def planta(request):
    return render(request,'Planta.html')

def fabricaciones(request):
    return render(request,'Fabricaciones.html')