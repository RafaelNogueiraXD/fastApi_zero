from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_zero.data import *

app = FastAPI()

@app.get("/user/")
def all_Users():
    return usersData

@app.get("/chapa/")
def all_chapas():
    return chapas

@app.get("/eleicao/")
def all_elections():
    return votacoes

@app.get("/eleicao/{eleicao_id}")
async def search_election(eleicao_id):
    for eleicao in votacoes["resposta"]:
        if int(eleicao['id']) == int(eleicao_id):
            return eleicao
    return None

@app.get("/chapa/{chapa_id}")
async def search_chapa(chapa_id):
    for chapa in chapas["resposta"]:
        if int(chapa['id']) == int(chapa_id):
            return chapa
    return None


@app.get("/user/{user_id}")
async def search_User(user_id):
    for user in usersData["resposta"]:
        if int(user['id']) == int(user_id):
            return user
    return None

@app.delete("/eleicao/{eleicao_id}")
async def delete_election(eleicao_id):
    votacoes["resposta"] = [user for user in votacoes["resposta"] if user["id"] != eleicao_id]
    return "eleicao deletada"

@app.delete("/chapa/{chapa_id}")
async def delete_election(chapa_id):
    chapas["resposta"] = [user for user in chapas["resposta"] if user["id"] != chapa_id]
    return  chapas["resposta"] 

@app.delete("/user/{user_id}")
async def delete_user(user_id):
    usersData["resposta"] = [user for user in usersData["resposta"] if user["id"] != user_id]
    return "usuario deletado"


@app.put("/user/{user_id}")
async def update_user(user_id, user_update: UserForm):
    for user in usersData["resposta"]:
        if int(user['id']) == int(user_id):
            user['nome'] = user_update.nome
            user['email'] = user_update.email
            user['senha'] = user_update.senha
            return user
    return None


@app.put("/eleicao/{election_id}")
async def update_election(election_id, election_update: ElectionForm):
    for election in votacoes["resposta"]:
        if int(election['id']) == int(election_id):
            election['nome'] = election_update.nome
            return election
    return None

@app.put("/chapa/{chapa_id}")
async def update_chapa(chapa_id, chapa_update: chapaForm):
    for chapa in chapas["resposta"]:
        if int(chapa['id']) == int(chapa_id):
            chapa['nome'] = chapa_update.nome
            return chapa
    return None
            
@app.post("/user/login")
def login(login: Login):
    for user in usersData["resposta"]:
        if user['email'] == login.email and user['senha'] == login.senha :
            return user
    return None

@app.post("/user/create")
def create_user(cadastra: UserForm):
    for user in usersData["resposta"]:
        if user['email'] == cadastra.email:
            return "email ja cadastrado"
        
    ultimoId = usersData["resposta"][-1]['id']
    ultimoId += 1
    new_user = {
        "id" : ultimoId,
        "nome" : cadastra.nome,
        "email" : cadastra.email,
        "senha" : cadastra.senha
    }    
    usersData['resposta'].append(new_user)
    return "usuario criado com sucesso! "

@app.post("/eleicao/create")
def create_election(eleicao: ElectionForm):
    ultimoId = votacoes["resposta"][-1]['id']
    ultimoId += 1
    new_eleicao = {
        "id" : ultimoId,
        "nome" : eleicao.nome
    }
    votacoes['resposta'].append(new_eleicao)
    return "eleicao criada com sucesso! "

@app.post("/chapa/create")
def create_chapa(chapa: chapaForm):
    ultimoId = chapas["resposta"][-1]['id']
    ultimoId += 1
    new_chapa = {
        "id" : ultimoId,
        "nome" : chapa.nome
    }
    chapas['resposta'].append(new_chapa)
    return "chapa criada com sucesso! "


