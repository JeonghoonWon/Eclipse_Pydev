import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                
import matplotlib.pyplot as plt  
import pymysql

def getAllPrices():
    zs = []
    mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "python",
        database = "_stock_old"
        )
    
    #statement
    mycursor = mydb.cursor()
    
    # 페이징 처리 가 아닌 이상 *를 사용하지 않는게 좋다. 하나씩 컬럼 적는게 좋다.
    sql =   '''
         SELECT 
           *
        FROM 
            stock_sync_0121
            
            '''
        
        
    
    mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    # rows 행 전체 출력
    rows = mycursor.fetchall()
    
    cnt10 = len(rows)  # price
    cnt3 = len(rows[0])-1  #stockNum
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3] #초기값

        for j10 in range(cnt10):
            if first_price == 0:
                line.append(0.8)
            else:    
                line.append(int(rows[j10][i3])/int(first_price)) # 큰 방 작은 방 확인    
        zs.append(line) 
        
    
#    for row in rows:
#        arr.append(row[2])
   
    mydb.close()
    return zs

mpl.rcParams['legend.fontsize'] = 10         

fig = plt.figure()                               
ax = fig.gca(projection='3d') 

# x : 종목
# y : 시간
# z : 가격

zs = getAllPrices()

for i in range(len(zs[0])+1):
    x = np.zeros(i)
    y   = range(i)

    

#    print(getPrices('삼성전자')[i]/getPrices('삼성전자')[0])
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)    
# z = np.linspace(-2, 2, 100)                        
# r = z**2 + 1                                  
# x = r * np.sin(theta)                         
# y = r * np.cos(theta)  


# zs 의 갯수 만큼 for문 돌린다.

print(len(zs))
print(len(zs[0]))

for i in range(len(zs)):
    ax.plot(x + i, y, zs[i])   
                              
# ax.plot(x + 0, y, zs[0],color='blue',label ='1')   
# ax.plot(x + 1, y, zs[1],color='gold',label ='2')
# ax.plot(x + 2, y, zs[2],color='red',label ='3')
# ax.plot(x + 3, y, zs[3],color='pink',label ='4')     

ax.legend()                                      
plt.show()