from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('MS', 'Mancuernas'),
    ('BO', 'Barras Olímpicas'),
    ('DO', 'Discos Olímpicos'),
    ('MC', 'Máquinas Cardio'),
    ('BR', 'Bancas y Racks'),
)

REGION_CHOICES = (
    ('RM', 'Región Metropolitana de Santiago'), 
    ('I', 'Región de Tarapacá'), 
    ('II', 'Región de Antofagasta'),
    ('III', 'Región de Atacama'), 
    ('IV', 'Región de Coquimbo'), 
    ('V', 'Región de Valparaíso'), 
    ('VI', 'Región del Libertador Bernardo OHiggins'), 
    ('VII', 'Región del Maule'), 
    ('VIII', 'Región del Bío Bío'), 
    ('IX', 'Región de la Araucanía'), 
    ('X', 'Región de los Lagos'), 
    ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'), 
    ('XII', 'Región de Magallanes y la Antártica Chilena'), 
    ('XIV', 'Región de Los Ríos'), 
    ('XV', 'Región de Arica-Parinacota'))

class Producto(models.Model):

    id_producto      = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=50)
    desc             = models.CharField(max_length=250)
    precio           = models.CharField(max_length=10)
    categoria        = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  
    imagen           = models.ImageField(upload_to="productos", null=True)


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.desc, self.precio, self.imagen)

class Cliente(models.Model):
    usuario   = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre    = models.CharField(max_length=200)
    region    = models.CharField(choices=REGION_CHOICES, max_length=200)
    ciudad    = models.CharField(max_length=50)
    celular   = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Carro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def costo_total(self):
        return self.cantidad * self.producto.precio
