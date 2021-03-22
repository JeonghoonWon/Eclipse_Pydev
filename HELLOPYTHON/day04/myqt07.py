import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        #버튼 연결
        self.pb.clicked.connect(self.myclick)
        
        #함수 실행 부분
    def myclick(self):
        
        Result = ""
        rnd = random.randrange(1,3)
        if(rnd == 1):
            self.leCom.setText("홀")
        else:
            self.leCom.setText("짝")
        
        Com = self.leCom.text()
        Mine = self.leMine.text()
        
        if(Com == Mine):
            Result = "이김"
        else:
            Result = "짐"
        
       
       
        self.leResult.setText(Result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()