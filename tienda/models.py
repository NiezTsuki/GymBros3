from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('MS', 'Mancuernas'),
    ('BO', 'Barras Olímpicas'),
    ('DO', 'Discos Olímpicos'),
    ('MC', 'Máquinas Cardio'),
    ('BR', 'Bancas y Racks'),
)


class Producto(models.Model):

    id_producto      = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    desc             = models.CharField(max_length=250)
    precio           = models.CharField(max_length=10)
    categoria        = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  
    imagen           = models.ImageField(upload_to="productos", null=True)


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.desc, self.precio, self.imagen)

    
