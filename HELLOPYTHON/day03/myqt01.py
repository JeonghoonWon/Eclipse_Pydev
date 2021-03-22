import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("hello.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self.pb)
        #버튼 연결
        self.pb.clicked.connect(self.myclick)
        
        #함수 실행 부분
    def myclick(self):
        self.lbl.setText("Good Evening")    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()