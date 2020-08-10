from .models.relatorio import Qualidade
from core.speed import velocidade
from flask import url_for, redirect, render_template, flash


def init_routes(app, db):
    @app.before_first_request
    def before_first_request_func():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/medir')
    def medir():
        velo = velocidade()
        internet = Qualidade(**velo)
        db.session.add(internet)
        db.session.commit()
        return redirect(url_for('dados'))

    @app.route('/dados')
    def dados():
        qual = Qualidade.query.all()
        return render_template('qualidade.html', qual=qual)
