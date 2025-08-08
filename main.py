from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
      
      id: int
      titulo: str
      descricao: str
      concluida: bool

class CriarTarefa(BaseModel):
      titulo: str
      descricao: str
      concluida: bool

banco_de_dados_tarefas = [
      
    Tarefa(id = 1, titulo= "Treinar a mira", descricao="Puxar DMs ate ficar em primeiro 2x seguidas", concluida=False),
    Tarefa(id = 2, titulo= "Bater laje", descricao="Ja que voce nao eh bom no valorant, vai subir muro", concluida=True),

]


@app.get("/")
def ler_raiz():
      return{"mensagem":"Bem vindo a minha api de tarefas"}

@app.get("/tarefas")
def listar_tarefas():
      return banco_de_dados_tarefas

@app.post("/tarefas")
def criar_tarefas(tarefa_a_criar: CriarTarefa):
      if banco_de_dados_tarefas: 
        ultimo_id = banco_de_dados_tarefas[-1].id
        novo_id = ultimo_id + 1
      else: 
        novo_id = 1

      nova_tarefa = Tarefa(id=novo_id, **tarefa_a_criar.model_dump())
      banco_de_dados_tarefas.append(nova_tarefa)
      return {"status": "sucesso", "mensagem": "Tarefa criada!", "tarefa_adicionada":  nova_tarefa}


@app.delete("/tarefas")
def deletar_tarefas(id_tarefa: int):
     tarefa_a_deletar = None
     for tarefa in banco_de_dados_tarefas:
          if  tarefa.id == id_tarefa:
               tarefa_a_deletar = tarefa
               break
          
     if tarefa_a_deletar is None:
         raise HTTPException(status_code=404, detail="Tarefa não encontrada")
     
     banco_de_dados_tarefas.remove(tarefa_a_deletar)
     return {"status": "sucesso", "mensagem": "Tarefa deletada!"}

@app.put("/tarefas/{id_da_tarefa}")
def atualizar_tarefa(id_da_tarefa: int, tarefa_dados_novos: CriarTarefa):
   
    for i, tarefa_atual in enumerate(banco_de_dados_tarefas):
        if tarefa_atual.id == id_da_tarefa:
            tarefa_atualizada = Tarefa(id=id_da_tarefa, **tarefa_dados_novos.model_dump())
            banco_de_dados_tarefas[i] = tarefa_atualizada
            return {"status": "sucesso", "mensagem": "Tarefa atualizada!"}
    
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")