from django.shortcuts import render

from .forms import UsuarioForm
from .models import Producto, Usuario

# Create your views here.
def home(request):
    return render(request, 'files/inicio.html')

def carrito(request):
    return render(request, 'files/carrito.html')

def login(request):
    return render(request, 'files/login.html')

def register(request):
    datos = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
    return render(request, 'files/register.html', datos)

def catalogo(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'files/catalogo.html', datos)

def admin(request):
    usuarios = Usuario.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request, 'files/adm.html', datos)