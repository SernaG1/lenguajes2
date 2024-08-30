from PyQt6 import QtCore, QtGui, QtWidgets
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.provider import Provider
from controlator.dao_logic import Dao
from controlator.connection import DataBase




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 475)
        self.lbl_id = QtWidgets.QLabel(parent=Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(200, 10, 151, 21))
        self.lbl_id.setObjectName("lbl_id")
        self.lbl_nit = QtWidgets.QLabel(parent=Dialog)
        self.lbl_nit.setGeometry(QtCore.QRect(200, 50, 151, 21))
        self.lbl_nit.setObjectName("lbl_nit")
        self.lbl_comp_name = QtWidgets.QLabel(parent=Dialog)
        self.lbl_comp_name.setGeometry(QtCore.QRect(200, 100, 151, 21))
        self.lbl_comp_name.setObjectName("lbl_comp_name")
        self.ln_nit = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_nit.setGeometry(QtCore.QRect(200, 80, 151, 20))
        self.ln_nit.setObjectName("ln_nit")
        self.ln_comp_name = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_comp_name.setGeometry(QtCore.QRect(200, 130, 151, 20))
        self.ln_comp_name.setObjectName("ln_comp_name")
        self.lbl_addres = QtWidgets.QLabel(parent=Dialog)
        self.lbl_addres.setGeometry(QtCore.QRect(200, 160, 151, 21))
        self.lbl_addres.setObjectName("lbl_addres")
        self.ln_address = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_address.setGeometry(QtCore.QRect(200, 190, 151, 20))
        self.ln_address.setObjectName("ln_address")
        self.ln_phone = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_phone.setGeometry(QtCore.QRect(200, 250, 151, 20))
        self.ln_phone.setObjectName("ln_phone")
        self.lbl_phone = QtWidgets.QLabel(parent=Dialog)
        self.lbl_phone.setGeometry(QtCore.QRect(200, 220, 151, 21))
        self.lbl_phone.setObjectName("lbl_phone")
        self.btn_save = QtWidgets.QPushButton(parent=Dialog)
        self.btn_save.setGeometry(QtCore.QRect(230, 420, 81, 41))
        self.btn_save.setObjectName("btn_save")
        self.lbl_email = QtWidgets.QLabel(parent=Dialog)
        self.lbl_email.setGeometry(QtCore.QRect(200, 280, 151, 21))
        self.lbl_email.setObjectName("lbl_email")
        self.ln_email = QtWidgets.QLineEdit(parent=Dialog)
        self.ln_email.setGeometry(QtCore.QRect(200, 310, 151, 20))
        self.ln_email.setObjectName("ln_email")
        self.lbl_idprint = QtWidgets.QLabel(parent=Dialog)
        self.lbl_idprint.setGeometry(QtCore.QRect(200, 30, 151, 21))
        self.lbl_idprint.setText("")
        self.lbl_idprint.setObjectName("lbl_idprint")
        self.btn_save.clicked.connect(self.save_provider)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_id.setText(_translate("Dialog", "ID PROVEEDOR"))
        self.lbl_nit.setText(_translate("Dialog", "NIT"))
        self.lbl_comp_name.setText(_translate("Dialog", "Razon Social"))
        self.lbl_addres.setText(_translate("Dialog", "Direccion"))
        self.lbl_phone.setText(_translate("Dialog", "Telefono"))
        self.btn_save.setText(_translate("Dialog", "Guardar"))
        self.lbl_email.setText(_translate("Dialog", "email"))

    def createProvider(self):
        if self.ln_nit.text()\
        and self.ln_comp_name.text()\
        and self.ln_address.text() \
        and self.ln_phone.text()\
        and self.ln_email.text() != (""):
            obj_provider = Provider(self.ln_nit.text(),self.ln_comp_name.text(),self.ln_address.text(), self.ln_phone.text(), self.ln_email.text())
    
    def save_provider(self,provider):
        db = DataBase()
        db.create_connection()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
