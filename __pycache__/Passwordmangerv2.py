# finished: Setup, login
from PyQt5 import QtCore, QtGui, QtWidgets
import os

# GLOBAL VARIABLES
LOGIN_USERNAME = 'Admin'
LOGIN_PASSWORD = '123'

PATH_FOLDER = os.path.join('assets')
PASSWORD_PATH = os.path.join(PATH_FOLDER, 'passwords.txt')
VIEW_PATH = os.path.join(PATH_FOLDER, 'view.txt')

class Ui_MainWindow(object):

    def add(self):
        if self.login():
            platform_saved = self.add_platform_lineedit.text()
            email_saved = self.add_email_lineedit.text()
            username_saved = self.add_username_lineedit.text()
            password_saved = self.add_password_lineedit.text()


            txt_file = open(PASSWORD_PATH, 'a')
            txt_file.write('\n'+'PLATFORM: ')
            txt_file.write(platform_saved)
            txt_file.write('\n')
            txt_file.write('EMAIL: ')
            txt_file.write(email_saved)
            txt_file.write('\n')
            txt_file.write('USERNAME: ')
            txt_file.write(username_saved)
            txt_file.write('\n')
            txt_file.write('PASSWORD: ')
            txt_file.write(password_saved)
            txt_file.close()

            self.add_platform_lineedit.setText('')
            self.add_email_lineedit.setText('')
            self.add_username_lineedit.setText('')
            self.add_password_lineedit.setText('')


    def login(self):
        # takes the input from qlineedit
        login_username_lineedit_saved = self.login_username_lineedit.text()
        login_password_lineedit_saved = self.login_password_lineedit.text()
        if login_username_lineedit_saved == LOGIN_USERNAME and login_password_lineedit_saved == LOGIN_PASSWORD:
            return True
        else:
            # removes text in qlineedit if not correct
            self.login_username_lineedit.setText('')
            self.login_password_lineedit.setText('')
            return False

    def setup(self):
        if self.login():  # checks if login returned True
            if os.path.exists(PATH_FOLDER):  # checks if the folder exists
                pass
            else:
                os.mkdir(PATH_FOLDER)  # if not create folder
                # change current working directory to new folder
                os.chdir(PATH_FOLDER)
                with open('passwords.txt', 'w') as f:  # create .txt file in the folder
                    pass

    def view(self):
        if self.login():
            os.system('passwords.txt')




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # VIEW BUTTON
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(320, 340, 111, 41))
        self.view_button.setObjectName("view_button")
        self.view_button.clicked.connect(self.view)

        # ADD BUTTON
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(530, 200, 75, 23))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add)

        # LOGIN BUTTON
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(180, 50, 75, 23))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.login)

        # SETUP BUTTON
        self.setup_button = QtWidgets.QPushButton(self.centralwidget)
        self.setup_button.setGeometry(QtCore.QRect(610, 80, 91, 31))
        self.setup_button.setObjectName("setup_button")
        self.setup_button.clicked.connect(self.setup)

        # LOGIN USERNAME LINEEDIT
        self.login_username_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_username_lineedit.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.login_username_lineedit.setObjectName("login_username_lineedit")

        # LOGIN PASSWORD LINEEDIT
        self.login_password_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_password_lineedit.setGeometry(QtCore.QRect(10, 70, 161, 20))
        self.login_password_lineedit.setObjectName("login_password_lineedit")

        # PLATFORM LINEEDIT
        self.add_platform_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_platform_lineedit.setGeometry(QtCore.QRect(280, 120, 221, 20))
        self.add_platform_lineedit.setObjectName("add_platform_lineedit")

        # EMAIL LINEEDIT
        self.add_email_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_email_lineedit.setGeometry(QtCore.QRect(280, 160, 221, 20))
        self.add_email_lineedit.setObjectName("add_email_lineedit")

        # USERNAME LINEEDIT
        self.add_username_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_username_lineedit.setGeometry(QtCore.QRect(280, 200, 221, 20))
        self.add_username_lineedit.setObjectName("add_username_lineedit")

        # PASSWORD LINEEDIT
        self.add_password_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_password_lineedit.setGeometry(QtCore.QRect(280, 240, 221, 20))
        self.add_password_lineedit.setObjectName("add_password_lineedit")

        # LOGIN USERNAME LABEL
        self.login_username_label = QtWidgets.QLabel(self.centralwidget)
        self.login_username_label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.login_username_label.setObjectName("login_username_label")

        # LOGIN PASSWORD LABEL
        self.login_password_label = QtWidgets.QLabel(self.centralwidget)
        self.login_password_label.setGeometry(QtCore.QRect(10, 50, 161, 16))
        self.login_password_label.setObjectName("login_password_label")

        # HEADER
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(310, -20, 191, 61))
        self.header.setObjectName("header")

        # ADD PLATFORM LABEL
        self.add_platform_label = QtWidgets.QLabel(self.centralwidget)
        self.add_platform_label.setGeometry(QtCore.QRect(280, 100, 60, 16))
        self.add_platform_label.setObjectName("add_platform_label")

        # ADD EMAIL LABEL
        self.add_email_label = QtWidgets.QLabel(self.centralwidget)
        self.add_email_label.setGeometry(QtCore.QRect(280, 140, 51, 16))
        self.add_email_label.setObjectName("add_email_label")

        # ADD USERNAME LABEL
        self.add_username_label = QtWidgets.QLabel(self.centralwidget)
        self.add_username_label.setGeometry(QtCore.QRect(280, 180, 71, 16))
        self.add_username_label.setObjectName("add_username_label")

        # ADD PASSWORD LABEL
        self.add_password_label = QtWidgets.QLabel(self.centralwidget)
        self.add_password_label.setGeometry(QtCore.QRect(280, 220, 71, 16))
        self.add_password_label.setObjectName("add_password_label")

        # INFO BROWSER
        self.info_textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.info_textbrowser.setGeometry(QtCore.QRect(540, 0, 256, 81))
        self.info_textbrowser.setObjectName("info_textbrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.add_button.setText(_translate("MainWindow", "ADD"))
        self.view_button.setText(_translate("MainWindow", "VIEW"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))
        self.login_username_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">USERNAME</span></p></body></html>"))
        self.login_password_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PASSWORD</span></p></body></html>"))
        self.header.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Passwordmanager</span></p></body></html>"))
        self.add_email_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Email</span></p></body></html>"))
        self.add_username_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username</span></p></body></html>"))
        self.add_password_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.add_platform_label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Platform</span></p></body></html>"))

        self.info_textbrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If this is your first time running this passwordmanager, click the setup to get all the boring stuff ready.</p></body></html>"))
        self.setup_button.setText(_translate("MainWindow", "Setup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
