from controller import get_response, get_response_list
import socket
import json

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

tcp.send(b'Connect')

print('Opções Disponíveis:')

menu = '1 - Listar Filmes\n2 - Buscar Filme\n3 - Adicionar Filme\n4 - Atualizar Filme\n5 - Deletar Filme\n0 - Encerrar'

print(menu)
code_msg = input('>>').lower()
while code_msg != '0':
    if code_msg == '1':
        req = {
            "method": 'list'
        }

        req = json.dumps(req)
        tcp.send(req.encode())

        response = json.loads(tcp.recv(1024).decode())

        get_response_list(response)

    elif code_msg == '2':
        print('Digite o ID do filme')
        movie_id = int(input('>>'))
        req = {
            "method": 'find',
            "data": {
                "id": movie_id
            }
        }

        req = json.dumps(req)
        tcp.send(req.encode())

        response = json.loads(tcp.recv(1024).decode())

        get_response(response)

    elif code_msg == '3':
        print('Adicione as informações do filme')
        name = input('Nome: ')
        year = int(input('Ano: '))
        genre = input('Genero: ')

        req = {
            "method": 'add',
            "data": {
                "nome": name,
                "ano_lancamento": year,
                "genero": genre
            }
        }

        req = json.dumps(req)
        tcp.send(req.encode())

        response = json.loads(tcp.recv(1024).decode())
        get_response(response)

    elif code_msg == '4':
        print('Adicione as informações do filme')
        movie_id = int(input('ID: '))
        name = input('Nome: ')
        year = int(input('Ano: '))
        genre = input('Genero: ')

        req = {
            "method": 'update',
            "data": {
                "id": movie_id,
                "nome": name,
                "ano_lancamento": year,
                "genero": genre
            }
        }

        req = json.dumps(req)
        tcp.send(req.encode())

        response = json.loads(tcp.recv(1024).decode())
        get_response(response)

    elif code_msg == '5':
        print('Digite o ID do filme')
        movie_id = int(input('>>'))
        req = {
            "method": 'delete',
            "data": {
                "id": movie_id
            }
        }

        req = json.dumps(req)
        tcp.send(req.encode())

        response = json.loads(tcp.recv(1024).decode())

        get_response(response)

    print(menu)
    code_msg = input('>>')

tcp.send(b'f')

tcp.close()
