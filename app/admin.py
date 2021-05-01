# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

@admin.register(Empleado)
class ClienteDetail(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'rut', 'usuario', 'clave']
    
    fieldsets = (
        ('Datos Personales', {
            'fields':('id', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'rut')
        }),
        ('Datos de Acceso', {
            'fields':('usuario', 'clave')
        })
    )

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Ticket)
admin.site.register(Categoria)
# Register your models here.
