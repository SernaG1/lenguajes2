# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 518)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(330, 70, 241, 51))
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lbl_opcion = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_opcion.setGeometry(QtCore.QRect(350, 270, 141, 31))
        self.lbl_opcion.setObjectName("lbl_opcion")
        self.btn_signUp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_signUp.setGeometry(QtCore.QRect(350, 310, 111, 31))
        self.btn_signUp.setObjectName("btn_signUp")
        self.btn_createAcc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_createAcc.setGeometry(QtCore.QRect(350, 350, 111, 31))
        self.btn_createAcc.setObjectName("btn_createAcc")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_titulo.setText(_translate("MainWindow", "Sistema de inventario"))
        self.lbl_opcion.setText(_translate("MainWindow", "Seleccione la opcion"))
        self.btn_signUp.setText(_translate("MainWindow", "Ingresar"))
        self.btn_createAcc.setText(_translate("MainWindow", "Crear cuenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
