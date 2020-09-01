import json
import os

try:
    os.mkdir(os.path.dirname(__file__) + '/status')
except:
    pass
pasta = os.path.dirname(__file__) + '/status'


def gravar_json(status, path):
    with open(f'{pasta}/{path}.json', 'w') as file:
        internet = status
        internet = json.dumps(internet)
        file.write(internet)


def ler_json(path):
    with open(f'{pasta}/{path}.json', 'r') as file:
        internet = file.read()
        status = json.loads(internet)
        return status
gravar_json({'status':'True'}, 'status')
ler_json('status')
