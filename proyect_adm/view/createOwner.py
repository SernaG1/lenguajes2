import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6 import QtCore, QtGui, QtWidgets
from model.owner import Owner
from model.user import User
from controlator.dao_logic import Dao
from controlator.connection import DataBase

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 475)
        self.lbl_id = QtWidgets.QLabel(parent=Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(200, 10, 151, 21))
        self.lbl_id.setObjectName("lbl_id")
        self.ln_id = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_id.setGeometry(QtCore.QRect(200, 30, 151, 20))
        self.ln_id.setObjectName("ln_id")
        self.lbl_name = QtWidgets.QLabel(parent=Dialog)
        self.lbl_name.setGeometry(QtCore.QRect(200, 50, 151, 21))
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_surname = QtWidgets.QLabel(parent=Dialog)
        self.lbl_surname.setGeometry(QtCore.QRect(200, 100, 151, 21))
        self.lbl_surname.setObjectName("lbl_surname")
        self.ln_name = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_name.setGeometry(QtCore.QRect(200, 80, 151, 20))
        self.ln_name.setObjectName("ln_name")
        self.ln_surname = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_surname.setGeometry(QtCore.QRect(200, 130, 151, 20))
        self.ln_surname.setObjectName("ln_surname")
        self.lbl_email = QtWidgets.QLabel(parent=Dialog)
        self.lbl_email.setGeometry(QtCore.QRect(200, 160, 151, 21))
        self.lbl_email.setObjectName("lbl_email")
        self.ln_email = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_email.setGeometry(QtCore.QRect(200, 190, 151, 20))
        self.ln_email.setObjectName("ln_email")
        self.ln_phone = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_phone.setGeometry(QtCore.QRect(200, 250, 151, 20))
        self.ln_phone.setObjectName("ln_phone")
        self.lbl_phone = QtWidgets.QLabel(parent=Dialog)
        self.lbl_phone.setGeometry(QtCore.QRect(200, 220, 151, 21))
        self.lbl_phone.setObjectName("lbl_phone")
        self.btn_save = QtWidgets.QPushButton(parent=Dialog)
        self.btn_save.setGeometry(QtCore.QRect(230, 420, 81, 41))
        self.btn_save.setObjectName("btn_save")
        self.lbl_pass = QtWidgets.QLabel(parent=Dialog)
        self.lbl_pass.setGeometry(QtCore.QRect(200, 350, 151, 21))
        self.lbl_pass.setObjectName("lbl_pass")
        self.ln_pass = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_pass.setGeometry(QtCore.QRect(200, 370, 151, 20))
        self.ln_pass.setObjectName("ln_pass")
        self.lbl_user = QtWidgets.QLabel(parent=Dialog)
        self.lbl_user.setGeometry(QtCore.QRect(200, 280, 151, 21))
        self.lbl_user.setObjectName("lbl_user")
        self.ln_user = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_user.setGeometry(QtCore.QRect(200, 310, 151, 20))
        self.ln_user.setObjectName("ln_user")
        self.btn_save.clicked.connect(self.save)
        self.db=DataBase()
        self.dao=Dao(self.db.connection)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear cuentadante"))
        self.lbl_id.setText(_translate("Dialog", "Documento"))
        self.lbl_name.setText(_translate("Dialog", "Nombre"))
        self.lbl_surname.setText(_translate("Dialog", "Apellido"))
        self.lbl_email.setText(_translate("Dialog", "Email"))
        self.lbl_phone.setText(_translate("Dialog", "Telefono"))
        self.btn_save.setText(_translate("Dialog", "Guardar"))
        self.lbl_pass.setText(_translate("Dialog", "contraseña"))
        self.lbl_user.setText(_translate("Dialog", "usuario"))
        
    #def clean_fields(self):


    def create_owner(self):
        if self.ln_id.text() and \
        self.ln_surname.text() and\
        self.ln_email.text() and \
        self.ln_phone.text() and\
        self.ln_pass.text() and \
        self.ln_user.text() != (''):

            obj_owner=Owner(self.ln_id.text(), self.ln_name.text(),self.ln_surname.text(), self.ln_email.text(), self.ln_phone.text())
            self.dao.create_owner(obj_owner)
    
    def create_user(self):
        if self.ln_id.text() and self.ln_surname.text() and self.ln_email.text() and self.ln_phone.text() and\
        self.ln_pass.text() and self.ln_user.text()!= (''):
            obj_user=User(self.ln_user.text(),  self.ln_pass.text(),2)
            self.dao.create_user(obj_user)
        
    def save(self):
        self.create_owner()
        self.create_user()
        Dialog.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
