from requests import get
from datetime import datetime
from speed import perda


class Requisicao:
    def __init__(self, url='https://www.bing.com/'):
        self.url = url

    def status(self):
        codes = False
        try:
            codes = get(self.url).ok
        except:
            loss = perda()
            if loss.isdigit():
                print('sem conexão')
        data = self._data_hora()['data']
        hora = self._data_hora()['hora']
        return {'status':codes,'data':data, 'hora':hora}

    def _data_hora(self) -> tuple:
        """
        Converte a data e hora para o formato brasileiro
        :return: data e hora
        """
        agora = datetime.now()
        tempo = agora.strftime('%m/%d/%Y,%H:%M:%S').split(',')
        data = tempo[0]
        hora = tempo[1]
        return {'data':data, 'hora':hora}


if __name__ == '__main__':
    requisicao = Requisicao()
    a = requisicao.status()
    print(a)
