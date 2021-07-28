import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


def add_user(id = None, username = None, edad = None, genero = None, fecha = None, correo = None):

    print("Datos de usario")
    print(id, username, edad, genero, fecha, correo)
    print("Capturdo")


    almacenable = {
        "id": id,
        "username": username,
        "edad": edad,
        "genero": genero,
        "fecha": fecha,
        "correo": correo,
    }
    nombre_de_archivo = f"{username}-{id}.json"
    datos = store_string(
        "url/user",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos
