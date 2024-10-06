from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from schemas import (SchemaRestaurante, SchemaRestauranteAvaliar, SchemaRestauranteAlternarStatus, SchemaRestauranteDeletar)
from modelos.restaurante_inserir import RestauranteInserir
from modelos.restaurante_exibir import RestauranteExibir
from modelos.restaurante_alternar_status import RestauranteAlternarStatus
from modelos.restaurante_avaliar import RestauranteAvaliar
from modelos.restaurante_deletar import RestauranteDeletar
from modelos.response import responses

app = FastAPI(
    title="API Food Express",
    description="Esse projeto consiste em um CRUD utilizando FastAPI com o banco de dados SQL Server.",
    version="1.0.0"
)

@app.post('/restaurante/cadastro', responses=responses)
def cadastrar_restaurante(schema: SchemaRestaurante):
    '''
    Endpoint para cadastrar um restaurante.

    Inputs: JSON com o nome e a categoria do restaurante. 
    
    Outputs: JSON com a mensagem de sucesso do cadastro.
    '''
    try:
        restaurante = RestauranteInserir(nome=schema.nome.title(), categoria=schema.categoria.title())
        inserir = restaurante.executar()
        if inserir['sucesso']:
            return {'mensagem': inserir['mensagem']}
        else:
            raise HTTPException(status_code=400, detail=inserir['mensagem'])
    except Exception as excecao:
        raise HTTPException(status_code=500, detail=str(excecao))
    
@app.get('/')
def redirect_to_restaurantes():
    return RedirectResponse(url='/restaurante')

@app.get('/restaurante', responses=responses)
def exibir_restaurantes():
    '''
    Endpoint para exibir um objeto com todos os restaurantes cadastrados.

    Output: JSON que possue o id, nome, categoria, status e avaliacao dos restaurantes.
    
    Obs:
    status 0 desativado | status 1 ativado
    '''
    try:
        exibir = RestauranteExibir()
        listar = exibir.executar()
        if listar:
            return listar
        else:
            return {"mensagem": "Nenhum restaurante encontrado."}
    except Exception as excecao:
        raise HTTPException(status_code=500, detail=str(excecao))
    
@app.put('/restaurante/alternar_status', responses=responses)
def alternar_status_restaurante(schema: SchemaRestauranteAlternarStatus):
    '''
    Endpoint para atualizar o estado de um restaurante.

    Inputs: JSON com o id do restaurante. 
    
    Outputs: JSON com a mensagem de sucesso da atualização.
    '''
    try:
        restaurante = RestauranteAlternarStatus()
        atualizar = restaurante.executar(id=schema.id)
        if atualizar:
            return atualizar
        else:
            return {"mensagem": "Nenhum restaurante encontrado."}
    except Exception as excecao:
        raise HTTPException(status_code=500, detail=str(excecao))
    
@app.put('/restaurante/avaliar', responses=responses)
def avaliar_restaurante(schema: SchemaRestauranteAvaliar):
    '''
    Endpoint para avaliar um restaurante.

    Inputs: JSON com o id do restaurante. 
    
    Outputs: JSON com a mensagem de sucesso da atualização.
    '''
    try:
        restaurante = RestauranteAvaliar()
        atualizar = restaurante.executar(id=schema.id, nota=schema.nota)
        if atualizar:
            return atualizar
        else:
            return {"mensagem": "Nenhum restaurante encontrado."}
    except Exception as excecao:
        raise HTTPException(status_code=500, detail=str(excecao))
    
@app.delete('/restaurante/deletar', responses=responses)
def deletar_restaurante(schema: SchemaRestauranteDeletar):
    '''
    Endpoint para excluir um restaurante.

    Inputs: JSON com o id do restaurante. 
    
    Outputs: JSON com a mensagem de sucesso da exclusão.
    '''
    try:
        restaurante = RestauranteDeletar()
        deletar = restaurante.executar(id=schema.id)
        if deletar:
            return deletar
        else:
            return {"mensagem": "Nenhum restaurante encontrado."}
    except Exception as excecao:
        raise HTTPException(status_code=500, detail=str(excecao))