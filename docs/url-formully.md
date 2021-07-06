# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas donde el usario pondra su informacion basica y repondera una serie de preguntas.

## PATH

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/encuesta.py       |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Edad":"edad","Email":"emailexample","genero":"gener","fechaini":"fecha de inicio","fechafin":"fecha de final"|
| /url/respuestas.py         |este archivo alamacenara las respuestas del formulario |
| /url/send.py             |Este archivo ejecutara la validacion de todos los datos que fueron ingresados en el formulario.             |
| /url/id.py         |este archivo tendra el ID de la encuesta |

A continuacion se tiene un ejemplo del diseño del programa


# Operacion de almacenamiento de datos

## Operaciones del usuario
### Relleno de formulario
* Solicita su nombre, correo electronico,genero, edad.

# Operaciones de consulta
* Poder consultar todos los usarios y cuestonarios

# Operaciones de administrador
* Consultar y eliminar usarios o formularios
* Poder modificar la direccion hacia donde se envian los correos

#Consulta de datos
* Por ID
* Por orden alfabetico
* Por fecha de registro

#creacion de encuestas
* Numero de preguntas
* Fecha de inicio y final

#Estructuras de solicitud y respuesta



<!-- Blockquote -->
> {"ID" : 1,
"username" : "Juan Perez",
"Fecha de inicio" : "02/07/2021",
"Edad" :"21",
"Genero" :"Hombre",
"Email" :  "estenoesunbait@bait.com"
}
<!-- Blockquote -->
> {"Prgunta " : "¿Que es esto?",
"Respuesta" :"Un ejemplo",
"}


<!-- Blockquote -->
> {"Prgunta " : "¿Cual es la opcion correcta?",
"Respuesta" :"A",
"Respuesta" :"B",
"Respuesta" :"C",
"Respuesta" :"D"
Answer : [2]
"}
# Mensaje de encuesta enviada
<!-- Blockquote -->
> {"solicitud" : "Encuesta enviada exitosamente"}

# Mensaje de error con la pagina
<!-- Blockquote -->
> {"code : "500",
"message": "El servidor esta sufriendo amsiedad",
![Cheems](https://github.com/JorgeNYLV/storage-api/blob/master/cheems.png)}

# Mensaje de error con encuestas no encontradas
<!-- Blockquote -->
> {"code : "404",
"message": "Pagina no encomtrada",
![Cheems](https://github.com/JorgeNYLV/storage-api/blob/master/cheems.png)}

# Mensaje de error con solicitud erronea
<!-- Blockquote -->
> {"code : "400",
"message": "Solicitud Incorrecta",
![Cheems](https://github.com/JorgeNYLV/storage-api/blob/master/cheems.png)}

# Implementación de rutas para los recursos
POST /URL-FORULY/encuesta
{tittle:"Encuesta ",
fechaini:"04/07/2021,
fechafin:"05/07/2021",
ID:1
}

GET/URL-FORMULY/encuesta/1
{
respuestas :
 [0,
 1,
 3,
 0,
 2,
 1]
}
