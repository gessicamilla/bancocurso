import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QPushButton

con = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="bancocursos"
)
cursor = con.cursor()

class CadCurso(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro dos Cursos")

        labelNomeCurso = QLabel("Nome do curso:")
        self.editNomeCurso = QLineEdit()

        labelCargaHoraria = QLabel("Carga Horária:")
        self.editCargaHoraria = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("|")
        
        layout = QVBoxLayout()
        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)

        layout.addWidget(labelCargaHoraria)
        layout.addWidget(self.editCargaHoraria)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.CadCur)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)
    
    def CadCur(self):
        cursor.execute("insert into tbcursos(nome_curso,carga_horaria)values(%s,%s)",
                       (self.editNomeCurso.text(),self.editCargaHoraria.text()))
        con.commit()
        self.labelMsg.setText("Curso cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCurso()
    tela.show()
    sys.exit(app.exec_())