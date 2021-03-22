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
            LIMIT 10
            '''
        
        
    
    mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    # rows 행 전체 출력
    rows = mycursor.fetchall()
    
    cnt10 = len(rows)  # price
    cnt3 = len(rows[0])  #stockNum
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3] #초기값
        for j10 in range(cnt10):
            line.append(rows[j10][i3]/first_price) # 큰 방 작은 방 확인    
        zs.append(line) 
        
    
#    for row in rows:
#        arr.append(row[2])
   
    mydb.close()
    return zs

if __name__ == '__main__':
    arr = getAllPrices()
    print(arr)
    