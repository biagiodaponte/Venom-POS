# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import GeneratePdf

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    #% EMPLEADOS --->
    path('empleados/', views.empleados, name='empleados'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('eliminar_empleado/<id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('editar_empleado/<id>/', views.editar_empleado, name='editar_empleado'),

    #% PRODUCTOS -->
    path('productos/', views.productos, name='productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('eliminar_producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<id>/', views.editar_producto, name='editar_producto'),

    #% CLIENTES -->
    path('clientes/', views.clientes, name='clientes'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('eliminar_cliente/<id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<id>/', views.editar_cliente, name='editar_cliente'),

    #% VENTAS -->
    path('ventas/<id>/', views.ventas, name='ventas'),
    path('completar_venta/<id>/', views.completar_venta, name='completar_venta'),
    path('vaciar_venta/<id>/', views.vaciar_venta, name='vaciar_venta'),
    path('eliminar_detalle/<ticket>/<id>/', views.eliminar_detalle, name='eliminar_detalle'),
    path('suma_cantidad/<ticket>/<id>/', views.suma_cantidad, name='suma_cantidad'),

    
    #% REPORTE -->
    path('reportes/', views.reportes, name='reportes'),
    path('reportes/stock_critico/', views.reporte_stock_critico, name='reporte_stock_critico'),
    path('reportes/stock_total/', views.reporte_stock_total, name='reporte_stock_total'),
    path('reportes/total_ventas/', views.reporte_total_ventas, name='reporte_total_ventas'),
    
    path('venta_pdf/<id>/', GeneratePdf.as_view(), name='venta_pdf'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
