from datetime import timedelta


def formatar_data(data):
    if data == None:
        return ''
    return data.strftime('%d/%m/%Y %H:%M:%S')


def seconds_to_time(seconds):
    time = timedelta(seconds=seconds)
    return time
