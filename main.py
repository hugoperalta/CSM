from src.gui import ConverterApp
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())
