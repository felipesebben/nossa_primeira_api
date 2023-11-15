from fastapi import FastAPI
from typing import List, Dict, Any


app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo"}

produtos: List[Dict[str, Any]] = [{
    "id": 1,
    "nome": "Iphone14",
    "descricao": "Celular da Apple",
    "preco": 5000.00
},
{
    "id": 2,
    "nome": "PS5",
    "descricao": "Videogame da Sony",
    "preco": 2000.00
},
{
    "id": 3,
    "nome": "Workshop - do Jupyter pro Deploy",
    "descricao": "Workshop de implementação de projetos",
    "preco": 120.00
},
]

id_atual = 3

def lista(self):
    return self.produtos


def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
    self.id_atual += 1
    item["id"] = self.id_atual
    return self.produtos.append(item)

@app.get("/produtos")
def listar_produtos():
    """
    View que retorna o dicionário de produtos.
    """
    return produtos