import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QPushButton, QLabel
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="bancocursos"
)
cursor = cx.cursor()

class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setGeometry(100,100,360,400)
        self.setWindowTitle("Cursos cadastrados")

        labelId = QLabel("Id Curso: ")
        self.editId = QLineEdit()

        labelNomeCurso = QLabel("Nome do Curso: ")
        self.editNomeCurso = QLineEdit()

        labelCargaHoraria = QLabel("Carga Horária: ")
        self.editCargaHoraria = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        layout.addWidget(labelId)
        layout.addWidget(self.editId)

        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)

        layout.addWidget(labelCargaHoraria)
        layout.addWidget(self.editCargaHoraria)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCur)

        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(10)

        headerLine=["Id","Curso","Carga Horária"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from tbcursos")
        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

       
        layout.addWidget(tbcursos)
        self.setLayout(layout)
    
    def upCur(self):
        if(self.editId.text() == ""):
            print("Não é possível atualizar sem o Id do curso")

        elif(self.editNomeCurso.text() == "" and self.editCargaHoraria.text() == ""):
            print("Não é possível atualizar se não houver dados")

        elif(self.editNomeCurso.text() != "" and self.editCargaHoraria.text() == ""):
            cursor.execute("update tbcursos set nome_curso=%s where cursos_id=%s",
                           (self.editNomeCurso.text(), self.editId.text()))
            
        elif(self.editNomeCurso.text() == "" and self.editCargaHoraria.text() != ""):
            cursor.execute("update tbcursos set carga_horaria=%s where cursos_id=%s",
                           (self.editCargaHoraria.text(), self.editId.text()))
        else:
            cursor.execute("update tbcursos set nome_curso=%s, carga_horaria=%s where cursos_id=%s",
                           (self.editNomeCurso.text(),self.editCargaHoraria.text(), self.editId.text()))
            
        cx.commit()
        print("Todas as modificações foram realizadas")

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())