import json
from database.db import *


def get_response_code(code):
    codes = {
        10: 'sucess',
        20: 'error in request',
        30: 'response error',
        40: 'method not found',
    }

    return code, codes[code]


@db_session
def all_movies():
    result = select(f for f in Filme)[:]

    movies = []
    for m in result:
        movie = {
            "id": m.id,
            "nome": m.nome,
            "ano_lancamento": m.ano_lancamento,
            "genero": m.genero
        }

        movies.append(movie)

    response = json.dumps(movies)

    return response


@db_session
def detail_movies(id):
    try:
        result = Filme.get(id=id)

        movie = {
            "id": result.id,
            "nome": result.nome,
            "ano_lancamento": result.ano_lancamento,
            "genero": result.genero
        }

        return json.dumps(movie)
    except:
        return json.dumps({})


@db_session
def add_movies(nome, ano, genero):
    movie = Filme(nome=nome, ano_lancamento=ano, genero=genero)

    response = {
        'msg': 'Filme adicionado'
    }

    response = json.dumps(response)

    return response


@db_session
def update_movie(id, nome, ano, genero):
    try:
        result = Filme.get(id=id)

        if nome != '':
            result.nome = nome
        if ano != None:
            result.ano = ano
        if genero != '':
            result.genero = genero

        response = {
            'msg': 'Filme Atualizado',
        }

        response = json.dumps(response)

    except:
        response = {
            'msg': 'Filme não encontrado'
        }
        response = json.dumps(response)

    return response


@db_session
def remove_movie(id):
    try:
        result = Filme.get(id=id)
        result.delete()

        response = {
            'msg': 'Filme deletado'
        }
    except:
        response = {
            'msg': 'Filme nao encontrado'
        }

    response = json.dumps(response)

    return response
