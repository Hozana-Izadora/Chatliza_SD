from windowLog import createWindowLog
from window import *


def start():
    # Iniciando janela de login e recebendo parâmetro
    name, nick, addr, port = createWindowLog()

    # Iniciando Janela do chat, que inicia a classe client
    if (name and addr and port):
        app = QApplication(sys.argv)
        win = MainWindow(name, nick, addr, port)

        win.show()
        app.exec_()


if __name__ == "__main__":
    
    start()

