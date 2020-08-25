from core.core import Requisicao
from datetime import datetime, date, timedelta
from core.speed import velocidade, perda
from sqlalchemy.sql import func
from app.models.relatorio import Qualidade,Relatorio
from app import create_app

'''import webbrowser

webbrowser.open_new_tab('http://127.0.0.1:5000/')
# testando
'''
a = '01:00:00'.split(':')

date = timedelta(hours=int(a[0]), minutes=int(a[1]),seconds=int(a[2]))
print(int(date.total_seconds()))

"""app = create_app()

with app.app_context():
    from datetime import datetime

    string = "00:00:01"
    # Considering date is in dd/mm/yyyy format


    relatorio = Relatorio.query.with_entities(Relatorio.periodo).all()
    print(relatorio)
"""





