from flask import Flask , request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from functions import *

server = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='Prova Backend')
spec.register(server)

class maxsum(BaseModel):
    lista: list[int]=[]

class respo(BaseModel):
    sum:int 
    positions: list[int]=[]

@server.post('/maxsum')
@spec.validate(body=Request(maxsum), resp=Response(HTTP_200=respo))
def post_list():
    body = request.context.body.dict()
    return respo(
            sum = max_sum(body),
            positions = position(body)).dict()

server.run()