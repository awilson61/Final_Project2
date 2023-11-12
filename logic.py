from PyQt6.QtWidgets import *
from gui import *
from datetime import date

class Logic(QMainWindow, Ui_ProduceShop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.receipt_button.clicked.connect(lambda: self.receipt_print())


    def clear(self):
        self.exception_label.clear()
        self.pear_input.clear()
        self.strawberry_input.clear()
        self.pineapple_input.clear()
        self.apple_input.clear()
        self.banana_input.clear()
        self.watermelon_input.clear()
        self.total_label.clear()
        self.produce_label.clear()
        self.cost_label.clear()
        self.dollars_label.clear()

    def convert_to_zero(self, text):
        try:
            if text == '':
                return 0.0
            else:
                return float(text)
        except ValueError:
            self.exception_label.setText('Enter values that are numeric,\n e.g. 4 or 5.25. Input only numerical\n values; do not include "lbs"')
            self.pear_input.clear()
            self.strawberry_input.clear()
            self.pineapple_input.clear()
            self.apple_input.clear()
            self.banana_input.clear()
            self.watermelon_input.clear()
            self.total_label.clear()
            self.produce_label.clear()
            self.cost_label.clear()
            self.dollars_label.clear()
            return 0

    def submit(self):
        pear_text = self.pear_input.text().strip()
        pear_cost = self.convert_to_zero(pear_text)
        strawberries_text = self.strawberry_input.text().strip()
        strawberries_cost = self.convert_to_zero(strawberries_text)



        total = pear_cost + strawberries_cost
        self.total_label.setText('TOTAL')
        self.dollars_label.setText(f'${total:.2f}')

    def receipt_print(self):
        self.exception_label.clear()
        self.pear_input.clear()
        self.strawberry_input.clear()
        self.pineapple_input.clear()
        self.apple_input.clear()
        self.banana_input.clear()
        self.watermelon_input.clear()
        self.total_label.clear()
        self.produce_label.clear()
        self.cost_label.clear()
        self.dollars_label.clear()
        file = 'recipt'
        now = date.today()
        with open(file, 'w') as recipt:
            recipt.write('-'*50)
            recipt.write('\nThe Produce Shop\n')
            recipt.write(f'Omaha, Nebraska | Date: {now} ')
