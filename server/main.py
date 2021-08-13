import socket

from database.db import *
from controller import *

with db_session:
    if Filme.select().first() is None:
        populate_database()

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

while True:
    con, client = tcp.accept()
    print('Conectado com ', con)

    init = con.recv(1024)

    products = []
    while True:
        msg = con.recv(1024)
        if not msg:
            break

        if msg.decode() == 'f':
            break

        req = json.loads(msg.decode())

        method = req['method']

        if method == 'list':
            movies = json.loads(all_movies())

            cod, msg_response = get_response_code(10)
            if not movies:
                cod, msg_response = get_response_code(30)

            response = {
                "cod": cod,
                "msg": msg_response,
                "data": movies
            }
            response = json.dumps(response)
            con.send(response.encode())

        elif method == 'find':
            data = req['data']
            movie = json.loads(detail_movies(data['id']))

            cod, msg_response = get_response_code(10)
            if not movie:
                cod, msg_response = get_response_code(30)

            response = {
                "cod": cod,
                "msg": msg_response,
                "data": movie
            }

            response = json.dumps(response)
            con.send(response.encode())

        elif method == 'add':
            data = req['data']
            movie = add_movies(
                data['nome'], data['ano_lancamento'], data['genero'])

            cod, msg_response = get_response_code(10)
            if not movie:
                cod, msg_response = get_response_code(20)

            response = {
                "cod": cod,
                "msg": msg_response
            }

            response = json.dumps(response)
            con.send(response.encode())

        elif method == 'update':
            data = req['data']
            movie = update_movie(
                data['id'], data['nome'], data['ano_lancamento'], data['genero'])

            cod, msg_response = get_response_code(10)
            if not movie:
                cod, msg_response = get_response_code(30)

            response = {
                "cod": cod,
                "msg": msg_response
            }

            response = json.dumps(response)
            con.send(response.encode())

        elif method == 'delete':
            data = req['data']
            movie = json.loads(remove_movie(data['id']))

            cod, msg_response = get_response_code(10)
            if not movie:
                cod, msg_response = get_response_code(30)

            response = {
                "cod": cod,
                "msg": msg_response
            }

            response = json.dumps(response)
            con.send(response.encode())

    break

print('Finalisando conexão com ', client)
con.close()
