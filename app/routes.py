from .models.relatorio import Relatorio

def init_routes(app, db):
    relatorio = Relatorio()
    @app.before_first_request
    def before_first_request_func():
        db.create_all()

    @app.route('/')
    def index():
        relatorio.data_volta = '08/08/2020'
        db.session.add(relatorio)
        db.session.commit()
        return '<h1> Brasil</h1>'

    @app.route('/a')
    def query():
        relatorio.query.all()
        return f'{relatorio}'
