from corrupted_save_file_error import *
from GUI import Ui_MainWindow
from PyQt5 import QtWidgets

def main():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



