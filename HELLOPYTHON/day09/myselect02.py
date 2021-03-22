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
    sql =   '''
            SELECT
            s_code,
            s_name,
            s_price,
            in_date
            FROM stock
            WHERE
            s_name = 'LG'
            '''
        
        
    
    mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    # rows 행 전체 출력
    rows = mycursor.fetchall()
    for row in rows:
        arr.append(row[2])
   
    mydb.close()
    return arr

if __name__ == '__main__':
    arr = getPrices('LG')
    print(arr)
    