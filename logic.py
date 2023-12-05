from PyQt6.QtCore import QSize, Qt, QObject, QEvent
from PyQt6.QtGui import QKeySequence, QAction, QIcon, QShortcut
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from gui import *
from datetime import date


class Logic(QMainWindow, Ui_ProduceShop):
    def __init__(self) -> None:
        """
        Function to initialize the object's attributes
        """
        super().__init__()
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.receipt_button.clicked.connect(lambda: self.receipt_print())
        self.DISCOUNT = 50

        # This adds an event filter that permits keyboard shortcuts for clear, submit, and receipt_print functions.
        event_filter = GlobalShortcutEventFilter(self)
        QApplication.instance().installEventFilter(event_filter)

    def clear(self) -> None:
        """
        This function clears all the labels in the GUI.
        """
        self.button_click_clear()
        self.receipt_label_printed.clear()
        self.exception_label.clear()

    def clean_user_input(self, text: str) -> float:
        """
        This ensures that the input is converted to a non-negative float or an exception is raised.
        :param text: the value of each fruit's input box.
        :return: A float representing the number of pounds to be purchased of a fruit.
        """
        if text == '':
            float_pounds = 0.0
        else:
            float_pounds = float(text)
        if float_pounds < 0:
            raise ValueError
        return float_pounds

    def exception_handling(self) -> None:
        """
        This function labels the GUI and clearing unnecessary labels when an exception occurs
        """
        self.exception_label.setText(
            'Only enter positive numbers,\n e.g. 4 or 5.25. Input only numerical\n values; do not include "lbs"')
        self.button_click_clear()

    def button_click_clear(self) -> None:
        """
        This function clears the labels in the GUI. Used to condense code
        """
        self.total_label.clear()
        self.pear_input.setValue(0)
        self.strawberry_input.setValue(0)
        self.pineapple_input.setValue(0)
        self.apple_input.setValue(0)
        self.banana_input.setValue(0)
        self.watermelon_input.setValue(0)
        self.produce_label.clear()
        self.cost_label.clear()
        self.dollars_label.clear()
        self.receipt_label_printed.clear()

    def submit(self) -> None:
        """
        This function displays the total cost of all the produce.
        """
        cost_list = []
        try:
            # Converting to a float
            pear_cost = self.clean_user_input(self.pear_input.text()) * 0.20
            strawberries_cost = self.clean_user_input(self.strawberry_input.text()) * 0.40
            pineapples_cost = self.clean_user_input(self.pineapple_input.text()) * 0.30
            apples_cost = self.clean_user_input(self.apple_input.text()) * 0.10
            bananas_cost = self.clean_user_input(self.banana_input.text()) * 0.08
            watermelons_cost = self.clean_user_input(self.watermelon_input.text()) * 0.10

            # Cost calculations
            cost_list.append(pear_cost)
            cost_list.append(strawberries_cost)
            cost_list.append(pineapples_cost)
            cost_list.append(apples_cost)
            cost_list.append(bananas_cost)
            cost_list.append(watermelons_cost)
            total = sum(cost_list)
            if total >= self.DISCOUNT:
                total -= 5
                self.cost_label.setText(
                    f'${pear_cost:.2f}\n${strawberries_cost:.2f}\n${pineapples_cost:.2f}\n${apples_cost:.2f}\n${bananas_cost:.2f}\n${watermelons_cost:.2f}\n\n$-5.00')
                self.produce_label.setText(
                    'Pears\nStrawberries\nPineapples\nApples\nBananas\nWatermelons\n\nDiscount')
            else:
                self.cost_label.setText(
                    f'${pear_cost:.2f}\n${strawberries_cost:.2f}\n${pineapples_cost:.2f}\n${apples_cost:.2f}\n${bananas_cost:.2f}\n${watermelons_cost:.2f}')
                self.produce_label.setText(
                    'Pears\nStrawberries\nPineapples\nApples\nBananas\nWatermelons')
            # Setting the GUI labels
            self.total_label.setText('TOTAL:')
            self.dollars_label.setText(f'${total:.2f}')
            self.exception_label.clear()
            self.receipt_label_printed.clear()
        except ValueError:
            self.exception_handling()

    def receipt_print(self) -> None:
        """
        This function prints a digital receipt into a text file.
        """
        cost_list = []
        try:
            # Converting to a float
            pear_cost = self.clean_user_input(self.pear_input.text()) * 0.20
            strawberries_cost = self.clean_user_input(self.strawberry_input.text()) * 0.40
            pineapples_cost = self.clean_user_input(self.pineapple_input.text()) * 0.30
            apples_cost = self.clean_user_input(self.apple_input.text()) * 0.10
            bananas_cost = self.clean_user_input(self.banana_input.text()) * 0.08
            watermelons_cost = self.clean_user_input(self.watermelon_input.text()) * 0.10
            cost_list.append(pear_cost)
            cost_list.append(strawberries_cost)
            cost_list.append(pineapples_cost)
            cost_list.append(apples_cost)
            cost_list.append(bananas_cost)
            cost_list.append(watermelons_cost)
            # Cost calculations
            total = sum(cost_list)
            if total >= 50:
                total -= 5
            # Clearing all labels
            self.button_click_clear()
            self.exception_label.clear()
            # Receipt label
            self.receipt_label_printed.setText('Receipt Printed!\nThanks for shopping!')

            file = 'receipt'
            now = date.today()
            # Writing the TXT file
            with open(file, 'w') as receipt:
                receipt.write('-' * 50)
                receipt.write('\n{: ^50}\n'.format("The Produce Shop"))
                receipt.write('\n{: ^50}\n'.format('6001 Dodge Street'))
                receipt.write('{: ^50}\n'.format('Omaha, Nebraska'))
                receipt.write('{: ^50}\n'.format(f'Date: {now}'))
                receipt.write('-' * 50)

                # Format prices.
                formatted_pear_cost = f'${pear_cost:,.2f}'
                formatted_strawberries_cost = f'${strawberries_cost:,.2f}'
                formatted_pineapples_cost = f'${pineapples_cost:,.2f}'
                formatted_apples_cost = f'${apples_cost:,.2f}'
                formatted_bananas_cost = f'${bananas_cost:,.2f}'
                formatted_watermelons_cost = f'${watermelons_cost:,.2f}'
                formatted_total = f'${total:,.2f}'

                # Write to receipt.
                receipt.write('\n{: <20}{:>30}'.format(f'Pears', formatted_pear_cost))
                receipt.write('\n{: <20}{:>30}'.format(f'Strawberries', formatted_strawberries_cost))
                receipt.write('\n{: <20}{:>30}'.format(f'Pineapples', formatted_pineapples_cost))
                receipt.write('\n{: <20}{:>30}'.format(f'Apples', formatted_apples_cost))
                receipt.write('\n{: <20}{:>30}'.format(f'Bananas', formatted_bananas_cost))
                receipt.write('\n{: <20}{:>30}\n'.format(f'Watermelons', formatted_watermelons_cost))
                receipt.write('-' * 50)
                if total >= self.DISCOUNT:
                    receipt.write('\n{: <20}{:>30}\n'.format(f'Discount', '$-5.00'))
                    receipt.write('-' * 50)
                receipt.write('\n\n{: <20}{:>30}'.format(f'TOTAL:', formatted_total))
        except:
            self.exception_handling()


# This adds keyboard shortcuts.
class GlobalShortcutEventFilter(QObject):
    def __init__(self, parent):
        super().__init__(parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_C:
                self.parent().clear()
                return True
            if event.key() == Qt.Key.Key_S:
                self.parent().submit()
                return True
            if event.key() == Qt.Key.Key_R:
                self.parent().receipt_print()
                return True
        return super().eventFilter(obj, event)
