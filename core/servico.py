import json


def registro_internet(operadora, down, up, valor):
    registro = {'operadora': operadora, 'download': down, 'upload': up, 'valor': valor}
    registro = json.dumps(registro)
    try:
        with open('registro.json', 'w') as file:
            file.write(registro)
    except:
        print('Não foi possivel salvar')


def abrir_registro():
    with open('registro.json', 'r') as file:
        registro = json.loads(file.readline())
        return registro

