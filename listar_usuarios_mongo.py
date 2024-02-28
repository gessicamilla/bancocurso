import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QVBoxLayout
from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

db = client.loja_db

class ExibirUsuarios(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,360,300)
        self.setFixedSize(500,300)
        self.setWindowTitle("Usuários cadastrados")

        tbusuarios = QTableWidget(self)
        tbusuarios.setColumnCount(4)
        tbusuarios.setRowCount(10)

        headerLine=["Id","Nome Usuário","Senha","Nivel de Acesso"]

        tbusuarios.setHorizontalHeaderLabels(headerLine)

        lintb = 0

        for us in db["usuario"].find():
            tbusuarios.setItem(lintb,0,QTableWidgetItem(str(us["_id"])))
            tbusuarios.setItem(lintb,1,QTableWidgetItem(us["nomeusuario"]))
            tbusuarios.setItem(lintb,2,QTableWidgetItem(us["senha"]))
            tbusuarios.setItem(lintb,3,QTableWidgetItem(us["nivel"]))
            lintb+=1

        layout = QVBoxLayout()
        layout.addWidget(tbusuarios)
        self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirUsuarios()
    tela.show()
    sys.exit(app.exec_())