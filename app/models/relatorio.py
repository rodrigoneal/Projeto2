from app import db


class Relatorio(db.Model):
    __tablename__ = 'relatorios'
    id = db.Column(db.Integer, primary_key=True)
    queda = db.Column(db.DateTime, unique=True)
    volta = db.Column(db.DateTime, unique=True)
    periodo = db.Column(db.Integer())
    protocolo = db.Column(db.String(60))



class Qualidade(db.Model):
    __tablename__ = 'qualidades'
    id = db.Column(db.Integer, primary_key=True)
    download = db.Column(db.Integer())
    upload = db.Column(db.Integer())
    ping = db.Column(db.Integer())
    perda = db.Column(db.Integer())
    atualizado = db.Column(db.DateTime)

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


