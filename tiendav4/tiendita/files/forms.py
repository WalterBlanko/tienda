from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select
from .models import Usuario, Producto

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        verbose_name_plural = 'Usuarios'
        fields = ['nombreUsuario', 'correoUsuario', 'Region', 'Provincia', 'Comuna', 'passUsuario']
        widgets = {
            'nombreUsuario': TextInput(attrs = {
                'class': "form-control form-control-lg",
                'for': 'InputUsername',
                'placeholder': 'Nombre de usuario',
            }),
            'correoUsuario': EmailInput(attrs = {
                'class': "form-control form-control-lg",
                'for': 'InputRegEmail',
                'placeholder': 'Correo electronico',
            }),
            'Region': Select(attrs = {
                'class': 'form-select fs-5',
            }),
            'Provincia': Select(attrs = {
                'class': 'form-select fs-5',
            }),
            'Comuna': Select(attrs = {
                'class': 'form-select fs-5',
            }),
            'passUsuario': PasswordInput(attrs = {
                'class': "form-control form-control-lg",
                'for': "InputPassword",
                'placeholder': 'Contraseña',
                'type': 'password',
            }),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('correoUsuario')
        if Usuario.objects.filter(email = email).exists():
            raise forms.ValidationError(u'El email ya está registrado, prueba con otro')
        return email

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'descripcionProducto','imagen','Categoria']
