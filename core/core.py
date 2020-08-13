import requests
from datetime import datetime


class Requisicao:
    def __init__(self, url='https://www.bing.com/'):
        self.url = url

    def status(self):
        codes = False
        try:
            codes = requests.get(self.url, timeout=5).ok
        except:
            codes = False
        data = self._data_hora()['data']
        return {'status':codes,'data':data}

    @staticmethod
    def _data_hora() -> dict():
        """
        Converte a data e hora para o formato brasileiro
        :return: data e hora
        """
        agora = datetime.now()
        tempo = agora.strftime('%d/%m/%Y,%H:%M:%S')
        data = datetime.strptime(tempo, '%d/%m/%Y,%H:%M:%S')
        return {'data':data}

