import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        #버튼 연결
        self.pb.clicked.connect(self.myclick)
        
        #함수 실행 부분
    def myclick(self):
        print("click")
        add = 0
         
        a = int(self.le1.text())
        b = int(self.le2.text())
        
        for i in range(a,b+1):
            add = add + i
        
        self.le3.setText(str(add))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()