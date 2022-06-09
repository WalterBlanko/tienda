from django.db import models
from django import forms
from autoslug import AutoSlugField
# Create your models here.
# Modelo para Region
class Region(models.Model):
    idRegion = models.IntegerField(primary_key = True, verbose_name = 'Id de la region')
    nombreRegion = models.CharField(max_length= 80, verbose_name = 'Nombre de la region')
    def __str__(self):
        return self.nombreRegion

class Provincia(models.Model):
    idProvincia = models.IntegerField(primary_key = True, verbose_name = 'Id de la provincia')
    nombreProvincia = models.CharField(max_length= 80, verbose_name = 'Nombre de la provincia')
    Region = models.ForeignKey(Region, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreProvincia

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key = True, verbose_name = 'Id de la Comuna')
    nombreComuna = models.CharField(max_length= 80, verbose_name = 'Nombre de la Comuna')
    Provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreComuna

class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key = True, verbose_name = 'Id tipo usuario', default = 1)
    descripcion = models.CharField(max_length= 40, verbose_name = 'Tipo de usuario')

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name = 'Id del usuario')
    nombreUsuario = models.CharField(max_length = 80, verbose_name = 'Nombre del usuario')
    correoUsuario = models.CharField(max_length = 80, unique = True, verbose_name = 'Correo del usuario')
    passUsuario = models.CharField(max_length = 80, verbose_name = 'Password del usuario')
    Region = models.ForeignKey(Region, on_delete = models.CASCADE)
    Provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE)
    Comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE)
    def __str__(self):
        return self.correoUsuario

class Administrador(models.Model):
    idAdministrador = models.AutoField(primary_key = True, verbose_name = 'Id del administrador') 
    cargoAdministrador = models.CharField(max_length= 80, verbose_name = 'Cargo del administrador', default = 'null')
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE)
    def __str__(self):
        return self.cargoAdministrador

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key = True, verbose_name = 'Id del empleado')
    rolEmpleado = models.CharField(max_length= 80, verbose_name = 'Rol del empleado', default = 'null')
    Administrador = models.ForeignKey(Administrador, on_delete = models.CASCADE)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE)
    def __str__(self):
        return self.rolEmpleado

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de la categoria', default = 0) 
    nombreCategoria = models.CharField(max_length= 200, verbose_name = 'Nombre de la categoria', default = 'null')
    slug = AutoSlugField(populate_from='nombreCategoria', null=True)
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True, verbose_name = 'Codigo del Producto')
    nombreProducto = models.CharField(max_length= 100, verbose_name = 'Nombre del producto')
    slug = AutoSlugField(populate_from='nombreProducto', null=True)
    precioProducto = models.IntegerField(verbose_name = 'Precio del producto')
    descripcionProducto = models.CharField(max_length= 900, verbose_name = 'Descripcion del producto')
    imagen = models.ImageField(null=True, blank=True, upload_to="productos")
    Categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key = True, verbose_name = 'Id del cliente')
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE)
    def __str__(self):
        return self.idCliente

class Historial(models.Model):
    idCompra = models.AutoField(primary_key = True, verbose_name = 'Id de la compra')
    fechaCompra = models.DateField(verbose_name='Fecha de la compra')
    cantidadProductos = models.IntegerField(verbose_name = 'Cantidad de productos')
    totalCompra = models.IntegerField(verbose_name = 'Total de la compra') 
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    def __str__(self):
        return self.idCompra