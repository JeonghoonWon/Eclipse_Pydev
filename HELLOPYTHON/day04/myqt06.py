import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        #버튼 연결
        self.pb.clicked.connect(self.myclick)
        
        #함수 실행 부분
    def myclick(self):
        dan = int(self.le.text())
        
        txt = ""
        for i in range(1,10):
            txt += str(dan)+"*"+str(i)+"="+str(dan*i)+"\n"
        
        txt +=("end\n")
        
        txt += str(dan)+"*"+str(1)+"="+str(dan*1)+"\n"
        txt += str(dan)+"*"+str(2)+"="+str(dan*2)+"\n"
        txt += str(dan)+"*3="+str(dan*3)+"\n"
        txt += str(dan)+"*4="+str(dan*4)+"\n"
        txt += str(dan)+"*5="+str(dan*5)+"\n"
        txt += str(dan)+"*6="+str(dan*6)+"\n"
        txt += str(dan)+"*7="+str(dan*7)+"\n"
        txt += str(dan)+"*8="+str(dan*8)+"\n"
        txt += str(dan)+"*9="+str(dan*9)+"\n"
       
        
        self.te.setText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()