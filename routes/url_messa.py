import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.data_formuly import (
    add_user,
    get_user_list,
    get_id_details,
    add_encuesta,
    get_encuesta,
    add_repuestas,
    get_answers,
    update_encuestas
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

@app.get("/<id>")
def get_id(*args,id=None, **kwargs):
    try:
        respuesta = get_id_details(id = id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
    #bottle.response.status = 400
    #bottle.response.content_type = "application/json"
    #return dict(code = 400, message = "Not found").


#Añade encuestas
# curl http://localhost:8080/url_messa/4/encuesta -X POST -H 'Content-Type: application/json' -d '{"encuesta": "comida","id": "4", "pregunta_1": "era bait", "pregunta_2": "no soy una respuesta", "pregunta_3": "respuesta"}'
@app.post("/<id>/encuesta")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        encuesta = str(payload['encuesta'])
        pregunta_1= str(payload['pregunta_1'])
        pregunta_2 = str(payload['pregunta_2'])
        pregunta_3 = str(payload['pregunta_3'])
        print("Datos validos")
        respuesta = add_encuesta(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, "Creaste una nueva encuesta")

#Consulta las encuestas
#curl http://localhost:8080/url_messa/4/comida -X GET
@app.get("/<id>/<encuesta>")
def get_encuestas(*args, id=None, encuesta=None, **kwargs):
    try:
       respuesta = get_encuesta(id,encuesta)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

# Variable para modificar los las preguntas de las encuestas
# curl http://localhost:8080/url_messa/4/comida -X POST -H 'Content-Type: application/json' -d '{"encuesta": "comida","id": "4", "pregunta_1": "era bait", "pregunta_2": "no soy una respuesta", "pregunta_3": "respuesta"}'

@app.post("/<id>/<encuesta>")
def update_datos(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        encuesta = str(payload['encuesta'])
        pregunta_1= str(payload['pregunta_1'])
        pregunta_2 = str(payload['pregunta_2'])
        pregunta_3 = str(payload['pregunta_3'])
        print("Datos validos")
        respuesta = update_encuestas(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, "La base de datos a sido actualizada")

# Agrega las respuestas a la encuesta
# curl http://localhost:8080/url_messa/4/comida/respuesta -X POST -H 'Content-Type: application/json' -d '{"id": "4", "encuesta": "comida", "respuesta_1": "no era bait", "respuesta_2": " soy una respuesta", "respuesta_3": "respuesta de bait"}'
@app.post("/<id>/<encuesta>/respuesta")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        encuesta = str(payload['encuesta'])
        respuesta_1= str(payload['respuesta_1'])
        respuesta_2 = str(payload['respuesta_2'])
        respuesta_3 = str(payload['respuesta_3'])
        print("Datos validos")
        respuesta = add_repuestas(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, "Agregaste las respuestas :D")


#Consulta de encuestas y las respuestas
#curl http://localhost:8080/url_messa/4/comida/no_era_bait -X GET
@app.get("/<id>/<encuesta>/<respuesta_1>")
def get_specific_answer(*args, id=None,  encuesta=None, respuesta_1=None, **kwargs):
    try:
       respuesta = get_answers(id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
