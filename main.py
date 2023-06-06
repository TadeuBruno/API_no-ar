from distutils.log import debug

from random import triangular

from tkinter.messagebox import RETRY

from fastapi import FastAPI

from numpy import True_

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from tinydb import TinyDB, Query

db = TinyDB('banco.json')

app = FastAPI()

origins = [

'*'

]

app.add_middleware(

CORSMiddleware,

allow_origins=origins,

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"],

)

class Treinador(BaseModel):

    name: str

    elemento: str

@app.get('/ver_treinadores')

async def ver_treinadores():

    return db.search(Query().status == True)

@app.get('/ver_treinadores/{id_treinador}')

async def pegar_id(id_treinador:int):

    return db.search(Query().id == id_treinador and Query().status == True)

@app.post('/criar_treinador')

async def criar_trainador(treinado: Treinador):

    db.insert({'id': len(db), 'name': treinado.name, 'elemento': treinado.elemento, 'status': True})

    return 'Success'

@app.put('/soft_delete_treinador')

async def deletar(id_treinador:int):

    db.update({"status": False}, Query().id == id_treinador)

    return 'Success'

@app.put('/alterar_treinador')

async def alterar(id_treinador: int, tipo: str, novo_valor):
        db.update({tipo: novo_valor}, Query().id == id_treinador)
        return db.search(Query().id == id_treinador)

