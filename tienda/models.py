from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria     =models.AutoField(db_column='idCategoria', primary_key=True)
    categoria        =models.CharField(max_length=20, blank=False, null=False)
    

    def __str__(self):
        return str(self.categoria)


class Producto(models.Model):

    id_producto     = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    desc             = models.CharField(max_length=250)
    precio           = models.CharField(max_length=10)
    id_categoria     = models.ForeignKey(Categoria,on_delete=models.CASCADE, db_column='idCategoria')  
    imagen           = models.ImageField(upload_to="productos", null=True)
    activo           = models.IntegerField()


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.desc, self.precio, self.imagen)

    
