import webbrowser
import threading
import os

def executa(programa):
    exec(open(programa).read())


principal = threading.Thread(target=executa, args=('main.py',))

if __name__ == '__main__':
    os.system('python -m venv .venv')
    os.system('pip install requeriments.txt')
    principal.start()
    webbrowser.open_new_tab('http://127.0.0.1:5000/')
    exec(open('app.py').read())

