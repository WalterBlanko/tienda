from django.urls import path
from .views import home, carrito, login, register, catalogo, admin

urlpatterns = [
    path('', home, name = 'home'),
    path('carrito', carrito, name = 'carrito'),
    path('login', login, name = 'login'),
    path('register', register, name = 'register'),
    path('catalogo', catalogo, name = 'catalogo'),
    path('admin menu', admin, name = 'admin_menu'),
]