# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    descuento = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100, blank=True)
    precio_costo = models.IntegerField(blank=True)
    precio_venta = models.IntegerField(blank=True)
    inventario = models.IntegerField(blank=True)
    minimo = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.nombre} | Categoría: {self.categoria} | Código: {self.codigo} | Precio Costo: {str(self.precio_costo)} | Precio Venta: {str(self.precio_venta)} | Inventario: {self.inventario}'

class Ticket(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField(null=True)
    cerrada = models.BooleanField(default=False)
    detalle = models.JSONField(default=dict)
    total = models.IntegerField(default=0)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    correo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    rut = models.CharField(max_length=20)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    correo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    rut = models.CharField(max_length=20)
    saldo = models.IntegerField(default=0)
    limite_credito = models.IntegerField(default=0)
    descuento_pred = models.IntegerField(default=0)
