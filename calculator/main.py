import sys

import model
from view import MainWindow
from PyQt5 import QtWidgets
from controler import CalculatorController

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()

    CalculatorController(model.evaluate_expression, ui)
    sys.exit(app.exec())
