from json import dumps as json_dumps
import bottle
from modules.bottles import BottleJson
import json
from time import time
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

import bottle
from modules.bottles import BottleJson
from modules.data_formuly import add_usuario

#app = BottleJson()
app = BottleJson()
@app.get("/")
def index():
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501, 'Error')

#@app.get("/encuesta/<tipo_id>")
#def get_tipo(tipo_id):
    #print(tipo_id)
    #raise bottle.HTTPError(501, 'Error')

    #bottle.response.status = 404
    #bottle.response.content_type = "application/json"
    #return dict(code= 404, message = "Bad Request ")

@app.get("/add_usuario/add")
def bar(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
     try:

        username = str(payload['username'])
        genero = str(payload['genero'])
        edad = str(payload['edad'])
        fecha = str(payload['fecha'])
        year, month, date = [int(x) for x in release_date.split("-")]
        correo = str(payload['correo'])
        ID = str(payload['ID'])
        print("Datos Aceptados")
        respuesta = add_usuario(**payload)
        raise bottle.HTTPError(201)
    except:
        print("Datos incorrecros")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)


@app.get("/consulta/<nombre_us>")
def get_all_info(nombre_us):
    print(nombre_us)
    raise bottle.HTTPError(501, 'Error')
    #bottle.response.status = 500
    #bottle.response.content_type = "application/json"
    #return dict(code = 500, message = "Not implemented")

@app.get("/historial/<tipos_id>")
def get_info_by_sn(tipos_id):
    print(tipos_id)
    raise bottle.HTTPError(501, 'Error')
    #bottle.response.status = 400
    #bottle.response.content_type = "application/json"
    #return dict(code = 400, message = "Not found")
@app.get("/User/<names_id>")
def get_User(names_id):
    print(names_id)
    raise bottle.HTTPError(501, 'Error')
    #bottle.response.status = 501
    #bottle.response.content_type = "application/json"
    #return dict(code = 501, message = "Not implemented")

@app.get("/ID/tipo/<encuestas_id>")
def get_ID(encuestas_id):
    print(encuestas_id)
    raise bottle.HTTPError(501, 'Error')
    #bottle.response.status = 501
    #bottle.response.content_type = "application/json"
    #return dict(code = 501, message = "Not implemented")

@app.get("/Delete/user/<tipo_id>")
def get_delete(tipo_id):
    print(tipo_id)
    raise bottle.HTTPError(501, 'Error')
    #bottle.response.status = 501
    #bottle.response.content_type = "application/json"
    #return dict(code = 501, message = "Not implemented")
