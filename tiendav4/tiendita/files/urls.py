from django.urls import path
from .views import home, carrito, login, register, catalogo, administrador, buscar_categorias, form_cat, form_mod_cat, form_del_cat

urlpatterns = [
    path('', home, name = 'home'),
    path('carrito', carrito, name = 'carrito'),
    path('login', login, name = 'login'),
    path('register', register, name = 'register'),
    path('catalogo', catalogo, name = 'catalogo'),
    path('admin-menu', administrador, name = 'admin_menu'),
    path('catalogo/<slug>', buscar_categorias, name = 'catalogo'),
    path('form-cat', form_cat, name = 'form_cat'),
    path('form-mod-cat/<id>', form_mod_cat, name = 'form_mod_cat'),
    path('form-del-cat/<id>', form_del_cat, name = 'form_del_cat'),
]