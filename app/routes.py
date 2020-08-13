from .models.relatorio import Qualidade, Relatorio
from core.speed import velocidade
from flask import url_for, redirect, render_template, request
from core.status import ler_tem_internet
from datetime import date
from . import filtros


def init_routes(app, db):
    app.jinja_env.filters['formatdate'] = filtros.formatar_data

    @app.before_first_request
    def before_first_request_func():
        db.create_all()

    @app.route('/')
    def home():
        return redirect(url_for('index', page_num=1))

    @app.route('/<int:page_num>')
    def index(page_num):
        tem = ler_tem_internet()
        quedas = Relatorio.query.paginate(per_page=5, page=page_num, error_out=True)
        return render_template('index.html', tem=tem['status'], quedas=quedas)

    @app.route('/qualidade/<int:page_num>')
    def qualidade(page_num):
        tem = ler_tem_internet()
        qualidades = Qualidade.query.paginate(per_page=5, page=page_num, error_out=True)
        return render_template('qualidade.html', tem=tem['status'], qualidades=qualidades)

    @app.route('/qualidade')
    def fake_qualidade():
        return redirect(url_for('qualidade', page_num=1))

    @app.route('/protocolo', methods=['POST'])
    def protocolo():
        id = request.form.get('id')
        proto = request.form.get('protocolo')
        relatorio = Relatorio.query.get(id)
        relatorio.protocolo = proto
        db.session.add(relatorio)
        db.session.commit()
        return redirect(url_for('index', page_num=1))

    @app.route('/teste')
    def teste():
        start = date(year=1990, month=1, day=1)
        end = date(year=2000, month=1, day=1)

        relatorio = Relatorio.query.filter(Relatorio.queda <= end).filter(Relatorio.queda >= start)
        print(relatorio)
        return render_template('teste.html', relatorio=relatorio)

    @app.route('/speedtest')
    def speedtest():
        speed = velocidade()
        qualidade = Qualidade(**speed)
        db.session.add(qualidade)
        db.session.commit()
        return redirect(url_for('qualidade', page_num=1))
