import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                
import matplotlib.pyplot as plt  
import pymysql

def getPrices(s_name):
    arr = []
    mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "python",
        database = "python"
        )
    
    #statement
    mycursor = mydb.cursor()
    
    # 페이징 처리 가 아닌 이상 *를 사용하지 않는게 좋다. 하나씩 컬럼 적는게 좋다.
    
    sql =   """
            
            SELECT
            s_code,
            s_name,
            s_price,
            in_date
            FROM stock
            WHERE
            s_name = '""" +s_name+ """'
            
            """
        
        
    
    mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    # rows 행 전체 출력
    rows = mycursor.fetchall()
    for row in rows:
        arr.append(row[2])
   
    mydb.close()
    return arr


    




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
# ax.plot(x + 1, y, zs[1],color='gold', label='LG')
# ax.plot(x + 2, y, zs[2],color='red', label='SK')      

ax.legend()                                      
plt.show()