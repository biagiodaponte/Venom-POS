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
$ # Acceder a la aplicación desde el navegador: http://127.0.0.1:8000/
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
   - Listado de Productos
   - Crear Producto
   - Modificar Producto
   - Eliminar Producto
   - En el botón de más opciones en la esquina superior derecha, se podrán generar: Listado de la totalidad de productos ("Exportar a Excel") y un reporte con los productos con su stock en estado "crítico" (cantidad actual por debajo del mínimo) en "Reporte Stock Crítico".

   ### Empleados
   - Listado de Empleados
   - Crear Empleado (Validaciones: Tanto "Usuario" y "R.U.T" serán únicos por cada empleado)
   - Modificar Empleado
   - Eliminar Empleado

   ### Clientes
   - Listado de Clientes
   - Crear Cliente (Validaciones: En caso de ingresar R.U.T, no podrá repetirse en ningún otro cliente.)
   - Modificar Cliente
   - Eliminar Cliente

   ### Ventas
   - Se podrán agregar artículos a la venta actual introduciendo el código del artículo. (Si se desea añadir x cantidad del mismo artículo se podrá utilizar la nomenclatura de "cantidad\*codigo" (*ej. 3\*1515*).
   - Se podrá hacer un FOCUS al campo de introducción del código del artículo, presionando la tecla F2.
   - Se podrá incrementar la cantidad en 1 de cada producto que se encuentre en la venta actual, presionando el botón "*+*" al lado de su cantidad.
   - Está permitido eliminar artículos no deseados en la venta presionando el botón de eliminar en la fila del producto en cuestión.
   - Si se desea vaciar la venta por completo, se podrá realizar en el botón de "*Limpiar Ticket*" y confirmar su acción (deben existir productos en la venta actual).
   - Se incluye, por motivos estrictamente necesarios, el campo de "*Total*" en la parte inferior de la pantalla (deben existir productos en la venta actual).
   -  Para confirmar una venta, sólo se debe clickear el botón de "*Completar Venta*" y luego confirmar. La aplicación, automáticamente lo devolverá a la pantalla de la siguiente venta. Si desea imprimir la venta previamente aceptada, puedes descargar el pdf en el apartado superior derecho "Descargar Última Venta".

   ### Reportes
   - **Reporte Stock Crítico:** Exporta a una planilla Excel, una tabla con todos los productos con su inventario actual bajo su mínimo esperado en tienda.
   - **Reporte Total de Ventas:** Exporta a una planilla Excel, una tabla con el reporte total de las ventas, que incluye por cada ticket emitido, su número, fecha y monto total. (como desarrollo posterior al Máster, se busca implementar filtrar estos resultados mediante un intervalo de fechas.)
<br/>
<br/>

## Límites del Proyecto

   ### Inicio
   - Las gráficas actuales no representan información real de las ventas de la aplicación, es sólo ilustrativo (se desarrollarán éstas al adquirir conocimientos en más tecnologías que Python).

   ### Empleados
   - Una de las metas del proyecto, era poder tomar esta clase Empleado y sus datos, para procesar el log-in a la aplicación. Por falta de conocimiento en las modificaciones de las clases UserLogin de Django, de momento solo se podrá ingresar al sistema con los Usuarios predefinidos de Django como tal.

   ### Clientes 
   - El atributo "saldo" de esta clase, de momento no será utilizadas en la aplicación. Esto debido a que no manejará de momento los métodos de pago en la venta. Una vez se implemente el método de pago "A Crédito" y el método de "Abono a Cliente", es cuando se manejará el saldo del cliente.

   ### Ventas
   - Debido al bajo conocimiento de javascript, no se podrá implementar de momento el apartado de "Cliente Asociado a esta Venta". Ya que se logrará mediante una busqueda en tiempo real por nombre, apellido o R.U.T (DNI) en un respectivo Card.

<br/>
<br/>

---

- Utilizando **Argon Dashboard** (Free Version) de **Creative-Tim** y **AppSeed**
- UI-Ready app, SQLite Database, Django Native ORM
- Modular design, clean code-base
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx

<br />