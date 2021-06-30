# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas para registrar datos de usario y  enviarlos a un correo.

## API

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/post.json        |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Empresa":"empresaname","Email":"emailexample","Mensaje":"Mensajex"|
| /url/send.py             |Este archivo ejecutara la validacion de todos los datos que fueron ingresados en el formulario.             |
| /url/deleate.py         |Este archivo borrara todos lo escrito en el formulario              |
| /url/user.py         |este archivo alamacenara la informacion registrada en el |

A continuacion se tiene un ejemplo del diseño del programa


## Formulario
<!-- Blockquote -->
> Ingrese Su nombre
<!-- Blockquote -->
> Ingrese el nombre de su empresa
<!-- Blockquote -->
> Ejemplodecorreo@ejemplo.com
<!-- Blockquote -->
> datos adicionales


`send` `deleate`
# operacion de almacenamiento de datos

## Operaciones del usuario
### Relleno de formulario
* Solicita su nombre, correo electronico,nombre de la empresa y datos adicioneles.
* Cada usario tendra una id autoincrementable

#Operaciones de consulta
* Poder consultar todos los usario y los datos

#operaciones de administrador
* Consultar, editar y eliminar usarios
* poder odificar la direccion hacia donde se envian los correos

#Consulta de datos
* por id
* por orden alfabetico
* por fecha de registro
