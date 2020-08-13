import json
import os

try:
    os.mkdir(os.path.dirname(__file__) + '/status')
except:
    pass
pasta = os.path.dirname(__file__) + '/status'


def tem_internet(status):
    with open(f'{pasta}/status.json', 'w') as file:
        internet = {'status': status}
        internet = json.dumps(internet)
        file.write(internet)


def ler_tem_internet():
    with open(f'{pasta}/status.json', 'r') as file:
        internet = file.read()
        status = json.loads(internet)
        return status
