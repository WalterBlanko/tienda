from django.contrib import admin
from .models import Region, Provincia, Comuna, Usuario, Administrador, Empleado, Cliente, Historial, Categoria, Producto, Login
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# # Register your models here.

# admin.site.register(Region)
class RegionResource(resources.ModelResource):
    class Meta:
        model = Region

class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource

class ProvinciaResource(resources.ModelResource):
    class Meta:
        model = Provincia

class ProvinciaAdmin(ImportExportModelAdmin):
    resource_class = ProvinciaResource

class ComunaResource(resources.ModelResource):
    class Meta:
        model = Comuna

class ComunaAdmin(ImportExportModelAdmin):
    resource_class = ComunaResource

admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Historial)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Login)