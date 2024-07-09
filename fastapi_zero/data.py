from pydantic import BaseModel
usersData = {"resposta" : [
        {
            "id" : 1,
            "nome": "Rafael",
            "email": "rafael@unipampa.com",
            "senha": "123"
        }, 
        {
            "id" : 2,
            "nome": "thiago",
            "email": "thiago@unipampa.com",
            "senha": "123"
        }, 
        {
            "id" : 3,
            "nome": "bernardo",
            "email": "bernardo@unipampa.com",
            "senha": "123"
        }, 
    ]
}
eleitor = {
    "resposta": [
        {
            "id":1,
            "nome":1,
            "chapaPertencente":0
        }
    ]
}
chapas = {"resposta" : [
        {
            "id" : 1,
            "nome": "chapa dasso"
        },
        {
            "id" : 2,
            "nome": "chapa py"
        }
    ]
}
votacoes = {
    "resposta" : [
        {
            "id" : 1,
            "nome" : "votacao de 2022"
        },
        {
            "id" : 2,
            "nome" : "votacao de 2026"
        }
    ]
}

class Login(BaseModel):
    email: str
    senha: str
class ElectionForm(BaseModel):
    nome: str
class chapaForm(BaseModel):
    nome: str
class UserForm(BaseModel):
    nome: str
    email: str
    senha: str