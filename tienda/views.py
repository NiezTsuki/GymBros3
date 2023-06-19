from django.db.models import Count
from .models import Producto
from django.shortcuts import render
from django.views import View

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def mantenciones(request):
    return render(request,'tienda/mantenciones.html')

def asesoramiento(request):
    return render(request,'tienda/asesoramiento.html')

def productos(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos' : producto})
 
class categoriaView(View):
    def get(self,request,val):
        producto = Producto.objects.filter(categoria=val)
        nombre = Producto.objects.filter(categoria=val).values('nombre')
        return render(request,'tienda/categoria.html',locals())
    

class productoDetalle(View):
    def get(self,request,pk):
        producto = Producto.objects.get(pk=pk)
        return render(request,"tienda/productodetalle.html", locals())