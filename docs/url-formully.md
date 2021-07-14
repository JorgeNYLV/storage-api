# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas donde el usario pondra su informacion basica y repondera una serie de preguntas.Los formularios solo se podrann responder una vez y estos estaran registrados por un ID unica asi que el usario solo podra responder una vez, en caso de que se envien datos inccorrectos, la pagina tendra distintos mensajes de error dependiento el fallo que sea encontrado.


Para este proyecto no se requieren grandes infrestructuras ya que solo se requiere tener un servidor capaz de mantener el programa estable y de un personal para poder manternelo y darle mantenimiento, asi como tener uno para estar formlando, modificando y creando los cuestionarios.

Este proyecto forzozamente debe de estar conectada a internet para poder recolectar toda la informacion de los formularios, asi como poder consultar todos los datos que los usarios introduscan.


## PATH

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/encuesta.py       |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Edad":"edad","Email":"emailexample","genero":"gener","fechaini":"fecha de inicio","fechafin":"fecha de final"|
| /url/Consulta.py         |este archivo alamacenara las respuestas del formulario |
| /url/encuesta/user.py             |Este archivo ejecutara guarf¿dara los datos del usario que realizo la encuesta.             |
| /url/encuesta/id.py         |este archivo tendra el ID de la encuesta |


Al ser un formulario se eben de tener un acceso a la inforacion de los formularios que sean contestados, ya que es necesario saber que datos y quien esta contestando dichos formularios.

## Operacion de almacenamiento de datos

## Consulta de datos

## Relleno de formulario
* Solicitar su nombre
* correo electronico
* genero
* edad


## Operaciones de consulta
* Poder consultar todos los usarios
* cuestonarios realizados.

## Operaciones de administrador
* Consultar y eliminar usarios o formularios.
* Poder modificar la direccion hacia donde se envian los correos.

## Consulta de datos
* Por ID
* Por orden alfabetico
* Por fecha de registro

## creacion de encuestas
* Numero de preguntas
* Fecha de inicio y final

## Consulta de respuestas
* Numero de preguntas
* Preguntas correctas
* Pregutas incorrectas
* Preguntas Abiertas
* Preguntas Cerradas

Una vez planteada todos los datos de la estructura, se crearan la estructura en codigo mostrando ejeplos de consulta de informacion de posibles consultas.

## Estructuras de solicitud y respuesta

<!-- Blockquote -->
> {"ID" : 1,
"username" : "Juan Perez",
"Fecha de inicio" : "02/07/2021",
"Edad" :"21",
"Genero" :"Hombre",
"Email" :  "estenoesunbait@bait.com"
}
## Ejemplo de pregunta abierta
<!-- Blockquote -->
> {"Prgunta " : "¿Que es esto?",
"Respuesta" :"Un ejemplo",
"}

## Ejemplo de estructura de pregunta de opcion multiple
<!-- Blockquote -->
> {"Prgunta " : "¿Cual es la opcion correcta?",
"Respuesta" :"A",
"Respuesta" :"B",
"Respuesta" :"C",
"Respuesta" :"D"
Answer : [2]
"}
## Mensaje de encuesta enviada
<!-- Blockquote -->
> {"solicitud" : "Encuesta enviada exitosamente"}

## Mensaje de error con la pagina
<!-- Blockquote -->
> {"code : "500",
"message": "El servidor esta sufriendo problemas",

## Mensaje de error con encuestas no encontradas
<!-- Blockquote -->
> {"code : "404",
"message": "Pagina no encontrada",

## Mensaje de error con solicitud erronea
<!-- Blockquote -->
> {"code : "400",
"message": "Solicitud Incorrecta",


Una vez que se tengan las consultas y los mensajes de la pagina se deberan  implentar las estructuras de las rutas del proyecto

## Implementación de rutas para los recursos
## Ejemplo de consulta de formularios.
En esta seccion se da un ejemplo de como se consutaria el tipo de encuesta con su nombre, fecha y el ID.

GET /URL-FORULY/encuesta
- Muestra las encuestas que tiene el sistema
- muesta la informacion recientemente enviada
-  Regresa un mensaje de fallo si no se encuentran encuestas
## Ejemplo de datos de una respuestas de preguntas de opcion multible
En esta secccion se da un ejemplo de como se consultaria todas las respuestas de la preguntas de opcion multiple.

GET/URL-FORMULY/encuesta/1
- Muestra las repuestas de un usuario en el caso de preguntas de opcion multiple  
- Regresa un error en caso de que no se encuentren respuestas


## Consulta de datos de usario
En esta seccion se van a vizualizar los datos del usario que realizo la encuesta, se vera sus datos principales y tambie la fecha en la que la encuesta inicio y la fecha en la que va a expirar.

GET/URL-FORMULY/encuesta/User
- Muestra los datos del usuario y la encuesta que realizo, asi como el id de su encuesta
- Regresa un mensaje de error en caso de no encontrar al usario o id especifico

GET/URL-FORMULY/encuesta/delete
- Muestra unmensaje de que una encuesta a sido borrada o tambien de que las respuestas de un usario fueron borradas
- Regresa un error en caso de no encontrar una encuesta o usario

# Historial de git
Este es el historial de todos los commit que se hicieron en la archivo desde que se hizo el fork, aqui vienen los datos de quien hizo el commit y la fecha.
```

commit 78c4025c5051ceaac5cb011f438e74ae638ef229
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 12 14:47:43 2021 -0700

    Modificacion de descripiones

commit 233a275afab174dc60b8d3c45730ced1b7f6a004
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 12 14:43:51 2021 -0700

    Agregacion de documento de consulta con datos

commit d1fcb71b4ed43e7ff3e40d39d19febe88010a5dc
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 12 14:41:39 2021 -0700

    Correcion de mensajes de error

commit a92515de5483707db2223d85a47bdd802f5f10e4
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 12 13:40:10 2021 -0700

    Modificacion de descripciones en algunas tablas.

commit ea56b20be9480c44517424537114eb0be7c7997e
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 12 09:00:00 2021 -0700

    Correccion de descripciones de las imagenes


commit 49c0790cd98d2bf03a6c8d197964b0f9eab15535
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 1 12:17:23 2021 -0700

    Avance de estructuras de error


commit b6cf3677d520428415f8488f51252dbcfcb9c12f
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Wed Jun 30 14:20:21 2021 -0700

    Avance de funcionamiento del trabajo


commit 70d70f91083316110cedcafd7e6428fd0e050d5d
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:34:08 2021 -0700

    Estructura de la pagina y modo de uso version 10.1


commit 3acb89e18b91d49fc26516e725ce178b270fe08e
Merge: 66b9c7e 812228b
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jun 24 19:52:46 2021 -0700

    Merge branch 'master' of github.com:JorgeNYLV/storage-api

commit 66b9c7e438394b736470eeba8e4359adc93eebd1
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jun 24 19:44:23 2021 -0700

    Se agrego un archivo de documentacion para proyecto url-formully
```
# Computo en la nube

## Crear un fork del proyecto storage-api
En esta tabla se creo el fork del proyecto de la carpeta que se nos proporciono para empezar a trabajar
| Path                  | Descripción |
| --------------------- | ----------- |
| archivo original  | 8c9c250a11ab0ac5c2b83ceb07cc5ec8dc1560f7           |
| Crear fork y agregar md      |66b9c7e438394b736470eeba8e4359adc93eebd1  |


##  Crear todas las rutas especificadas en su archivo de documentación
En esta tabla se creon las rutas de las estructuras de los formatos de py
| Path                  | Descripción |
| --------------------- | ----------- |
| Commit de rutas py | 70d70f91083316110cedcafd7e6428fd0e050d5d|

## Crear mock ups, de las vistas que desean implementar, utilizando MoqUps
Aqui se creo una nueva carpeta en la ruta  ```/docs/assets``` en donde esta muestran la estructura que se desea que tenga la pagina, al ser imagenes de dmostracion se agregaron pocos datos en el caso de las preguntas.

![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-02-estructura%20de%20encuesta.png)

- El ingreso de datos del usario sera basicamente igual, ya que este debera de ingresar sus datos basicos y esta encuesta tendra la fecha y el ID de la encuesta pero estos ultimos no seran modificables para el usario.

![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-01-encuesta%20formato.png)

- En esta imagen se muestra la estructura que llevaran las preguntas asi como van a estar configuradas para responder.

![Imagen de edicion de encuestas](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-03-tabla%20de%20consulta%20y%20edicion%20de%20encuestas.png)

- La parte de consulta de datos tendra la opciones de buscar lass encuestas por fecha que fueron contestadas, asi como la opcion de editar preguntas y respuestas, asi como eliminar las encuestas.
- La parte de edicion mostrara las preguntas como se ve en la primera imagen nonmas que esta podra borrar o agregar tecto.

![Imagen de Consulta de usuarios](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-04-tabla%20de%20consulta%20de%20usarios%20que%20contestaron%20una%20encuesta.png)

- En esta seccion se muestra los usarios que reposndieron una encuesta y esta mostrar las opciones de vizualizar las respuestas que contestaron o eliminar sus respuestas.

Una vez ya planteada la idea del diseño ya se empezara con la parte de progrmar cada una de las estrructura como se propuso en las imagenes previamente mostradas.
