# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dangky.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 340)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.489, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(138, 138, 142, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.input_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(80, 80, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_name.setFont(font)
        self.input_name.setAccessibleDescription("")
        self.input_name.setAutoFillBackground(False)
        self.input_name.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"color: rgb(255, 255, 255);")
        self.input_name.setOverwriteMode(False)
        self.input_name.setCenterOnScroll(False)
        self.input_name.setPlaceholderText("")
        self.input_name.setObjectName("input_name")
        self.ptn_dangky = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_dangky.setGeometry(QtCore.QRect(80, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ptn_dangky.setFont(font)
        self.ptn_dangky.setStyleSheet("color: rgb(255, 255, 255);")
        self.ptn_dangky.setObjectName("ptn_dangky")
        self.ptn_pre = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_pre.setGeometry(QtCore.QRect(240, 270, 75, 23))
        self.ptn_pre.setStyleSheet("color: rgb(255, 255, 255);")
        self.ptn_pre.setObjectName("ptn_pre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ĐĂNG KÝ"))
        self.input_name.setPlainText(_translate("MainWindow", "Nhập tên"
""))
        self.ptn_dangky.setText(_translate("MainWindow", "Chấp nhận"))
        self.ptn_pre.setText(_translate("MainWindow", "Trở lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
