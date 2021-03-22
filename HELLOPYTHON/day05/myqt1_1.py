import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore


form_class = uic.loadUiType("myqt1_1.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        # for i in range(0,10):
            # for j in range(0,10):
        pb = QPushButton(self)
        pb.setIcon(QtGui.QIcon('0.png'))
        pb.setIconsSize(QtCore.QSize(40,40))
                # pb.setGeometry(QtCore.QRect(40*i,40*j,40,40))
        
    
    
   
    
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()