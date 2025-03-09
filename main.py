# main.py

import sys
from PyQt5 import QtWidgets
from controllers.login_controller import LoginController

def main():
    app = QtWidgets.QApplication(sys.argv)
    login = LoginController()
    login.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
