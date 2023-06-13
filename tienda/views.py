from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def productos(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos' : producto})
    