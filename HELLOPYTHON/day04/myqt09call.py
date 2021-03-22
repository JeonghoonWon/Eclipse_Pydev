from PyQt5 import uic, QtWidgets
import sys

from PyQt5.QtWidgets import *


form_class = uic.loadUiType("myqt09call.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        #버튼 연결
        
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
        self.pbCall.clicked.connect(self.myCall)
    
    #함수 실행 부분
    def myclick(self):
        print(self.sender().text())
        txt_old = self.leResult.text()
        txt_new = self.sender().text()
          
        self.leResult.setText(txt_old+txt_new)
    
    def myCall(self):
        txt_call = self.leResult.text()
        QtWidgets.QMessageBox.about(self,"Calling",txt_call)
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()