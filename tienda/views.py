from django.db.models import Count
from .models import Cliente, Producto, Carro
from django.shortcuts import render, redirect
from django.views import View
from . forms import FormularioRegistroCliente, CustomerProfileForm, LoginForm
from django.contrib import messages

# Create your views here.

def home(request):
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
            usuario   = request.user
            nombre    = form.cleaned_data['nombre']
            region    = form.cleaned_data['region']
            ciudad    = form.cleaned_data['ciudad']
            celular   = form.cleaned_data['celular']
            direccion = form.cleaned_data['direccion']

            reg = Cliente(usuario=usuario, nombre=nombre, region=region, ciudad=ciudad, celular=celular, direccion=direccion)
            reg.save()
            messages.success(request, "Perfil Guardado Exitosamente!")
        else:
            messages.warning(request, "Error al Guardar!")
        return render(request, 'tienda/profile.html', locals())

def Direccion(request):
    add = Cliente.objects.filter(usuario=request.user)
    return render(request, 'tienda/direccion.html', locals())



class UpdateDireccion(View):
    def get(self,request,pk):
        add  = Cliente.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'tienda/actualizardireccion.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add           = Cliente.objects.get(pk=pk)
            add.nombre    = form.cleaned_data['nombre']
            add.region    = form.cleaned_data['region']
            add.ciudad    = form.cleaned_data['ciudad']
            add.celular   = form.cleaned_data['celular']
            add.direccion = form.cleaned_data['direccion']
            add.save()
            messages.success(request, "Perfil Actualizado Exitosamente!")
        else:
            messages.warning(request, "Error al Guardar!")
        return redirect('direccion')

def add_to_cart(request):
    user = request.user
    id_producto = request.GET.get('prod_id')
    producto = Producto.objects.get(id=id_producto)
    Carro(user=user, producto=producto).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Carro.objects.filter(user=user)
    return render(request, 'tienda/addtocart.html',locals())