# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas para registrar datos de usario y  enviarlos a un correo.

## PATH

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/post.json        |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Empresa":"empresaname","Email":"emailexample","Datos":"datos"|
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
> Datos adicionales


`send` `deleate`
# Operacion de almacenamiento de datos

## Operaciones del usuario
### Relleno de formulario
* Solicita su nombre, correo electronico, nombre de la empresa y datos adicioneles.
* Cada usario tendra una id autoincrementable

# Operaciones de consulta
* Poder consultar todos los usario y los datos

# Operaciones de administrador
* Consultar, editar y eliminar usarios
* Poder odificar la direccion hacia donde se envian los correos

#Consulta de datos
* Por ID
* Por orden alfabetico
* Por fecha de registro

#Estructuras de solicitud y respuesta
<!-- Blockquote -->
> {"ID" : 1,
"username" : "Juan Perez",
"Empresa" :"Malvados y asociados",
"Email" :  "estenoesunbait@bait.com",
"datos" : "Es bait"}

<!-- Blockquote -->
> {"solicitud" : "Registro Existoso"}

<!-- Blockquote -->
> {"code : "500",
"message": "El servidor esta sufriendo amsiedad"
![Image of Yaktocat](https://latinversionistas.com/wp-content/uploads/elementor/thumbs/cheems-no-puede-ser-en-la-academia-latinoamericana-de-inversionistas-p3w4067e630uqw60m0c1fmzr1qn4w6x0b4bcod5kso.png)}
