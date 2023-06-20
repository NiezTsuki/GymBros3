from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User


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
