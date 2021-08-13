import json


def get_response_list(response):
    cod = response["cod"] if "cod" in response else None
    msg = response["msg"] if "msg" in response else None
    data = response["data"] if "data" in response else None

    print('-='*10)
    print("Resposta do protocolo")
    print("Código:", cod)
    print("Menssagem:", msg)
    if (type(data) is list):
        print("Response:")
        print('{} - {}'.format('ID', 'Nome'))
        for movie in data:
            print('{} - {}'.format(movie['id'], movie['nome']))
    print('-='*10)


def get_response(response):
    cod = response["cod"] if "cod" in response else None
    msg = response["msg"] if "msg" in response else None
    data = response["data"] if "data" in response else None

    print('-='*10)
    print("Resposta do protocolo")
    print("Código:", cod)
    print("Menssagem:", msg)
    if (type(data) is dict):
        print("Response:")
        for key in data:
            print(f'{key} - {data[key]}')
    print('-='*10)
