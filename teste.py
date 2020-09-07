import webbrowser
import threading
import os


def executa(programa):
    exec(open(programa).read())


principal = threading.Thread(target=executa, args=('main.py',))

if __name__ == '__main__':
    principal.start()
    webbrowser.open_new_tab('http://127.0.0.1:5000/')
    exec(open('app.py').read())
