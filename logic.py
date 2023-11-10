from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_ProduceShop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.receipt_button.clicked.connect(lambda: self.receipt_print())

    def clear(self):
        pass

    def submit(self):
        try:
            pear_price = float(self.pear_input.text())
            self.exception_label.clear()
        except:
            self.exception_label.setText(
                'Enter values that are numeric,\n e.g. 4 or 5.25 Input only numerical\n values; do not include "lbs"')

    def receipt_print(self):
        pass
