from django.urls import path
from .views import home, carrito, login, register, catalogo, test

urlpatterns = [
    path('', home, name = 'home'),
    path('carrito', carrito, name = 'carrito'),
    path('login', login, name = 'login'),
    path('register', register, name = 'register'),
    path('catalogo', catalogo, name = 'catalogo'),
    path('test', test, name = 'test'),
]