import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import sys
import webbrowser

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(600, 400)
        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(10, 5)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.labelAPI = QLabel("Enter your API key:", self)
        self.labelAPI.move(10,65)
        self.textAPI = QLineEdit(self)
        self.textAPI.move(10, 90)
        self.labelIP = QLabel("Enter ip:", self)
        self.labelIP.move(10,125)
        self.textIP = QLineEdit(self)
        self.textIP.move(10, 150)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 185)
        self.button = QPushButton("Send", self)
        self.button.move(10, 210)
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        ip = self.textIP.text()
        apiKey = self.textAPI.text()

        if hostname == "" or ip == "" or apiKey == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else :
            #res = self.__query(hostname)
            info = self.__query2(hostname,ip,apiKey)
            #if res:
                #self.label2.setText("Answer %s" % (res["Hello"]))
                #self.label2.adjustSize()
                #self.show()
            if info:
                self.label2.setText("Answer %s" % (info))
                self.label2.adjustSize()
                self.show()
                affCarte = self.__map(hostname,ip,apiKey)
                

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()

    def __query2(self, hostname,ip,apiKey):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip,apiKey) 
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()

    def __map(self,latitude,longitude):
        url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (latitude,longitude)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "location not found")
        if r.status_code == requests.codes.OK:
            webbrowser.open(url)
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
