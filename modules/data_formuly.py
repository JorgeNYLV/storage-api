import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


def add_user(id = None, username = None, genero = None, edad = None,  fecha = None, correo = None):

    print("Datos de usario")
    print(id, username, genero, edad, fecha, correo)
    print("Capturdo")


    almacenable = {
        "id": id,
        "username": username,
        "genero": genero,
        "edad": edad,
        "fecha": fecha,
        "correo": correo,
    }
    nombre_de_archivo = f"{username}-{id}-{genero}-{edad}-{fecha}-{correo}.json"
    datos = store_string(
        "user/users",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_user_list(users=None):
    query_result = query_storage(
        "user/users",
    )
    if users is None:
        return query_result["content"]

def get_id_details(id=None):
    query_result = query_storage(
        "user/users",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("done")

def add_encuesta(encuesta = None, id = None, pregunta_1 = None, pregunta_2 = None, pregunta_3 = None):
    print("Datos encuesta")
    print(encuesta, id, pregunta_1, pregunta_2, pregunta_3)
    print("Exito")

    almacenable = {
        "encuesta": encuesta,
        "id": id,
        "pregunta_1": pregunta_1,
        "pregunta_2": pregunta_2,
        "pregunta_3": pregunta_3,
    }
    nombre_de_archivo = f"{encuesta}-{id}-{pregunta_1}-{pregunta_2}-{pregunta_3}.json"
    datos = store_string(
        "enuesta/encuestas",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_encuesta(id = None, encuesta = None):
    query_result = query_storage(
        "enuesta/encuestas",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
        print("Le sabes")
    if encuesta is not None:
        return [
           r
           for r in query_result["content"]
           if encuesta in r
        ]
        print("Le sabes")


def add_repuestas(encuesta = None, id = None, respuesta_1 = None, respuesta_2 = None, respuesta_3 = None):
    print("Datos encuesta")
    print(encuesta, id, respuesta_1, respuesta_2, respuesta_3)
    print("Exito")

    almacenable = {
        "encuesta": encuesta,
        "id": id,
        "respuesta_1": respuesta_1,
        "respuesta_2": respuesta_2,
        "respuesta_3": respuesta_3,
    }
    nombre_de_archivo = f"{encuesta}-{id}-{respuesta_1}-{respuesta_2}-{respuesta_3}.json"
    datos = store_string(
        "enuesta/respuestas",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_answers(id = None, encuesta = None, respuesta_1 = None):
    query_result = query_storage(
        "enuesta/respuestas",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("Funciona 'hace un dab'")

def update_encuestas(encuesta = None, id = None, pregunta_1 = None, pregunta_2 = None, pregunta_3 = None):
    print("Datos encuesta")
    print(encuesta, id, pregunta_1, pregunta_2, pregunta_3)
    print("Exito")

    almacenable = {
        "encuesta": encuesta,
        "id": id,
        "pregunta_1": pregunta_1,
        "pregunta_2": pregunta_2,
        "pregunta_3": pregunta_3,
    }
    nombre_de_archivo = f"{encuesta}-{id}-{pregunta_1}-{pregunta_2}-{pregunta_3}.json"
    datos = store_string(
        "enuesta/encuestas",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos
