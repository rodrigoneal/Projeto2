from .models.relatorio import Qualidade, Relatorio
from core.speed import velocidade
from flask import url_for, redirect, render_template, request, flash, session
from core.status import gravar_json, ler_json
from . import filtros
from datetime import date, datetime, timedelta

speed = {}

status = ler_json('status')['status']


def date_picker(inicio, fim, periodo, page_num):
    if not fim:
        fim = datetime.now().date()
        fim = fim.strftime("%Y-%m-%d")
    if inicio and fim:
        inicio_ano, inicio_mes, inicio_dia = [int(i) for i in inicio.split('-')]
        fim_ano, fim_mes, fim_dia = [int(i) for i in fim.split('-')]
        start = date(year=inicio_ano, month=inicio_mes, day=inicio_dia)
        end = date(year=fim_ano, month=fim_mes, day=fim_dia)
        if end < start:
            flash('Data final não pode ser maior que a data inicial', 'warning')
        relatorio = Relatorio.query.filter(Relatorio.queda <= end).filter(Relatorio.queda >= start).filter(
            Relatorio.periodo >= periodo)
        paginate = relatorio.paginate(per_page=5, page=page_num, error_out=True)
        return paginate
    else:
        relatorio = Relatorio.query.filter(Relatorio.periodo >= periodo)
        paginate = relatorio.paginate(per_page=5, page=page_num, error_out=True)
        return paginate


def init_routes(app, db):
    app.jinja_env.filters['formatdate'] = filtros.formatar_data
    app.jinja_env.filters['parser_seconds'] = filtros.seconds_to_time

    @app.before_first_request
    def before_first_request_func():
        db.create_all()

    @app.route('/')
    @app.route('/<int:page_num>')
    def index(page_num=1):
        try:
            read = ler_json('config')
        except:
            flash('É necessário configurar o programa antes de começar', 'warning')
            return redirect(url_for('config'))

        try:
            quedas = Relatorio.query.paginate(per_page=5, page=page_num, error_out=True)
        except:
            return redirect(url_for('index'))

        return render_template('index.html', status=status, quedas=quedas)

    @app.route('/filter')
    @app.route('/filter/<int:page_num>')
    def filter(page_num=1):
        inicio = 0
        fim = 0
        date = request.args.get('periodo')
        if date:
            date = date.split(':')

            periodo = int(timedelta(hours=int(date[0]), minutes=int(date[1]), seconds=int(date[2])).total_seconds())
        else:
            periodo = 0

        argumento = request.args.get('inicio')
        if periodo > 0 and not argumento:
            session.clear()
        if 'inicio' in session:
            inicio = session['inicio']
            fim = session['fim']

            if argumento and argumento != session['inicio']:
                session['inicio'] = request.args.get('inicio')
                session['fim'] = request.args.get('fim')
                inicio = session['inicio']
                fim = session['fim']
        else:
            inicio = request.args.get('inicio')
            fim = request.args.get('fim')
            session['inicio'] = inicio
            session['fim'] = fim

        quedas = date_picker(inicio, fim, periodo, page_num)
        return render_template('filter.html', status=status, quedas=quedas)

    # Aqui Começa as rotas de qualidade

    @app.route('/qualidade/registro/<int:page_num>')
    def tabela_qualidade(page_num):
        qualidades = Qualidade.query.paginate(per_page=5, page=page_num, error_out=True)
        query = Qualidade.query.all()
        tamanho = len(query)
        avg_media = {'total': 0, 'download': 0, 'upload': 0, 'ping': 0, 'perda': 0}
        if tamanho > 0:
            soma_down = [i.download for i in query]
            soma_up = [i.upload for i in query]
            soma_ping = [i.ping for i in query]
            soma_perda = [i.perda for i in query]
            avg_down = sum(soma_down) / tamanho
            avg_up = sum(soma_up) / tamanho
            avg_ping = sum(soma_ping) / tamanho
            avg_perda = sum(soma_perda) / tamanho
            avg_media = {'total': tamanho, 'download': avg_down, 'upload': avg_up, 'ping': avg_ping, 'perda': avg_perda}
        config = ler_json('config')

        return render_template('lista_qualidade.html', status=status, qualidades=qualidades, avg_media=avg_media,
                               config=config)

    @app.route('/qualidade')
    def qualidade():
        global speed
        return render_template('qualidade.html', speed=speed)

    @app.route('/protocolo', methods=['POST'])
    def protocolo():
        id = request.form.get('id')
        proto = request.form.get('protocolo')
        relatorio = Relatorio.query.get(id)
        relatorio.protocolo = proto
        db.session.add(relatorio)
        db.session.commit()
        return redirect(url_for('index', page_num=1))

    @app.route('/speedtest')
    def speedtest():
        global speed
        speed = velocidade()
        qualidade = Qualidade(**speed)
        db.session.add(qualidade)
        db.session.commit()
        return redirect(url_for('qualidade'))

    @app.route('/config', methods=['GET', 'POST'])
    def config():
        if request.method == 'POST':
            down = request.form.get('down')
            up = request.form.get('up')
            operadora = request.form.get('operadora')
            valor = request.form.get('valor')
            if not valor:
                flash('Todos os campos são obrigatorios', 'warning')
                return redirect(url_for('config'))
            else:
                valor = valor.replace(',', '.')
            validar = valor.split('.')[0]
            if not validar.isnumeric():
                flash('Entre com um valor numerico', 'danger')
                return redirect(url_for('config'))

            config = {'download': int(down), 'upload': int(up), 'operadora': operadora, 'valor': valor}

            try:
                gravar_json(config, 'config')
                flash('Registro Salvo com Sucesso', 'success')
            except:
                flash('Erro ao gravar o registro.', 'danger')
                flash('Tente novamente.', 'danger')
            return redirect(url_for('config'))
        return render_template('config.html')
