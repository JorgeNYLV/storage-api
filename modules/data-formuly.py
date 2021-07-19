from bottle import response, request
import datetime
import binascii
from os import environ
from pathlib import Path
import datetime as dt

encuestas[]
def get_encuesta_usuario(username,edad,genero,fecha,correo,id):
    encuestas = {
    """
    Funcion para estructura de consulta de datos de un usario.
    - username es el nombre del usario en una cadena de texto.
    - Genero es el genero que el usario tiene, este es una cadena de texto.
    - Fecha es una cadena de texto que represente la fecha.
    -  Correo es una cadena de texto que representa el correo que registro el usario.
    - El ID es un dato sitring que signifia el id que se le dio al usario al reaslizar la encuesta.
    - Edad es un dato string que que significa la edad que el usario tiene
    En caso de que no se encuentre un usario, la estructura mostrara un mensaje dicendo 'Usuario no encontrado'

    Esta funcion llevar un diccionario con 5 datos 'username','genero','fecha','correo','ID'

>>> get_encuesta_usuario(Juan Perez,Hombre,21,02/07/2021,estenoesunbait@bait.com,1)
    > {"ID" : 1,
    "username" : "Juan Perez",
    "Fecha" : "02/07/2021",
    "Edad" :"21",
    "Genero" :"Hombre",
    "Email" :  "estenoesunbait@bait.com"
    }


    Exception: Usuario no encontrado
    """
    "username" : username,
    "genero" : genero,
    "fecha" :fecha ,
    "edad": edad,
    "correo" : correo,
    "ID" : id,
    }
encuestas.append(encuestas)
return json.dumps(encuestas)


def get_encuesta_fecha(encuesta,fecha){
try:
    date = dt.datetime.fromisoformat(fecha)
except:
    raise Exception("Fecha invalida.")
return {
    "date": date.isoformat(),
    "encuesta": encuesta
}
