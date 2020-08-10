from app import db


class Relatorio(db.Model):
    __tablename__ = 'relatorios'
    id = db.Column(db.Integer, primary_key=True)
    data_queda = db.Column(db.String(11))
    hora_queda = db.Column(db.String(8))
    data_volta = db.Column(db.String(11))
    hora_volta = db.Column(db.String(8))
    periodo = db.Column(db.String(8))


class Qualidade(db.Model):
    __tablename__ = 'qualidades'
    id = db.Column(db.Integer, primary_key=True)
    download = db.Column(db.Integer())
    upload = db.Column(db.Integer())
    ping = db.Column(db.Integer())
    perda = db.Column(db.Integer())
    atualizado = db.Column(db.String(11))

