from django.contrib import admin
from sistema.models import Usuario
from sistema.models import Cama

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

admin.site.register(Usuario, usuarioAdmin)

class camaAdmin(admin.ModelAdmin):
    list_display = ['id','area','disponibilidad']

admin.site.register(Cama, camaAdmin)