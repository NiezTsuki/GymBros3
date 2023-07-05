from django.db.models import Count
from .models import Cliente, Producto, Carro
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . forms import FormularioRegistroCliente, CustomerProfileForm, LoginForm, AgregarProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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

@login_required
def carro_compras(request):
    carros = Carro.objects.filter(usuario=request.user)
    total = 0
    cantidad_productos = 0
    for carro in carros:
        subtotal = carro.cantidad * int(carro.producto.precio)
        total += subtotal
        carro.subtotal = subtotal  # Agregamos el subtotal al objeto carro
        cantidad_productos += carro.cantidad

    context = {
        'carros': carros,
        'total': total,
        'cantidad_productos': cantidad_productos,
        'cantidad_productos_carro': request.session.get('cantidad_productos_carro', 0)
    }

    return render(request, 'tienda/carro_compras.html', context)

@login_required
def agregar_producto_carro(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))

    try:
        carro = Carro.objects.get(usuario=request.user, producto=producto)
        carro.cantidad += cantidad
        carro.save()
    except Carro.DoesNotExist:
        carro = Carro.objects.create(usuario=request.user, producto=producto, cantidad=cantidad)

    # Actualizar la variable de sesión
    request.session['cantidad_productos_carro'] = Carro.objects.filter(usuario=request.user).count()

    return redirect('carro_compras')

@login_required
def eliminar_producto_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    carro.delete()
    
    # Actualizar la variable de sesión
    request.session['cantidad_productos_carro'] = Carro.objects.filter(usuario=request.user).count()

    return redirect('carro_compras')






