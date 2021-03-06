import pymysql

def getStocks(s_name):
    ret = []
    mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "python",
        database = "python"
        )
    
    #statement
    mycursor = mydb.cursor()
    
    # 페이징 처리 가 아닌 이상 *를 사용하지 않는게 좋다. 하나씩 컬럼 적는게 좋다.
    sql = """
            SELECT 
            s_code, 
            s_name, 
            s_price, 
            in_date
            FROM
                stock
            WHERE
                s_name = """+ s_name +"""
        
          """
    
    mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    rows = mycursor.fetchall()
    for s in rows:
#        print(s)
        temp = {'s_code':s[0], 's_name':s[1], 's_price':s[2],'in_date':s[3]}
        ret.append(temp)
     
    mydb.close()
    return ret
if __name__ == '__main__':
    stocks = getStocks('삼성전자')
    print(stocks)