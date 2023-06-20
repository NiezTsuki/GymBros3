from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroCliente(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario', widget=forms.TextInput(attrs={'autofocus ' :'True', 'class' :'form-control'}))
    email= forms.EmailField(label= 'Correo Electronico', widget=forms.EmailInput(attrs={'class ' :'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class ' :'form-control'}))
    password2 = forms.CharField(label='Contraseña (Confirmación)', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
