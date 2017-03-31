from django.contrib import admin
from .models import Familia,Acabado,Subtipo,Material,Producto,TipoMedida

# Register your models here.
admin.site.register(Familia)
admin.site.register(Acabado)
admin.site.register(Subtipo)
admin.site.register(Material)
admin.site.register(Producto)
admin.site.register(TipoMedida)