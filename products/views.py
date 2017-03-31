from django.shortcuts import render
from products import models


def home(request):
    Tornilloslist=models.Familia.objects.filter(nombre="Tornillo")
    Tuercaslist=models.Familia.objects.filter(nombre="Tuerca")
    Varillaslist=models.Familia.objects.filter(nombre="Varilla")
    Arandelaslist=models.Familia.objects.filter(nombre="Arandelas")
    Pijaslist=models.Familia.objects.filter(nombre="Pijas")
    context = {
        'Tornillos':models.Subtipo.objects.filter(familia_ID=Tornilloslist),
        'Tuercas':models.Subtipo.objects.filter(familia_ID=Tuercaslist),
        'Varillas':models.Subtipo.objects.filter(familia_ID=Varillaslist),
        'Arandelas':models.Subtipo.objects.filter(familia_ID=Arandelaslist),
        'Pijas':models.Subtipo.objects.filter(familia_ID=Pijaslist),
    }
    return render(request,'Productos.html',context)

def sublist(request, subtipo_ID):
    cacho = models.Subtipo.objects.filter(id=subtipo_ID)
    context = {'listita':models.Producto.objects.filter(subtipo_ID=cacho),}
    return render(request,'ProductosList.html',context)