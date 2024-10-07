# 🍉 API Express API

Essa API RESTful de um aplicativo de entrega chamado **Food Express**, foi desenvolvido em linguagem Python e FastAPI.

Com o objetivo de colocar em prática os conhecimento adquiridos em Python orientado a objetos.

## 🚀 Tecnologias utilizadas
<div align="left">
    <a href="https://skillicons.dev">
        <img src="https://skillicons.dev/icons?i=python,fastapi"/>
    </a>
</div>

## 🛠️ Como executar?
Para executar esse projeto é necessário seguir o passo a passo a seguir:

1. Criar o ambiente virtual do Python.

Na pasta raíz do repositório local, execute o comando:
```
python -m venv <nome do ambiente virtual>
```

2. Ativar o ambiente virutal
```
.\venv\Scripts\activate
```

3. Instalar as dependências do **requirements.txt**.
```
pip install -r requirements.txt
```

4. Executar o script abaixo no **SQL Server Management** para criação do banco de dados e tabela.
```
CREATE DATABASE Food_Express

CREATE TABLE Restaurante (
  RestauranteID INT IDENTITY(1,1) PRIMARY KEY,
  NomeRestaurante NVARCHAR(100) NOT NULL,
  Categoria NVARCHAR(50) NOT NULL,
  Status NVARCHAR(20) NOT NULL
)
```

5. Executar o comando a seguir para iniciar a aplicação:
```
uvicorn app:app --reload
```

## 📝 Testes

Essa API é documentada com **Swagger** e para testá-la você poderá utilizar o mesmo para testar os endpoints.

Para acessá-la utilize o comando a seguir:
```
<local_host>/doc
```

## 📁 Documentações de referência
[Documentação FastAPI](https://fastapi.tiangolo.com/)
