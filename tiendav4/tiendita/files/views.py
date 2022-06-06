from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'files/inicio.html')

def carrito(request):
    return render(request, 'files/carrito.html')

def login(request):
    return render(request, 'files/login.html')

def register(request):
    return render(request, 'files/register.html')

def catalogo(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'files/catalogo.html', datos)

def test(request):
    return render(request, 'files/base.html')