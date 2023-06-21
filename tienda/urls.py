
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm

urlpatterns=[
    path("index", views.index, name='index'),
    path("mantenciones", views.mantenciones, name='mantenciones'),
    path("asesoramiento", views.asesoramiento, name='asesoramiento'),
    path('productos', views.productos, name='productos'),
    path("categoria/<slug:val>", views.categoriaView.as_view(),name="categoria"),
    path("productodetalle/<slug:pk>", views.productoDetalle.as_view(),name="productodetalle"),
    path("profile/", views.ProfileView.as_view(), name='profile'),

    #login autentificacion

    path('registro/', views.registroClienteView.as_view(), name='registrocliente'),
    path('cuentas/login/', auth_view.LoginView.as_view(template_name='tienda/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='tienda/passwordreset.html', form_class=MyPasswordResetForm), name='password_reset'),

]
