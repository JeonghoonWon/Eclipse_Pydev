import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                
import matplotlib.pyplot as plt  


import pymongo

 
def getPrices(s_name):
    # 배열 만들기
    arr = []
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    
    # sort 는 oracle 의 order by 역할
    rows = stock.find({'s_name':s_name}).sort('indate',1)
    first_price = rows[0]['s_price']
    
   # print(rows[0]['s_price'])
    
    for r in rows:
        int_s_price = int(r['s_price'])/int(first_price)
        arr.append(int_s_price)
    return arr  # 초기값으로 값들을 나누고 arr 로 나눠준다.
        
        #print(int(r['s_price'])/int(first_price)) # str 이라서 int 로 변경해준다.



# if __name__ == '__main__':
    # arr = getPrices('삼성전자')
    # print(arr)





mpl.rcParams['legend.fontsize'] = 10         

fig = plt.figure()                               
ax = fig.gca(projection='3d') 

# x : 종목
# y : 시간
# z : 가격
zs = []
x = np.zeros(10,dtype=int)
y   = range(10)

zs.append(getPrices('삼성전자'))
zs.append(getPrices('LG'))
zs.append(getPrices('SK'))

# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)    
# z = np.linspace(-2, 2, 100)                        
# r = z**2 + 1                                  
# x = r * np.sin(theta)                         
# y = r * np.cos(theta)  
                          
ax.plot(x, y, zs[0],color='blue', label='Samsung')   
ax.plot(x + 1, y, zs[1],color='gold', label='LG')
ax.plot(x + 2, y, zs[2],color='red', label='SK')      

ax.legend()                                      
plt.show()