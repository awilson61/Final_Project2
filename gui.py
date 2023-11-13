# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProduceShop(object):
    def setupUi(self, ProduceShop):
        ProduceShop.setObjectName("ProduceShop")
        ProduceShop.resize(510, 600)
        ProduceShop.setMinimumSize(QtCore.QSize(510, 600))
        ProduceShop.setMaximumSize(QtCore.QSize(510, 600))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        ProduceShop.setFont(font)
        ProduceShop.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=ProduceShop)
        self.centralwidget.setObjectName("centralwidget")
        self.pear_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.pear_image.setGeometry(QtCore.QRect(20, 50, 51, 81))
        self.pear_image.setText("")
        self.pear_image.setPixmap(QtGui.QPixmap("pear.png"))
        self.pear_image.setScaledContents(True)
        self.pear_image.setWordWrap(False)
        self.pear_image.setObjectName("pear_image")
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(20, 510, 151, 51))
        self.submit_button.setObjectName("submit_button")
        self.clear_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(190, 510, 121, 51))
        self.clear_button.setObjectName("clear_button")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(139, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.strawberries_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.strawberries_image.setGeometry(QtCore.QRect(0, 140, 101, 71))
        self.strawberries_image.setText("")
        self.strawberries_image.setPixmap(QtGui.QPixmap("strawberries.png"))
        self.strawberries_image.setScaledContents(True)
        self.strawberries_image.setWordWrap(False)
        self.strawberries_image.setObjectName("strawberries_image")
        self.pineapple_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.pineapple_image.setGeometry(QtCore.QRect(0, 210, 111, 111))
        self.pineapple_image.setText("")
        self.pineapple_image.setPixmap(QtGui.QPixmap("pineapple.png"))
        self.pineapple_image.setScaledContents(True)
        self.pineapple_image.setWordWrap(False)
        self.pineapple_image.setObjectName("pineapple_image")
        self.watermelon_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.watermelon_image.setGeometry(QtCore.QRect(265, 230, 81, 81))
        self.watermelon_image.setText("")
        self.watermelon_image.setPixmap(QtGui.QPixmap("watermelon.png"))
        self.watermelon_image.setScaledContents(True)
        self.watermelon_image.setWordWrap(False)
        self.watermelon_image.setObjectName("watermelon_image")
        self.apple_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.apple_image.setGeometry(QtCore.QRect(255, 60, 91, 71))
        self.apple_image.setText("")
        self.apple_image.setPixmap(QtGui.QPixmap("apple.png"))
        self.apple_image.setScaledContents(True)
        self.apple_image.setWordWrap(False)
        self.apple_image.setOpenExternalLinks(False)
        self.apple_image.setObjectName("apple_image")
        self.banana_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.banana_image.setGeometry(QtCore.QRect(265, 130, 71, 91))
        self.banana_image.setText("")
        self.banana_image.setPixmap(QtGui.QPixmap("banana.png"))
        self.banana_image.setScaledContents(True)
        self.banana_image.setWordWrap(False)
        self.banana_image.setOpenExternalLinks(False)
        self.banana_image.setObjectName("banana_image")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 161, 21))
        self.label_2.setObjectName("label_2")
        self.produce_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.produce_label.setGeometry(QtCore.QRect(100, 320, 231, 161))
        self.produce_label.setText("")
        self.produce_label.setObjectName("produce_label")
        self.total_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(100, 490, 60, 16))
        self.total_label.setText("")
        self.total_label.setObjectName("total_label")
        self.dollars_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.dollars_label.setGeometry(QtCore.QRect(270, 490, 191, 16))
        self.dollars_label.setText("")
        self.dollars_label.setObjectName("dollars_label")
        self.cost_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.cost_label.setGeometry(QtCore.QRect(270, 320, 191, 161))
        self.cost_label.setText("")
        self.cost_label.setObjectName("cost_label")
        self.pear_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pear_input.setGeometry(QtCore.QRect(95, 90, 113, 21))
        self.pear_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pear_input.setObjectName("pear_input")
        self.strawberry_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.strawberry_input.setGeometry(QtCore.QRect(95, 170, 113, 21))
        self.strawberry_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.strawberry_input.setObjectName("strawberry_input")
        self.pineapple_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pineapple_input.setGeometry(QtCore.QRect(95, 260, 113, 21))
        self.pineapple_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pineapple_input.setObjectName("pineapple_input")
        self.watermelon_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.watermelon_input.setGeometry(QtCore.QRect(345, 260, 113, 21))
        self.watermelon_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.watermelon_input.setObjectName("watermelon_input")
        self.banana_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.banana_input.setGeometry(QtCore.QRect(345, 170, 113, 21))
        self.banana_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.banana_input.setObjectName("banana_input")
        self.apple_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.apple_input.setGeometry(QtCore.QRect(345, 90, 113, 21))
        self.apple_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.apple_input.setObjectName("apple_input")
        self.exception_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.exception_label.setGeometry(QtCore.QRect(130, 330, 241, 161))
        self.exception_label.setText("")
        self.exception_label.setObjectName("exception_label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(95, 70, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(95, 150, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(95, 240, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(345, 240, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(345, 150, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(345, 70, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.receipt_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.receipt_button.setGeometry(QtCore.QRect(330, 510, 151, 51))
        self.receipt_button.setObjectName("receipt_button")
        ProduceShop.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ProduceShop)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 24))
        self.menubar.setObjectName("menubar")
        ProduceShop.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ProduceShop)
        self.statusbar.setObjectName("statusbar")
        ProduceShop.setStatusBar(self.statusbar)

        self.retranslateUi(ProduceShop)
        QtCore.QMetaObject.connectSlotsByName(ProduceShop)

    def retranslateUi(self, ProduceShop):
        _translate = QtCore.QCoreApplication.translate
        ProduceShop.setWindowTitle(_translate("ProduceShop", "Produce Shop"))
        self.submit_button.setText(_translate("ProduceShop", "SUBMIT"))
        self.clear_button.setText(_translate("ProduceShop", "CLEAR"))
        self.label.setText(_translate("ProduceShop", "Welcome to the Produce Stand!"))
        self.label_2.setText(_translate("ProduceShop", "Spend $50 get 5$ off!"))
        self.label_3.setText(_translate("ProduceShop", "Pears 0.20 per lb"))
        self.label_4.setText(_translate("ProduceShop", "Strawberries 0.40 per lb"))
        self.label_5.setText(_translate("ProduceShop", "Pineapples 0.30 per lb"))
        self.label_9.setText(_translate("ProduceShop", "Watermelons 0.10 per lb"))
        self.label_7.setText(_translate("ProduceShop", "Bananas 0.08 per lb"))
        self.label_8.setText(_translate("ProduceShop", "Apples 0.10 per lb"))
        self.receipt_button.setText(_translate("ProduceShop", "PRINT REICIPT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProduceShop = QtWidgets.QMainWindow()
    ui = Ui_ProduceShop()
    ui.setupUi(ProduceShop)
    ProduceShop.show()
    sys.exit(app.exec())
