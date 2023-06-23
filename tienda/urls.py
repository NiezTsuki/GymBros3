
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns=[
    path("index", views.index, name='index'),
    path("mantenciones", views.mantenciones, name='mantenciones'),
    path("asesoramiento", views.asesoramiento, name='asesoramiento'),
    path('productos', views.productos, name='productos'),
    path("categoria/<slug:val>", views.categoriaView.as_view(),name="categoria"),
    path("productodetalle/<slug:pk>", views.productoDetalle.as_view(),name="productodetalle"),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("direccion/", views.Direccion, name='direccion'),
    path("actualizardireccion/<int:pk>", views.UpdateDireccion.as_view(), name='actualizardireccion'),

    #login autentificacion

    path('registro/', views.registroClienteView.as_view(), name='registrocliente'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='tienda/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='tienda/changepassword.html', form_class=MyPasswordChangeForm, success_url='/tienda/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='tienda/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='tienda/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='tienda/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='tienda/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='tienda/password_reset_complete.html'), name='password_reset_complete'),

]
