# VenomPOS

 ![version](https://img.shields.io/badge/version-1.0.0-blue.svg)
<br />
## Antes de empezar

> Descomprimir los archivos o clonar el repositorio. Luego de obtener el código, abrir un terminal y navegar hasta la raíz del proyecto.
> Deberás ejecutar las siguientes líneas de código para que el proyecto funcione correctamente.

```bash

$ # Instalar los módulos requeridos para el correcto funcionammiento del proyecto.
$ pip3 install -r requirements.txt
$
$ # Arrancar el proyecto (modo desarrollador)
$ python manage.py runserver # default port 8000
$
$ # Arrancar el proyecto - Puerto personalizado
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
$ # o en su defecto con puerto predeterminado.
```

> Nota: Para utilizar la app existen 2 tipos de login (administrador y vendedor) y se podrán acceder con las credenciales indicadas.

<br />

## Credenciales de VenomPOS
>Para acceder a VenomPOS en forma de **Administrador**:
>- Usuario: **admin**
>- Clave: **admin**
>
>Para acceder a VenomPOS en forma de **Vendedor**:
>- Usuario: **vendedor**
>- Clave: **vendedor**

<br />


## Módulos de VenomPOS
   ### Productos
   ---
   - #### Listado de Productos
   - #### Crear Producto
   - #### Modificar Producto
   - #### Eliminar Producto
   - #### En el botón de más opciones en la esquina superior derecha, se podrán generar: Listado de la totalidad de productos ("Exportar a Excel") y un reporte con los productos con su stock en estado "crítico" (cantidad actual por debajo del mínimo) en "Reporte Stock Crítico".
<br />
   ### Empleados
   ---
   - #### Listado de Empleados
   - #### Crear Empleado
   - #### Modificar Empleado
   - #### Eliminar Empleado

   ### Clientes
   ---
   - #### Listado de Cliente
   - #### Crear Cliente
   - #### Modificar Cliente
   - #### Eliminar Cliente

   ### Ventas
   ---
   - ### Se podrán agregar artículos a la venta actual introduciendo el código del artículo. (Si se desea añadir x cantidad del mismo artículo se podrá utilizar la nomenclatura de "cantidad*codigo" (ej. 3*1515).
   - ### Se podrá incrementar la cantidad en 1 de cada producto que se encuentre en la venta actual, presionando el botón "+" al lado de su cantidad.
   - ### Está permitido eliminar artículos no deseados en la venta presionando el botón de eliminar en la fila del producto en cuestión.
   - ### Si se desea vaciar la venta por completo, se podrá realizar en el botón de "Limpiar Ticket" y confirmar su acción (deben existir productos en la venta actual).
   - ### Se incluye, por motivos estrictamente necesarios, el campo de "Total" en la parte inferior de la pantalla (deben existir productos en la venta actual).
   - ### Para confirmar una venta, sólo se debe clickear el botón de "Completar Venta" y luego confirmar. La aplicación, automáticamente lo devolverá a la pantalla de la siguiente venta. Si desea imprimir la venta previamente aceptada, puedes descargar el pdf en el apartado superior derecho "Descargar Última Venta".



---
[Argon Dashboard - Django Template](https://www.creative-tim.com/product/argon-dashboard-django) - Provided by [Creative Tim](https://www.creative-tim.com/) and [AppSeed](https://appseed.us)
<br />
> Free product - **Django Dashboard** starter project - Features:

- UI Kit: **Argon Dashboard** (Free Version) por **[Creative-Tim]**
- UI-Ready app, SQLite Database, Django Native ORM
- Modular design, clean code-base
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx

<br />