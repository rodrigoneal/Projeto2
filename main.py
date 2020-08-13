from core.core import Requisicao
from core.converso import periodo
from app.models.relatorio import Relatorio, db
from app import create_app
from core.status import tem_internet

app = create_app()

requisicao = Requisicao()

queda = {'queda': None, 'volta': None, 'periodo': periodo}

with app.app_context():
    db.create_all()

while True:

    status = requisicao.status()
    tem_internet(status['status'])
    if not status['status']:
        queda['queda'] = status['data']

    while not status['status']:
        tem_internet(status['status'])
        status = requisicao.status()
        if status['status']:
            queda['volta'] = status['data']
            caiu = queda['queda']
            volta = queda['volta']
            tempo = periodo(caiu, volta, opcao=1)
            queda['periodo'] = tempo
            with app.app_context():
                relatorio = Relatorio(**queda)
                db.session.add(relatorio)
                db.session.commit()
            break
