from datetime import datetime


def periodo(caiu, voltou):
    tempo = (voltou - caiu).total_seconds()
    return tempo


def valor_segundo(valor, periodo):
    dia = valor / 30
    hora = dia / 24
    minuto = round(hora / 60, 3)
    segundo = minuto / 60
    desconto = (periodo * segundo)
    return desconto


def desconto(caiu, voltou, valor):
    tempo = periodo(caiu, voltou)
    desc = valor_segundo(valor, tempo)
    return desc


if __name__ == '__main__':
    caiu = datetime.now().replace(microsecond=0)
    voltou = datetime.fromordinal(737720)
    a = voltou - caiu
