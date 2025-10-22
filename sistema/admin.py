from django.contrib import admin
from sistema.models import Usuario

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

admin.site.register(Usuario, usuarioAdmin)