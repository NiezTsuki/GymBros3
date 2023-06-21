# Generated by Django 4.1.2 on 2023-06-20 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('region', models.CharField(choices=[('RM', 'Región Metropolitana de Santiago'), ('I', 'Región de Tarapacá'), ('II', 'Región de Antofagasta'), ('III', 'Región de Atacama'), ('IV', 'Región de Coquimbo'), ('V', 'Región de Valparaíso'), ('VI', 'Región del Libertador Bernardo OHiggins'), ('VII', 'Región del Maule'), ('VIII', 'Región del Bío Bío'), ('IX', 'Región de la Araucanía'), ('X', 'Región de los Lagos'), ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'), ('XII', 'Región de Magallanes y la Antártica Chilena'), ('XIV', 'Región de Los Ríos'), ('XV', 'Región de Arica-Parinacota')], max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('celular', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]