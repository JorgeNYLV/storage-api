# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas y enviarlas a un correo.

## API

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/post.json        |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Empresa":"empresaname","Email":"emailexample","Mensaje":"Mensajex","si":"sies","no":"noes"} En el caso de las opciones de `si` y `no` estas ejecutaran acciones que seran ejeutas con un `if` y un `else`  |
| /url/send.py             |Este archivo ejecutara la validacion de todos los datos que fueron ingresados en el formulario.             |
| /url/deleate.py         |Este archivo borrara todos lo escrito en el formulario              |


A continuacion se tiene un ejemplo del diseño del programa


## Formulario
<!-- Blockquote -->
> Ingrese Su nombre
<!-- Blockquote -->
> Ingrese el nombre de su empresa
<!-- Blockquote -->
> Ejemplodecorreo@ejemplo.com

```bash
Es usted un proveedor o esta interesado trabajar con nosotros
* [x] Si
* [x] No
```
En caso de que la respuesta sea `si` desplegara otras casillas y si es `no` hara nada
<!-- Blockquote -->
> Productos que manejan
<!-- Blockquote -->
> Operaciones que requieren

`send` `deleate`
# operacion de almacenamiento de datos

## Operaciones del usuario
### Relleno de fotrmulario 
