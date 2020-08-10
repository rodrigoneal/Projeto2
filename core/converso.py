from datetime import datetime


def periodo(caiu, voltou):
    caiu = datetime.strptime(caiu, '%d/%m/%Y, %H:%M:%S')
    voltou = datetime.strptime(voltou, '%d/%m/%Y, %H:%M:%S')
    total_segundos = (voltou - caiu).total_seconds()
    return total_segundos


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

