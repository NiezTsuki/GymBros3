
from django.urls import path
from . import views

urlpatterns=[
    path("index", views.index, name='index'),
    path("mantenciones", views.mantenciones, name='mantenciones'),
    path("asesoramiento", views.asesoramiento, name='asesoramiento'),
    path('productos', views.productos, name='productos'),
    path("categoria/<slug:val>", views.categoriaView.as_view(),name="categoria"),
    path("productodetalle/<slug:pk>", views.productoDetalle.as_view(),name="productodetalle"),
]
