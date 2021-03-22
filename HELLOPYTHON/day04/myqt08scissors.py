import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt08scissors.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        #버튼 연결
        self.pb.clicked.connect(self.myclick)
        
        #함수 실행 부분
    def myclick(self):
        
        Result = ""
        rnd = random.randrange(1,4)
        if(rnd == 1):
            self.leCom.setText("주먹")
        elif(rnd == 2):
            self.leCom.setText("가위")
        else:
            self.leCom.setText("보")
        
        Com = self.leCom.text()
        Mine = self.leMine.text()
        
        if(Com == Mine):
            Result = "비김"
        elif(Com=="주먹" and Mine=="가위" or Com=="가위" and Mine=="보" or Com=="보" and Mine=="주먹"):
            Result = "짐"
        else:
            Result = "이김"
        
       
       
        self.leResult.setText(Result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()