from django.db import models

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

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key = True, verbose_name = 'Id del usuario')
    nombreUsuario = models.CharField(max_length= 80, verbose_name = 'Nombre del usuario')
    correoUsuario = models.CharField(max_length= 80, verbose_name = 'Correo del usuario')
    passUsuario = models.CharField(max_length= 80, verbose_name = 'Password del usuario')
    Region = models.ForeignKey(Region, on_delete = models.CASCADE)
    Provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE)
    Comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreUsuario

class Administrador(models.Model):
    idAdministrador = models.IntegerField(primary_key = True, verbose_name = 'Id del administrador') 
    cargoAdministrador = models.CharField(max_length= 80, verbose_name = 'Cargo del administrador', default = 'null')
    Usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.cargoAdministrador

class Empleado(models.Model):
    idEmpleado = models.IntegerField(primary_key = True, verbose_name = 'Id del empleado')
    rolEmpleado = models.CharField(max_length= 80, verbose_name = 'Rol del empleado', default = 'null')
    Administrador = models.ForeignKey(Administrador, on_delete = models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.rolEmpleado

class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key = True, verbose_name = 'Id del cliente')
    Usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.idCliente

class Historial(models.Model):
    idCompra = models.IntegerField(primary_key = True, verbose_name = 'Id de la compra')
    cantidadProductos = models.IntegerField(verbose_name = 'Cantidad de productos')
    totalCompra = models.IntegerField(verbose_name = 'Total de la compra') 
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        return self.idCompra

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de la categoria', default = 0) 
    nombreCategoria = models.CharField(max_length= 100, verbose_name = 'Nombre de la categoria', default = 'null')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key = True, verbose_name = 'Id del producto')
    nombreProducto = models.CharField(max_length= 100, verbose_name = 'Nombre del producto')
    precioProducto = models.IntegerField(verbose_name = 'precio del producto')
    descripcionProducto = models.CharField(max_length= 900, verbose_name = 'Descripcion del producto')
    Categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreProducto