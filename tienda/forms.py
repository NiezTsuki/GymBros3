from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User

from .models import Cliente


class LoginForm(AuthenticationForm):
    username = UsernameField(label ='Nombre Usuario', widget=forms.TextInput(attrs={'autofocus' :'True', 'class':'form-control'}))
    password = forms.CharField(label ='Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class FormularioRegistroCliente(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario', widget=forms.TextInput(attrs={'autofocus ' :'True', 'class' :'form-control'}))
    email= forms.EmailField(label= 'Correo Electronico', widget=forms.EmailInput(attrs={'class ' :'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class ' :'form-control'}))
    password2 = forms.CharField(label='Contraseña (Confirmación)', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput(attrs={'autofoucs' : 'True', 'autocomplete' : 'current-password', 'class' : 'form-control'}))
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))  


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirme Nueva Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'region', 'ciudad', 'celular', 'direccion']
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'region':forms.Select(attrs={'class': 'form-control'}),
            'ciudad':forms.TextInput(attrs={'class': 'form-control'}),
            'celular':forms.NumberInput(attrs={'class' : 'form-control'}),
            'direccion' :forms.TextInput(attrs={'class' : 'form-control'}),
        }


class AgregarProductoForm(forms.Form):
    producto_id = forms.CharField(label='ID del producto')
    cantidad = forms.IntegerField(label='Cantidad')
