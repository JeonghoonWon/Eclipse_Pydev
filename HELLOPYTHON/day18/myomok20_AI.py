import sys

from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.Qt import QIcon, QSize
from PyQt5.QtWidgets import *
from tensorflow.python.keras.models import load_model

import numpy as np


form_class = uic.loadUiType("myomok20_AI.ui")[0]
#모델 가져오기
model = load_model('models/20201213_202430.h5')

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbReset.clicked.connect(self.myreset)
  
        
        self.seq = 0
        #print(self.pb)
        #버튼 연결
        
        #self.loadUI()
        #함수 실행 부분
        
        
        
        #전역변수 : self.이름
        self.arr2D=np.zeros((20,20))
        
        self.arr2pb = []


        
   
    
    #def loadUI(self):
        
        for i in range(20):
            line = []
            for j in range(20):
                button = QPushButton(self)
                button.setIcon(QtGui.QIcon('0.png'))
                button.setIconSize(QtCore.QSize(40,40))
                button.setGeometry(QtCore.QRect(40*j,40*i,40,40))
                button.clicked.connect(self.myclick)
                button.setToolTip("{},{}".format(i,j))
                line.append(button)
            self.arr2pb.append(line)    
                #(x,y,width,height)
                
                # button 은 loadUI안에서만 존재. 다른곳에서도 사용해야하기때문에 
                # init 에 적어 전역변수로 만든다.
        self.myrender()   
        self.flag_wb = True
        
        #전역변수 default 할땐 True 로 만드는게 좋다.
        self.flag_ing = True
      
    def myreset(self):
        
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
        
        self.flag_wb = True
        self.flag_ing = True
        self.seq = 0
        self.myrender()
      
    
    
    def myclick(self):
        if not self.flag_ing :
            return
        
        str = self.sender().toolTip()
        arr = str.split(",")
        i = int(arr[0]) 
        j = int(arr[1])
        
        if self.arr2D[i][j] == -1 or self.arr2D[i][j] == 1:
            return
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[i][j] = 1
            int_wb = 1
        else :    
            self.arr2D[i][j] = -1
            int_wb = 2
        self.myrender()
        
        up = self.getUP(i,j,int_wb)
        dw = self.getDW(i,j,int_wb)
        ri = self.getRI(i,j,int_wb)
        le = self.getLE(i,j,int_wb)
        ul = self.getUL(i,j,int_wb)
       
        ur = self.getUR(i,j,int_wb)
        dl = self.getDL(i,j,int_wb)
        dr = self.getDR(i,j,int_wb)
        
       
        d1 = up + dw + 1        # 오목 느낌 나기위해 + 1 
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self,"omok","백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self,"omok","흑돌이 이겼습니다.")   
            self.flag_ing = False
            return
        # flag 전에 처리해줘야함. 아니면 숫자가 꼬여버림
        self.flag_wb = not self.flag_wb
        
        # AI PART

        input = self.arr2D.copy()
        input[(input != 1) & (input != 0)] = -1
        input[(input == 1) & (input != 0)] = 1
        input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)

        output = model.predict(input).squeeze()
        output = output.reshape((20,20))
        com_i, com_j = np.unravel_index(np.argmax(output), output.shape)
        
        self.seq += 1
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[com_i][com_j] = 1
            int_wb = 1
        else :    
            self.arr2D[com_i][com_j] = -1
            int_wb = -1
        self.myrender()
        
        up = self.getUP(com_i,com_j,int_wb)
        dw = self.getDW(com_i,com_j,int_wb)
        ri = self.getRI(com_i,com_j,int_wb)
        le = self.getLE(com_i,com_j,int_wb)
        ul = self.getUL(com_i,com_j,int_wb)
       
        ur = self.getUR(com_i,com_j,int_wb)
        dl = self.getDL(com_i,com_j,int_wb)
        dr = self.getDR(com_i,com_j,int_wb)
        
        d1 = up + dw + 1        # 오목 느낌 나기위해 + 1 
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self,"omok","백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self,"omok","흑돌이 이겼습니다.")   
            self.flag_ing = False
            return
            
        self.flag_wb = not self.flag_wb
    
    #DR
    def getDR(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt 
    
    #DL    
    def getDL(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt 
    
    
    #UR
    def getUR(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                i -= 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt 
    
    #UL
    def getUL(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                i -= 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt 
    
    #LE
    def getLE(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt 
    
    
    #RI
    def getRI(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt           
    
    
    #DW
    def getDW(self,i,j,int_wb):
        cnt = 0
        try:
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt           
    
    #UP        
    def getUP(self,i,j,int_wb):
        cnt = 0
       
         # 돌을 놓은 곳으로부터 위로 올라감. i 가 1씩 줄어듬. 
         # 위쪽을 확인하면서 흰돌인 경우 1씩 cnt 증가
         # 
        try:
            while True :
                i -= 1
                if i < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1 
                else :
                    return cnt
        except:
            return cnt           
    
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QIcon('1.png'))
                if self.arr2D[i][j] == -1:
                    self.arr2pb[i][j].setIcon(QIcon('2.png'))
                    
    
                 
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()