from django.db.models import Count
from .models import Cliente, Producto
from django.shortcuts import render
from django.views import View
from . forms import FormularioRegistroCliente, CustomerProfileForm
from django.contrib import messages

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
        return render(request,"tienda/productodetalle.html",locals())
    
class registroClienteView(View):
    def get(self,request):
        form = FormularioRegistroCliente()
        return render(request, 'tienda/registrocliente.html', locals())
    def post(self,request):
        form = FormularioRegistroCliente(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuario Registrado Exitosamente!")
        else:
            messages.warning(request,"Error al Registrar!")
        return render(request, 'tienda/registrocliente.html', locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'tienda/profile.html', locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usuario = request.user
            nombre  = form.cleaned_data['nombre']
            region  = form.cleaned_data['region']
            ciudad  = form.cleaned_data['ciudad']
            celular = form.cleaned_data['celular']

            reg = Cliente(usuario=usuario, nombre=nombre, region=region, ciudad=ciudad, celular=celular)
            reg.save()
            messages.success(request, "Perfil Guardado Exitosamente!")
        else:
            messages.warning(request, "Error al Guardar!")
        return render(request, 'tienda/profile.html', locals())

def Direccion(request):
    add = Cliente.objects.filter(usuario=request.user)
    return render(request, 'tienda/direccion.html', locals())