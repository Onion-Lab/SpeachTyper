# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\b220256\Desktop\SpeachTyper\MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1027, 579)
        self.mainImage = QtWidgets.QLabel(Form)
        self.mainImage.setGeometry(QtCore.QRect(0, 0, 1027, 579))
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap("c:\\Users\\b220256\\Desktop\\SpeachTyper\\mainimage.png"))
        self.mainImage.setObjectName("mainImage")
        self.speachTextEdit = QtWidgets.QTextEdit(Form)
        self.speachTextEdit.setGeometry(QtCore.QRect(301, 128, 731, 451))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.speachTextEdit.setFont(font)
        self.speachTextEdit.setObjectName("speachTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
