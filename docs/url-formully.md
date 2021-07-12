# Formularios

Este es un trabajo que busca poder responder un formulario de pregutas donde el usario pondra su informacion basica y repondera una serie de preguntas.Los formularios solo se podrann responder una vez y estos estaran registrados por un ID unica asi que el usario solo podra responder una vez, en caso de que se envien datos inccorrectos, la pagina tendra distintos mensajes de error dependiento el fallo que sea encontrado.


Para este proyecto no se requieren grandes infrestructuras ya que solo se requiere tener un servidor capaz de mantener el programa estable y de un personal para poder manternelo y darle mantenimiento, asi como tener uno para estar formlando, modificando y creando los cuestionarios.

Este proyecto forzozamente debe de estar conectada a internet para poder recolectar toda la informacion de los formularios, asi como poder consultar todos los datos que los usarios introduscan.


## PATH

| Path                  | Descripción |
| --------------------- | ----------- |
| /url/encuesta.py       |Este archivo se encargara de almacenar toda la informacion ingresada en las casillas, {"username": "UserName","Edad":"edad","Email":"emailexample","genero":"gener","fechaini":"fecha de inicio","fechafin":"fecha de final"|
| /url/respuestas.py         |este archivo alamacenara las respuestas del formulario |
| /url/send.py             |Este archivo ejecutara la validacion de todos los datos que fueron ingresados en el formulario.             |
| /url/id.py         |este archivo tendra el ID de la encuesta |


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

Una vez planteada todos los datos de la estructura

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
```
GET /URL-FORULY/encuesta
{tittle:"Encuesta ",
fechaini:"04/07/2021,
fechafin:"05/07/2021",
ID:1
}
```
## Ejemplo de datos de una respuestas de preguntas de opcion multible
En esta secccion se da un ejemplo de como se consultaria todas las respuestas de la preguntas de opcion multiple.
```
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
```
## Ejemplo de datos de una respuesta abierta
En esta seccion se da un ejemplo de como se consultario una o las respuestas de una pregunta abierta.
```
GET/URL-FORMULY/encuesta/1
{
respuesta :
 [  Ejemplo de respuesta abierta]
}
```
## Consulta de datos de usario
En esta seccion se van a vizualizar los datos del usario que realizo la encuesta, se vera sus datos principales y tambie la fecha en la que la encuesta inicio y la fecha en la que va a expirar.
```
GET/URL-FORMULY/encuesta/1
{
 {"username" : "Juan Perez",
 "Fecha de inicio" : "02/07/2021",
 "Fecha Final" : 05/07/2021",
 "Edad" :"21",
 "Genero" :"Hombre",
 "Email" :  "estenoesunbait@bait.com"}
}
```

# Historial de git
Este es el historial de todos los commit que se hicieron en la archivo desde que se hizo el fork, aqui vienen los datos de quien hizo el commit y la fecha.
```

commit 7906531f1e64fec8a287bb194a3fc85e261eb6aa (HEAD -> master, github/master)
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 8 07:47:52 2021 -0700

    Avance

commit 50c8f2e4a8d8803f2c9eed3239e1ad559398439e
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jul 6 17:25:21 2021 -0700

    estructura

commit 9b7dc8f9c614d4cd831b798a94abd72d2fbc15db
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jul 6 11:06:41 2021 -0700

    Avance

commit 841b4d431be09ef8a02e0bd81ff4578e3412cd52
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jul 6 10:12:50 2021 -0700

    Avance minimo

commit 76304189563bed5ef5a32ee22445e6a30562557e
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 5 17:21:02 2021 -0700

    Avance

commit 1a7198b3d9912ef45f38096a57493a3ec90f64a2
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jul 5 17:11:59 2021 -0700

    Avance

commit 3a23ad42bfb04981bc05dd73d7fbc23cbcd33298
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Sun Jul 4 16:13:42 2021 -0700

    Avence

commit 5c21721df389adfdacabf3bc41455b9e9ba26b14
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Fri Jul 2 09:49:07 2021 -0700

    Avance 3

commit 1804db6051f19207d61cb1d08e416a399564b18f
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Fri Jul 2 08:41:20 2021 -0700

    Avance 2

commit 49c0790cd98d2bf03a6c8d197964b0f9eab15535
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 1 12:17:23 2021 -0700

    Avance de estructuras de error

commit d0788687bf3fc6961db58d0c1ed9649780e611d6
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 1 08:09:32 2021 -0700

    Prueba 3

commit 44346131a05e2ab0d9d51c04f83daf2d36e94999
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 1 08:08:34 2021 -0700

    Avance 2

commit 1d49adc22c3642c4f45c546d6f89c32db43b38fe
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Thu Jul 1 08:05:06 2021 -0700

    Avance todo chido

commit 2aab4385b10fb2ab095a229fa4a4d108d041cea9
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Wed Jun 30 14:55:48 2021 -0700

    Avance de documento 1.1

commit b6cf3677d520428415f8488f51252dbcfcb9c12f
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Wed Jun 30 14:20:21 2021 -0700

    Avance de funcionamiento del trabajo

commit 700c0f09df1a3789e6dc22d56392e4453643f65c
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Wed Jun 30 14:08:43 2021 -0700

    Actualizacion del proyecto

commit 0e404828e43f306c56c6445f71c09db96a8dda78
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 21:06:34 2021 -0700

    Avance 1 de operaciones

commit 70d70f91083316110cedcafd7e6428fd0e050d5d
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:34:08 2021 -0700

    Estructura de la pagina y modo de uso version 10.1

commit 98fe86de73c185ae058d720d3cb083813735077a
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:26:13 2021 -0700

    Avance de pagina 2

commit 6585d1664797ea30051cda514a5adf28bc6cf270
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:24:30 2021 -0700

    Prueba 6

commit fc4071f3395a7f3f44da6c8f28eb1d22d7940068
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:22:29 2021 -0700

    Prueba 5

commit 913c921bc726e5117c08937cf04bc1a34cd91fb4
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 09:15:40 2021 -0700

    Avance de trabajo

commit 8d95a5331f32c2c4e460fd81d1d22e88d7cfce01
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 08:16:26 2021 -0700

    Prueba 5

commit e33ccd3494a1e5af429db589b495f0fcaf99c4be
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 08:15:55 2021 -0700

    Prueba 4

commit a014ff33a6da5b6deb62fa5f02c451b9e725b7eb
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 08:14:45 2021 -0700

    Prueba 3

commit c47465af4dd570a2a5ee942f151af32992aaa958
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 08:07:29 2021 -0700

    Prueba 2

commit 0ee04b7167faf2877fa73777e976045ff7632196
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 08:05:19 2021 -0700

    Avance de la estructura de formulario

commit 60027a29a1c71a6db6e638806dce6ad3c70c664b
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Tue Jun 29 07:57:34 2021 -0700

    Avance

commit 7591dc6d4fef1b7260ba3e6fdd93d05202211a4d
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jun 28 19:32:14 2021 -0700

    Avence del diseño

commit e7d0c197e023eb5eaf74f3f9aa4be8b7ef702241
Author: jorge garcia <jorgearmando1999@hotmail.com>
Date:   Mon Jun 28 18:52:34 2021 -0700

    Prueba de comit

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
![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-01-encuesta%20formato.png)
En esta imagen se muestra la estructura que llevaran las preguntas asi como van a estar configuradas para responder.
![Imagen de formato de encuesta](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-02-estructura%20de%20encuesta.png)
El ingreso de datos del usario sera basicamente igual, ya que este debera de ingresar sus datos basicos y esta encuesta tendra la fecha y el ID de la encuesta pero estos ultimos no seran modificables para el usario.
![Imagen de edicion de encuestas](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-03-tabla%20de%20consulta%20y%20edicion%20de%20encuestas.png)
La parte de consulta de datos tendra la opciones de buscar lass encuestas por fecha que fueron contestadas, asi como la opcion de editar preguntas y respuestas, asi como eliminar las encuestas.
![Imagen de Consulta de usuarios](https://github.com/JorgeNYLV/storage-api/blob/master/docs/assets/slug-03-tabla%20de%20consulta%20y%20edicion%20de%20encuestas.png)
En esta seccion se muestra los usarios que reposndieron una encuesta y esta mostrar las opciones de vizualizar las respuestas que contestaron o eliminar sus respuestas.
