# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas donde el usario pondra su informacion basica y repondera una serie de preguntas.Los formularios solo se podrann responder una vez y estos estaran registrados por un ID unica asi que el usario solo podra responder una vez, en caso de que se envien datos inccorrectos, la pagina tendra distintos mensajes de error dependiento el fallo que sea encontrado.


Para este proyecto no se requieren grandes infrestructuras ya que solo se requiere tener un servidor capaz de mantener el programa estable y de un personal para poder manternelo y darle mantenimiento, asi como tener uno para estar formlando, modificando y creando los cuestionarios.

Este proyecto forzozamente debe de estar conectada a internet para poder recolectar toda la informacion de los formularios, asi como poder consultar todos los datos que los usarios introduscan.


## PATH

| Path                  | Descripción |
| --------------------- | ----------- |
|`/store`|Esta ruta crea o registra a todos los usarios que hayan ingresado su informacion |
|`/list`|Esta ruta muestra todos los datos que los usarios que se hayan registrado|
|`/<id>`|Esta ruta muestra un id especifico de los usarios|
|`/<id>/encuesta`|Esta ruta crea una nueva encuesta tomando en cuenta la id que tienen los usarios|
|`/<id>/<encuesta>`|Esta ruta muestra las encuestas que han sido creadas|
|`/<id>/<encuesta>`|Esta ruta modifica las encuestas que hayan sido creadas y les agrega las correcciones que el usario administrativo haya modificado|
|`/<id>/<encuesta>/respuesta`|Esta ruta almacena las respuestas dependiendo la encuesta que haya sido selecionada|
|`/<id>/<encuesta>/<respuesta_1>`|Esta ruta busca respuestas especificas de las consultas ya contestadas|


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

Una vez planteada todos los datos de la estructura
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
```
GET /URL-FORULY/encuesta
{tittle:"Encuesta ",
fechaini:"04/07/2021,
fechafin:"05/07/2021",
ID:1
}
```
## Ejemplo de datos de una respuestas de preguntas de opcion multible

## Ejemplo de datos de una respuesta abierta
En esta seccion se da un ejemplo de como se consultario una o las respuestas de una pregunta abierta.
```
localhost:8080/url_messa/4/encuesta
{
respuesta :
 [  Ejemplo de respuesta abierta]
}
```
## Consulta de datos de usario
En esta seccion se van a vizualizar los datos del usario que realizo la encuesta, se vera sus datos principales y tambie la fecha en la que la encuesta inicio y la fecha en la que va a expirar.
```
localhost:8080/url_messa/store
{
 {"username" : "Juan Perez",
 "Fecha de inicio" : "02/07/2021",
 "Edad" :"21",
 "Genero" :"Hombre",
 "Email" :  "estenoesunbait@bait.com"}
}
```

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

# Computo en la nube

## Crear un fork del proyecto storage-api
En esta tabla se creo el fork del proyecto de la carpeta que se nos proporciono para empezar a trabajar

En esta tabla se creo el fork del proyecto de la carpeta que se nos proporciono para empezar a trabajar
En esta tabla se creo el fork del proyecto de la carpeta que se nos proporciono para empezar a trabajar y estructurar el documento y poder tener avances con el diseño del proyecto.

| Path    | Descripción |
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
![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-01-encuesta%20formato.png)
![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-02-estructura%20de%20encuesta.png)
![Imagen de edicion de encuestas](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-03-tabla%20de%20consulta%20y%20edicion%20de%20encuestas.png)



##  Datos de la informacion de usarios y de las encuestas que han contestado
Esta ruta almacena los doatos de todos las encuestas, id, usarios y su inforacion, para luego ser conultada y poder editarla o eliminarla segun lo que se dese hacer.

| Path                  | Descripción |
| --------------------- | ----------- |
| Commit de rutas py | 96e133ce32b0aa6fa709d58506994f429255436a|


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

# Casos de uso

## Curl para agregarlos datos de los usuarios
* El usario agregara su informacion basica para poder quedar registrado
  * Su informacion constara de su nombre, su genero, su edad la fecha y su correo.
`<curl http://localhost:8080/url_messa/store  -X POST -H 'Content-Type: application/json'  -d '{"id" : "4" , "username" : "eduardo" , "genero" : "hombre" , "edad" : "10" , "fecha":"2021-01-01" , "correo" : "estenoesunbait@bait.com"}'>`
## Curl para poder agregar preguntas mediande un id
* Esta seccion se encarga de agreegar las preguntas y el tema de la encuesta
  * Las preguntas tiene un formato abierto al igual queel nombre de la encuesta tambien se le debe de asignar un id
`<curl http://localhost:8080/url_messa/4/encuesta -X POST -H 'Content-Type: application/json' -d '{"encuesta": "comida","id": "4", "pregunta_1": "era bait", "pregunta_2": "no soy una respuesta", "pregunta_3": "respuesta"}'>`

## Curl para poder agregar las respuestas de la encuestas
* En esta seccion se reponderan a las preguntas que se crearon, esto dependiendo el id
  * Esta tomara los datos del nombre de la encuesta y de su id como tambei las pregutas , pero essta vez seran renplasados por las respuestas
`<curl http://localhost:8080/url_messa/4/comida/respuesta -X POST -H 'Content-Type: application/json' -d '{"id": "4", "encuesta": "comida", "respuesta_1": "no era bait", "respuesta_2": " soy una respuesta", "respuesta_3": "respuesta de bait"}'>`

## Curl para poder modificar la informacion de los usarios
* En caso de que se quiera hacer correccioes a las pregunnta de deterinada encuesta
  * Esta podra ser corregida tanto como el id, la encuesta y las preguntas
`<curl http://localhost:8080/url_messa/4/comida -X POST -H 'Content-Type: application/json' -d '{"encuesta": "comida","id": "4", "pregunta_1": "era bait", "pregunta_2": "no soy una respuesta", "pregunta_3": "respuesta"}'>`

## curl para hacer consultas sobre los usarios
* Las consultas se utilizaran para saber los usarios que han contestado y el id de la encuesta
`<curl http://localhost:8080/url_messa/list -X GET>`

## curl para hacer consultas sobre las preguntas
* La consulta para saber cuantas encuestas se tinen y las id de estas mismas
`<curl http://localhost:8080/url_messa/4/comida -X GET>`

## curl para hacer consultas sobre las respuestas
* Tambien consultar todas las repuestas que se tienen de todas las encuestas que se tienen
`<curl http://localhost:8080/url_messa/4/comida/no_era_bait -X GET>`

# Planeacion del frontend

El desarrollo del frontend requiere una 2 caras uno del lado donde se van a consultar o crear las encuestas y otra donde el usario va a reponder a estas encuestas. La base de este forntend se encuentra en la carpeta de ```html``` en donde se encuestran archivos de ```html```, ```javascript``` y ```css``` estos para tener una estructura de la pagina y que esta simule la interaccion entreun usario y el proyecto.

Por el lado donde el usario consultara los datos o creara las encuestas, requerira las siguietes acciones
* Creacion de encuestas
* Consultar las encuestas
* Consultar a los usarios que contestaron las encuestas
* Modificar las encuestas

Finalmente por la parte para contestar las encuestas
* Contestar las encuestas o agregar las respuestas

# Futuros cambios

Para futuras modificaciones en el proyecto seria montar el codigo de python a html y javascript y hacer lo funcionar, asi como crear mmas funciones para poder borar encuestas o respuetas, asi como crear un contro de acceso para los usarios que vayan a ingresar para consultar o crear las esncuestas.
