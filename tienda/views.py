from django.db.models import Count
from .models import Producto
from django.shortcuts import render
from django.views import View

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def productos(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos' : producto})
 
class categoriaView(View):
    def get(self,request,val):
        producto = Producto.objects.filter(categoria=val)
        nombre = Producto.objects.filter(categoria=val).values('nombre').annotate(total=Count('nombre'))
        return render(request,'tienda/categoria.html',locals())
    

class productoDetalle(View):
    def get(self,request,pk):
        return render(request,"tienda/productodetalle.html", locals())