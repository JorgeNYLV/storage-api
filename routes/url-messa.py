from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle

app = bottle.Bottle()

@app.post("/encuesta")
def get_encues(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Not implemented ")

@app.get("/encuesta<User>")
def get_encuesta_User(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/encuesta<ID>")
def get_encuesta_ID(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/encuesta<Delete>")
def get_encuesta_delete(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")
