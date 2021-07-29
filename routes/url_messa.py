import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.data_formuly import (
    add_user,
    get_user_list
)


app = BottleJson()

#prueba de post
#curl http://localhost:8080/url_messa/store  -X POST -H 'Content-Type: application/json'  -d '{"id" : "4" , "username" : "eduardo" , "genero" : "hombre" , "edad" : "10" , "fecha":"2021-01-01" , "correo" : "estenoesunbait@bait.com"}'

@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        username = str(payload['username'])
        genero = str(payload['genero'])
        edad = str(payload['edad'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        correo = str(payload['correo'])
        print("Datos Aceptados")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos incorrecros")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)


#Optiene todos los datos introducidos
# curl http://localhost:8080/url_messa/list -X GET
@app.get("/list")
def get_all_info(*args, **kwargs):
    try:
       respuesta = get_user_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
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
