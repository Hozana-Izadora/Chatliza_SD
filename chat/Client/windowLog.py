import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import tuplas as ts
from config import*

from mqtt import *
# Função de criação da janela de Log
def createWindowLog():
    app = QApplication(sys.argv) # Recebe instância da aplicação em Qt
    win = LogWindow() # Inicia instância da janela de log
    win.show() # mostra a janela
    app.exec_() # interrompe execução da aplicação
    
    
    # Retorna parâmetros do usuário para iniciar chat
    return (win.name, win.nick , win.status, win.addr, win.prt)

# Classe da tela de login
# - cria interface para login
# - recebe parâmetros para inicializar conexão e aplicação principal

class LogWindow(QMainWindow):
    
    # Constrói janela e cria atributos de entrada
    def __init__(self):

        # Inicializando construtor da janela
        super(QMainWindow, self).__init__()
  
        # Carregando componentes da interface
        self.setupUi()

        # Inicializa atributos para realizar conexão 
        self.name = False
        self.addr = False
        self.prt = False

    # Carrega objetos e layout da interface
    def setupUi(self):

        # WINDOW      
        self.setWindowIcon(QtGui.QIcon(u"img\\miniLogo.png"))
        self.setObjectName("LogWindow") 
        self.resize(470, 742)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(200, 10, 100, 255), stop:0.971591 rgba(50, 100, 200, 255));")
        
        # FONTES
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        font1 = QFont()
        font1.setPointSize(14)
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(12)
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(18)
        font4 = QFont()
        font4.setFamily(u"Ink Free")
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setWeight(75)
   
        # MAIN GRID - organiza elementos de forma responsiva
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # LOGO
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMaximumSize(QSize(200, 200))
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setAutoFillBackground(False)
        self.logo.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Plain)
        self.logo.setPixmap(QPixmap(u"img\\logo.png"))        
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));")
        self.gridLayout.addWidget(self.logo, 1, 1, 1, 1, Qt.AlignHCenter)
        
        # TÍTULO
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMaximumSize(QSize(16777215, 40))
        self.titulo.setFont(font4)
        self.titulo.setLayoutDirection(Qt.LeftToRight)
        self.titulo.setFrameShape(QFrame.NoFrame)
        self.titulo.setFrameShadow(QFrame.Plain)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.titulo, 2, 1, 1, 1)

        # LABEL LOGIN
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        # LABEL USERNAME
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)

        # INPUT USERNAME
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(400, 31))
        self.username.setFont(font2)
        self.username.setFocus()
        self.username.setStyleSheet(u"background-color: white;")
        self.gridLayout.addWidget(self.username, 5, 1, 1, 1)

        # LABEL ENDEREÇO
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)

        # INPUT ENDEREÇO
        self.adress = QLineEdit(self.centralwidget)
        self.adress.setObjectName(u"adress")
        self.adress.setMaximumSize(QSize(400, 31))
        self.adress.setFont(font2)
        self.adress.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.adress, 7, 1, 1, 1)

        # LABEL PORTA
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)

        # INPUT PORTA
        self.port = QLineEdit(self.centralwidget)
        self.port.setObjectName(u"port")
        self.port.setMaximumSize(QSize(400, 31))
        self.port.setFont(font2)
        self.port.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.port, 9, 1, 1, 1)

        # LABEL NICK
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)

        # INPUT NICK
        self.nick = QLineEdit(self.centralwidget)
        self.nick.setObjectName(u"nick")
        self.nick.setMaximumSize(QSize(400, 31))
        self.nick.setFont(font2)
        self.nick.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.nick, 11, 1, 1, 1)

        # LABEL LATITUDE
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_7, 12, 1, 1, 1)

        # INPUT LATITUDE
        self.latitude = QLineEdit(self.centralwidget)
        self.latitude.setObjectName(u"latitude")
        self.latitude.setMaximumSize(QSize(400, 31))
        self.latitude.setFont(font2)
        self.latitude.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.latitude, 13, 1, 1, 1)

        # LABEL LONGITUDE
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_8, 14, 1, 1, 1)

        # INPUT LONGITUDE
        self.longitude = QLineEdit(self.centralwidget)
        self.longitude.setObjectName(u"longitude")
        self.longitude.setMaximumSize(QSize(400, 31))
        self.longitude.setFont(font2)
        self.longitude.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.longitude, 15, 1, 1, 1)

        # LABEL DISTANCIA
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_9, 16, 1, 1, 1)

        # INPUT DISTANCIA
        self.distancia = QLineEdit(self.centralwidget)
        self.distancia.setObjectName(u"distancia")
        self.distancia.setMaximumSize(QSize(400, 31))
        self.distancia.setFont(font2)
        self.distancia.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.distancia, 17, 1, 1, 1)

        # LABEL STATUS
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.label_10, 18, 1, 1, 1)

        # INPUT STATUS
        self.status = QLineEdit(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setMaximumSize(QSize(400, 31))
        self.status.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.status, 19, 1, 1, 1)

        # LABEL ERRO - se o usuário não preencher campos de entrada
        self.error = QLabel(self)
        self.error.setObjectName(u"errorLabel")
        self.error.setFont(font)
        self.error.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: Red;")
        self.gridLayout.addWidget(self.error, 20, 1, 1, 1)             
        

        # BUTTON ENTRAR
        self.entrar = QPushButton(self.centralwidget)
        self.entrar.setObjectName(u"entrar")
        self.entrar.setSizeIncrement(QSize(0, 0))
        self.entrar.setBaseSize(QSize(0, 0))
        self.entrar.setFont(font1)
        self.entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.entrar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0));\n color: white;")
        self.gridLayout.addWidget(self.entrar, 22, 1, 1, 1)
        self.entrar.clicked.connect(self.login) # Cria sinal para botar enviar


        # SPACERS
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 21, 1, 1, 1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        # Posiciona grid na janela
        self.setCentralWidget(self.centralwidget)


        self.completeUi()

        # Conecta slots aos elementos (botão enviar) permitindo que enviem sinais (função de log)
        QMetaObject.connectSlotsByName(self)

    # Insere nomes e placeholders dos campos
    def completeUi(self):

        # Nomes e textos das tabelas
        self.setWindowTitle(QCoreApplication.translate("self", u"Chatliza", None))
        self.label_2.setText(QCoreApplication.translate("self", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("self", u"Endere\u00e7o", None))
        self.label_4.setText(QCoreApplication.translate("self", u"Porta", None))
        self.label_5.setText(QCoreApplication.translate("self", u"Login", None))
        self.label_6.setText(QCoreApplication.translate("self", u"Nick", None))
        self.label_7.setText(QCoreApplication.translate("self", u"Latitude", None))
        self.label_8.setText(QCoreApplication.translate("self", u"Longitude", None))
        self.label_9.setText(QCoreApplication.translate("self", u"Distância", None))
        self.label_10.setText(QCoreApplication.translate("self", u"Status", None))
        self.entrar.setText(QCoreApplication.translate("self", u"Entrar", None))
        self.titulo.setText(QCoreApplication.translate("self", u"Chatliza", None))
        self.logo.setText("")

        # Place Holders dos campos
        self.username.setPlaceholderText(QCoreApplication.translate("self", u"Iza", None))
        self.adress.setPlaceholderText(QCoreApplication.translate("self", u"123.456.7.890", None))
        self.port.setPlaceholderText(QCoreApplication.translate("self", u"8888", None))
        self.nick.setPlaceholderText(QCoreApplication.translate("self", u"@iza", None))
        self.latitude.setPlaceholderText(QCoreApplication.translate("self", u"coord. x", None))
        self.longitude.setPlaceholderText(QCoreApplication.translate("self", u"coord. y", None))
        self.distancia.setPlaceholderText(QCoreApplication.translate("self", u"metros", None))
        self.status.setPlaceholderText(QCoreApplication.translate("self", u"True ou False", None))

    # Efetua login
    def login(self):

        # Recebe entradas dos campos
        self.name = self.username.text()
        self.addr = str(self.adress.text())
        self.prt = self.port.text()
        self.nick = self.nick.text()
        self.latitude = self.latitude.text()
        self.longitude = self.longitude.text()
        self.distancia = self.distancia.text()
        self.status = self.status.text()

        # (1) Se um dos campos estiver vazio é enviado o valor padrão
        if len(self.name)==0:
            self.name = 'User'
        if len(self.addr)==0:
            self.addr = SERVER
        if len(self.prt)==0:
            self.prt = PORT
        if len(self.nick)==0:
            self.nick = '@user'
        if len(self.latitude)==0:
            self.latitude = 50
        if len(self.longitude)==0:
            self.longitude = 50
        if len(self.distancia)==0:
            self.distancia = 50
        if len(self.status)==0:
            self.status = True      

        if(self.status == 'False' or self.status == False):
            self.status = False
            self.mqtt =  Mqtt(self.nick, self.username, 'public', 'broker.emqx.io', 1883)
        else:
            self.status = True      

        data = [self.name,self.nick,self.status,self.latitude,self.longitude,self.distancia]
        ts.createUser(data)
        self.close()        

    # Detecta event key
    def keyPressEvent(self, event):
        
        # Salva evento
        key = event.key() 
        if key == QtCore.Qt.Key_Return: # se evento for Retur (ENTER) 
            self.login() # chama função de login


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LogWindow()
    win.show()
    app.exec_()