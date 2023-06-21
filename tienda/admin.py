from django.contrib import admin
from .models import Producto, Cliente

# Register your models here.

admin.site.register(Producto)


@admin.register(Cliente)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'region', 'ciudad', 'celular']