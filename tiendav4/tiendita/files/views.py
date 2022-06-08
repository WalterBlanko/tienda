from django.shortcuts import render, HttpResponse,  redirect

from .forms import UsuarioForm, ProductoForm
from .models import Categoria, Empleado, Producto, Usuario, Login, Historial
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home(request):
    return render(request, 'files/inicio.html')

def carrito(request):
    return render(request, 'files/carrito.html')

# def login(request):
#     return render(request, 'files/login.html')

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


def administrador(request):
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    historial = Historial.objects.all()
    empleados = Empleado.objects.all()
    datos = {
        'usuarios': usuarios,
        'productos': productos,
        'categorias': categorias,
        'historial': historial,
        'empleados': empleados,
    }
    return render(request, 'files/adm.html', datos)

def login(request):
    if request.method == 'POST':
        email = request.POST['correoUsuario']
        encryptedpassword=make_password(request.POST['passUsuario'])
        checkpassword=check_password(request.POST['passUsuario'], encryptedpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Muchas gracias. Sus datos han sido robados, un abrazo')
    else:
        return render(request, 'files/login.html')

def catalogo(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'files/catalogo.html', datos)


def catalogo(request):
    template_name ='files/catalogo.html'
    
    categorias=Categoria.objects.filter()
    productos = Producto.objects.filter()
    context = {"productos":productos,"categorias":categorias}
    return render(request,template_name,context)

def buscar_categorias(request,slug):
    template_name='files/catalogo.html'
    cat=Categoria.objects.get(slug=slug)
    categorias = Categoria.objects.filter()
    productos=Producto.objects.filter(categoria=cat)
    context = {"productos":productos, "categorias":categorias}
    return render(request, template_name,context)



def form_cat(request):
    datos = {
        'form' :ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados con exito!!"

    return render(request, 'files/form_cat.html', datos)

def form_mod_cat(request, id):
    producto = Producto.objects.get(idProducto=id)

    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method=='POST':
        formulario = ProductoForm(request.POST,request.FILES, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'files/form_mod_cat.html', datos)

def form_del_cat(request, id):
    producto = Producto.objects.get(idProducto=id)

    producto.delete()

    return redirect(to="catalogo")