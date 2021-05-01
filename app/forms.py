# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from .models import Producto, Empleado, Categoria, Cliente
from django import forms
from django.contrib import messages

class EmpleadoCreateForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=False)
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'rut', 'usuario', 'clave']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Empleado.objects.filter(rut=rut).exists():
            raise forms.ValidationError(f'El RUT "{rut}" ya pertenece a otro empleado.')
        return rut
    
    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if Empleado.objects.filter(usuario=usuario).exists():
            raise forms.ValidationError(f'El usuario "{usuario}" ya pertenece a otro empleado.')
        return usuario

class EmpleadoEditForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=False)
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'rut', 'usuario', 'clave']

    def clean_rut(self):
        rut1 = self.initial.get('rut')
        rut2 = self.cleaned_data.get('rut')
        if rut1 == rut2:
            pass
        elif Empleado.objects.filter(rut=rut2).exists():
            raise forms.ValidationError(f'El RUT "{rut2}" ya pertenece a otro empleado.')
        return rut2
    
    def clean_usuario(self):
        usuario1 = self.initial.get('usuario')
        usuario2 = self.cleaned_data.get('usuario')
        if usuario1 == usuario2:
            pass
        elif Empleado.objects.filter(usuario=usuario2).exists():
            raise forms.ValidationError(f'El usuario "{usuario2}" ya pertenece a otro empleado.')
        return usuario2



class ProductCreateForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre*'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código*'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label="Selecciona una categoría...")
    precio_costo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Costo*'}))
    precio_venta = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Venta*'}))
    inventario = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Inventario*'}))
    minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mínimo*'}))

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'categoria', 'precio_costo', 'precio_venta', 'inventario', 'minimo']

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo').upper()
        if Producto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("El código ya existe.")
        return codigo

class ProductEditForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre*'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código*'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label="Selecciona una categoría...")
    precio_costo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Costo*', 'min':'0'}))
    precio_venta = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Venta*', 'min':'0'}))
    inventario = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Inventario*'}))
    minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mínimo*', 'min':'0'}))

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'categoria', 'precio_costo', 'precio_venta', 'inventario', 'minimo']

    def clean_codigo(self):
        codigo1 = self.initial.get('codigo').upper()
        codigo2 = self.cleaned_data.get('codigo').upper()
        if codigo1 == codigo2:
            pass
        elif Producto.objects.filter(codigo=codigo2).exists():
            raise forms.ValidationError("El código ya está registrado en otro producto.")
        return codigo2



class ClienteCreateForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=False)
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    saldo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0)
    limite_credito = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0)
    descuento_pred = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0, max_value=100)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'rut', 'direccion', 'saldo', 'limite_credito', 'descuento_pred']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if rut:
            if Cliente.objects.filter(rut=rut):
                raise forms.ValidationError("Ya existe un cliente con este RUT.")
            else:
                pass
        return rut

class ClienteEditForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=False)
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    saldo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0)
    limite_credito = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0)
    descuento_pred = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), initial=0, min_value=0, max_value=100)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'rut', 'direccion', 'saldo', 'limite_credito', 'descuento_pred']

    def clean_rut(self):
        rut = self.initial.get('rut')
        rut2 = self.cleaned_data.get('rut')
        if rut == rut2:
            pass
        elif not rut2:
            pass
        else:
            if Cliente.objects.filter(rut=rut2):
                raise forms.ValidationError("Ya existe un cliente con este RUT.")
            else:
                pass
        return rut2