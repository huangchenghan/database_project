import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QWidget
from numpy import select
import ui # main ui
import search_controller



class MainWindow(QMainWindow, search_controller.MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        search_controller.MainWindow.__init__(self, self.ui)
        
    def paintEvent(self, e): # will trigger when resize window
        pass

    def quit(self):
        sys.exit(app.exec_())

    def open_view(self):
        self.interface.destroy()
        self.show()
        # pass

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    # window.hide()
    # window.interface.show()
    sys.exit(app.exec_())
