from django.views.generic import ListView
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
from UliPlot.XLSX import auto_adjust_xlsx_column_width
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template import loader
from django.contrib import messages
from django import template
from .models import Ticket, Empleado, Cliente, Categoria
from .forms import *
import io
from django.http import HttpResponse, FileResponse
from django.views.generic import View
from .utils import render_to_pdf

class GeneratePdf(View):
    def get(self, request, id):
        ticket = Ticket.objects.get(numero=id)
        detalle = ticket.detalle

        total_format = str(ticket.total)
        if len(total_format) > 6:
            total_format = total_format[:-6]+'.'+total_format[-6:-3]+'.'+total_format[-3::]      
        elif len(total_format) > 3:
            total_format = total_format[:-3]+'.'+total_format[-3::]

        data = {
            'ticket_id':id,
            'detalle':detalle,
            'ticket':ticket,
            'total':total_format
        }
        pdf = render_to_pdf('invoice.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Ticket_%s.pdf" %(str(id))
            content = "attachment; filename= %s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

@login_required(login_url="/login/")
def index(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    empleados = Empleado.objects.count()
    productos = Producto.objects.count()
    clientes = Cliente.objects.count()
    ventas = Ticket.objects.count()-1
    ultima_venta = Ticket.objects.last().numero
    context = {
        'empleados':empleados,
        'productos':productos,
        'clientes':clientes,
        'ventas':ventas,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

#% INICIO EMPLEADOS ----------------------------
@login_required(login_url="/login/")
def empleados(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    empleados = Empleado.objects.all()
    ultima_venta = Ticket.objects.last().numero

    contexto = {
        'empleados':empleados,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'empleados.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')

@login_required(login_url="/login/")
def crear_empleado(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    if request.method == 'POST':
        form = EmpleadoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado creado correctamente.")
            return redirect(to="empleados")
    else:
        form = EmpleadoCreateForm()

    contexto = {
        'form':form,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'crear_empleado.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


@login_required(login_url="/login/")
def eliminar_empleado(request, id):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    obj_empleado = Empleado.objects.get(id=id)
    obj_empleado.delete()
    messages.success(request, "Empleado eliminado exitosamente.")

    contexto = {
        'usuario':usuario,
        'permiso':permiso
        }
    return redirect(to='empleados')


@login_required(login_url="/login/")
def editar_empleado(request, id):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    emple = get_object_or_404(Empleado, id=id)
    form = EmpleadoEditForm(request.POST or None, instance=emple)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado modificado exitosamente.')
            return redirect(to='empleados')

    contexto = {
        'form':form,
        'emple':emple,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'editar_empleado.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')

#% FIN EMPLEADOS -------------------------------



#% INICIO PRODUCTOS ----------------------------

@login_required(login_url="/login/")
def productos(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    productos = Producto.objects.all()
    ultima_venta = Ticket.objects.last().numero

    contexto = {
        'productos':productos,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'productos.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


@login_required(login_url="/login/")
def crear_producto(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    form = ProductCreateForm(request.POST or None)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect(to="productos")
    else:
        form = ProductCreateForm()
    contexto = {
        'form':form,
        'categorias':categorias,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'crear_producto.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


@login_required(login_url="/login/")
def eliminar_producto(request, id):
    obj_producto = Producto.objects.get(id=id)
    obj_producto.delete()
    messages.success(request, "Producto eliminado exitosamente.")
    return redirect(to='productos')


@login_required(login_url="/login/")
def editar_producto(request, id):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    prod = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    form = ProductEditForm(request.POST or None, instance=prod)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto modificado exitosamente.')
            return redirect(to='productos')

    contexto = {
        'form':form,
        'prod':prod,
        'categorias':categorias,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'editar_producto.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')
#% FIN PRODUCTOS -------------------------------



#% INICIO CLIENTES -----------------------------
@login_required(login_url="/login/")
def clientes(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    clientes = Cliente.objects.all()
    ultima_venta = Ticket.objects.last().numero

    contexto = {
        'clientes':clientes,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'clientes.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


@login_required(login_url="/login/")
def crear_cliente(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    if request.method == 'POST':
        form = ClienteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado exitosamente.")
            return redirect(to="clientes")
        else:
            print('malo')
    else:
        form = ClienteCreateForm()
    contexto = {
        'form':form,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'crear_cliente.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


@login_required(login_url="/login/")
def eliminar_cliente(request, id):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    obj_cliente = Cliente.objects.get(id=id)
    obj_cliente.delete()
    messages.success(request, "Cliente eliminado exitosamente.")
    return redirect(to='clientes')


@login_required(login_url="/login/")
def editar_cliente(request, id):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteEditForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente modificado exitosamente.')
            return redirect(to='clientes')

    contexto = {
        'form':form,
        'cliente':cliente,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
    }
    if permiso == True:
        return render(request, 'editar_cliente.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')
#% FIN CLIENTES --------------------------------


#% INICIO VENTAS -------------------------------
@login_required(login_url="/login/")
def ventas(request, id):
    #% PERMISOS:
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero
    last_ticket = Ticket.objects.last().numero-1

    ticket = Ticket.objects.get(numero=id)
    if request.method == 'POST':
        codigo = request.POST.get('code')
        if str(codigo).find('*') != -1:
            dividido = codigo.split('*')
            code = dividido[1]
            cantidad = int(dividido[0])
        else:
            code = codigo
            cantidad = 1
        try:
            obj = Producto.objects.get(codigo=code)
        except:
            messages.error(request, "El código no existe.")
        else:
            if code in ticket.detalle.keys():
                ticket.total += cantidad*ticket.detalle[code]["precio"]
                ticket.detalle[code]["cantidad"] += cantidad
                ticket.detalle[code]["total"] = ticket.detalle[code]["cantidad"]*ticket.detalle[code]["precio"]

            else:
                ticket.detalle[code] = {'codigo':obj.codigo, 'nombre':obj.nombre.upper(), 'cantidad':cantidad, 'precio':obj.precio_venta}
                ticket.detalle[code]["total"] = ticket.detalle[code]["cantidad"]*ticket.detalle[code]["precio"]
                ticket.total += ticket.detalle[code]["precio"]*cantidad
            ticket.save()

    total_format = str(ticket.total)
    if len(total_format) > 6:
        total_format = total_format[:-6]+'.'+total_format[-6:-3]+'.'+total_format[-3::]      
    elif len(total_format) > 3:
        total_format = total_format[:-3]+'.'+total_format[-3::]

    context = {
        'ticket':ticket,
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta,
        'total':total_format,
        'last_ticket':last_ticket
    }
    if ticket.cerrada  == True:
        messages.error(request, f"La venta Nº{ticket.numero} ya está cerrada.")
        return redirect(to='home')
    else:
        return render(request, 'ventas.html', context)


def completar_venta(request, id):
    ticket = Ticket.objects.get(numero=id)

    for codigo, dic in ticket.detalle.items():
        producto = Producto.objects.get(codigo=codigo)
        producto.inventario -= dic["cantidad"]
        producto.save()
    ticket.cerrada = True
    ticket.fecha = datetime.now()
    ticket.save()
    Ticket.objects.create(numero=ticket.numero+1, fecha=datetime.now(), detalle={})
    ultima_venta = Ticket.objects.last().numero
    messages.success(request, "Venta realizada con éxito.")

    return redirect('ventas', id=ultima_venta)


def vaciar_venta(request, id):
    ticket = Ticket.objects.get(numero=id)
    ticket.detalle = {}
    ticket.total = 0
    ticket.save()

    return redirect('ventas', id=ticket.numero)


def eliminar_detalle(request, ticket, id):
    ticket = Ticket.objects.get(numero=ticket)
    ticket.total -= ticket.detalle[id]["cantidad"]*ticket.detalle[id]["precio"]
    ticket.detalle.pop(id)
    ticket.save()

    return redirect('ventas', id=ticket.numero)


def suma_cantidad(request, ticket, id):
    ticket = Ticket.objects.get(numero=ticket)
    ticket.total += ticket.detalle[id]["precio"]
    ticket.detalle[id]["cantidad"] += 1
    ticket.save()

    return redirect('ventas', id=ticket.numero)

#% FIN VENTAS ----------------------------------



#% REPORTES ------------------------------------
@login_required(login_url="/login/")
def reportes(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    ultima_venta = Ticket.objects.last().numero

    contexto = {
        'usuario':usuario,
        'permiso':permiso,
        'ultima_venta':ultima_venta
        }

    if permiso == True:
        return render(request, 'reportes.html', contexto)
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


def reporte_stock_critico(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    productos = Producto.objects.all()

    cods, prods, invs, mins = [[], [], [], []]
    for prod in productos:
        if prod.inventario <= prod.minimo:
            cods.append(prod.codigo)
            prods.append(prod.nombre)
            invs.append(prod.inventario)
            mins.append(prod.minimo)

    df = pd.DataFrame({
        'Código': cods,
        'Nombre': prods,
        'Inventario Actual': invs,
        'Mínimo': mins
    })
    df = df[['Código', 'Nombre', 'Inventario Actual', 'Mínimo']]
    writer = ExcelWriter('stock_critico.xlsx')
    df.to_excel(writer, 'Hoja1', index=False)
    writer.save()

    filename = 'stock_critico.xlsx'
    archivo = FileResponse(open(filename, 'rb'))
    if permiso == True:
        return archivo
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


def reporte_stock_total(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    productos = Producto.objects.all()

    cods, prods, precio_costo, precio_venta, invs, mins = [[], [], [], [], [], []]
    for prod in productos:
        cods.append(prod.codigo)
        prods.append(prod.nombre)
        precio_costo.append(prod.precio_costo)
        precio_venta.append(prod.precio_venta)
        invs.append(prod.inventario)
        mins.append(prod.minimo)

    df = pd.DataFrame({
        'Código': cods,
        'Nombre': prods,
        'Precio Costo': precio_costo,
        'Precio Venta': precio_venta,
        'Inventario Actual': invs,
        'Mínimo': mins
    })
    df = df[['Código', 'Nombre', 'Precio Costo', 'Precio Venta', 'Inventario Actual', 'Mínimo']]
    writer = ExcelWriter('stock_total.xlsx', engine='xlsxwriter')
    df.to_excel(writer, 'Hoja1', index=False)
    workbook  = writer.book
    worksheet = writer.sheets['Hoja1']
    worksheet.set_column('B:B', 40)
    worksheet.set_column('A:A', 11)
    worksheet.set_column('C:D', 12)
    worksheet.set_column('E:E', 16)
    writer.save()

    filename = 'stock_total.xlsx'
    archivo = FileResponse(open(filename, 'rb'))
    if permiso == True:
        return archivo
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')


def reporte_total_ventas(request):
    usuario = User.objects.get(username=request.user)
    permiso = usuario.is_staff
    tickets = Ticket.objects.all().exclude(numero=Ticket.objects.last().numero)

    numeros, fechas, montos = [], [], []
    for ticket in tickets:
        numeros.append(ticket.numero)
        fechas.append(ticket.fecha.date())
        montos.append(ticket.total)
        
    df = pd.DataFrame({
        'Nº Ticket': numeros,
        'Fecha': fechas,
        'Monto Venta': montos,
    })
    df = df[['Nº Ticket', 'Fecha', 'Monto Venta']]
    writer = ExcelWriter('total_ventas.xlsx', engine='xlsxwriter')
    df.to_excel(writer, 'Hoja1', index=False)
    workbook  = writer.book
    worksheet = writer.sheets['Hoja1']
    worksheet.set_column('A:A', 11)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 12)
    writer.save()

    filename = 'total_ventas.xlsx'
    archivo = FileResponse(open(filename, 'rb'))
    if permiso == True:
        return archivo
    else:
        messages.error(request, 'No tienes permitido acceder a esta página')
        return redirect(to='/')

#% FIN REPORTES --------------------------------