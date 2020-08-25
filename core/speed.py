from datetime import datetime
import subprocess
from speedtest import Speedtest
import re


def perda(servidor='8.8.8.8'):
    servidor = servidor.replace(':8080', '')
    try:
        process = subprocess.run(['ping', '8.8.8.8', '-n','10'], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout
        padrao = r'(\w+%)'
        resultado = re.search(padrao, output)
        return resultado[0].replace('%', '')
    except:
        return 'None'


def velocidade():
    """
    Realizar um teste na velocidade de download, upload e ping
    :return: uma tupla com velocidade de download, upload e ping
    """
    atualizado = datetime.now()
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    servidor = s.get_best_server()['host']
    s.download()
    s.upload()
    res = s.results.dict()
    down = (round(res["download"] / 1024 / 1024))
    up = (round(res["upload"] / 1024 / 1024))
    ping = (round(res["ping"]))
    pacote = perda(servidor)
    resp = {'download': down, 'upload': up, 'ping': ping, 'perda': pacote, 'atualizado': atualizado}
    return resp
