'''
Created on 2021. 3. 16.

@author: Josh
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.Qt import QIcon, QSize

import sys
form_class = uic.loadUiType("myomok02.ui")[0]

class Mywindow(QMainWindow,form_class):
    def __init__(self):
        # super() 
        # 자식클래스에서 부모클래스이 내용을 사용하고 싶은 경우
        # super().부모클래스내용
        super().__init__()
        self.setupUi(self)
        self.pbReset.clicked.connect(self.myreset)
        
        #전역변수
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
               
            ]
        
        self.arr2pb = []
        
        
        for i in range(19):
            line = []
            for j in range(19):
                bt = QPushButton(self)
                bt.setIcon(QtGui.QIcon("0.png"))
                bt.setIconSize(QtCore.QSize(40,40))
                bt.setGeometry(QtCore.QRect(40*j,40*i,40,40))
                bt.clicked.connect(self.myclick)
                bt.setToolTip("{},{}".format(i,j))
                line.append(bt)
            self.arr2pb.append(line)
            
        self.myrender()
        self.flag_wb = True
        
        self.flag_ing = True
    
    #reset 버튼 눌렀을 경우 초기화 시키기    
    def myreset(self):
        
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j]=0
        
        self.flag_wb = True
        self.flag_ing = True
        self.myrender()
        
    def myclick(self):
        if not self.flag_ing :
            return
        
        str = self.sender().toolTip()
        arr = str.split(",")
        i = int(arr[0])
        j = int(arr[1])
        if self.arr2D[i][j] > 0:
            return
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[i][j] = 1
            int_wb = 1
        else : 
            self.arr2D[i][j] = 2
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
            
            
        # flag 전에 처리해줘야함. 아니면 숫자가 꼬여버림
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
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.arr2pb[i][j].setIcon(QIcon('2.png'))
                    
    
                 
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Mywindow()
    myWindow.show()
    app.exec_()
        
        
        
        
        