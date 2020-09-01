from core.core import Requisicao
from core.converso import periodo
from app.models.relatorio import Relatorio, db
from app import create_app
from core.status import gravar_json
from time import sleep
app = create_app()

requisicao = Requisicao()

registro = {'queda': None, 'volta': None, 'periodo': periodo}



while True:

    status = requisicao.status()
    gravar_json({'status':status['status']} , 'status')
    with app.app_context():
        db.create_all()
    if not status['status']:
        sleep(10)
        status = requisicao.status()
    if not status['status']:
        registro['queda'] = status['data']
        with app.app_context():
            relatorio = Relatorio()
            relatorio.queda = registro['queda']
            db.session.add(relatorio)
            db.session.commit()

    while not status['status']:
       gravar_json({'status':status['status']}, 'status')
       status = requisicao.status()
       if status['status']:
            registro['volta'] = status['data']
            caiu = registro['queda']
            volta = registro['volta']
            tempo = periodo(caiu, volta)
            registro['periodo'] = tempo
            with app.app_context():
                save = Relatorio.query.filter_by(queda=registro['queda']).first()
                save.volta = registro['volta']
                save.periodo = registro['periodo']
                db.session.add(save)
                db.session.commit()
            break
