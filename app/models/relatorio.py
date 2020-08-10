from app import db


class Relatorio(db.Model):
    __tablename__ = 'relatorios'
    id = db.Column(db.Integer, primary_key=True)
    data_queda = db.Column(db.String(11))
    hora_queda = db.Column(db.String(8))
    data_volta = db.Column(db.String(11))
    hora_volta = db.Column(db.String(8))
    periodo = db.Column(db.String(8))
    protocolo = (db.String(60))


class Qualidade(db.Model):
    __tablename__ = 'qualidades'
    id = db.Column(db.Integer, primary_key=True)
    download = db.Column(db.Integer())
    upload = db.Column(db.Integer())
    ping = db.Column(db.Integer())
    perda = db.Column(db.Integer())
    atualizado = db.Column(db.String(11))

    def __init__(self, download, upload, ping, perda, atualizado):
        self.download = download
        self.upload = upload
        self.ping = ping
        self.perda = perda
        self.atualizado = atualizado



class Desconto(db.Model):
    __tablename__ = 'descontos'
    id = db.Column(db.Integer, primary_key=True)
    janeiro = db.Column(db.Float)
    fevereiro = db.Column(db.Float)
    marco = db.Column(db.Float)
    abril = db.Column(db.Float)
    maio = db.Column(db.Float)
    junho = db.Column(db.Float)
    julho = db.Column(db.Float)
    agosto = db.Column(db.Float)
    setembro = db.Column(db.Float)
    outubro = db.Column(db.Float)
    novembro = db.Column(db.Float)
    dezembro = db.Column(db.Float)


class Protocolo(db.Model):
    __tablename__ = 'protocolos'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(11))
    queda = db.Column(db.String(8))
    protocolo = db.Column(db.String(60))
