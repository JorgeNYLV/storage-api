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
