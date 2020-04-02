# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RasterBand.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 213)
        self.btn_DataInput = QtWidgets.QToolButton(Form)
        self.btn_DataInput.setGeometry(QtCore.QRect(450, 60, 71, 31))
        self.btn_DataInput.setObjectName("btn_DataInput")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(450, 140, 71, 31))
        self.btn_ok.setObjectName("btn_ok")
        self.txt_DataInput = QtWidgets.QTextEdit(Form)
        self.txt_DataInput.setGeometry(QtCore.QRect(100, 60, 331, 31))
        self.txt_DataInput.setReadOnly(True)
        self.txt_DataInput.setObjectName("txt_DataInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据读取"))
        self.btn_DataInput.setText(_translate("Form", "浏览"))
        self.label.setText(_translate("Form", "数据路径："))
        self.btn_ok.setText(_translate("Form", "确定"))
