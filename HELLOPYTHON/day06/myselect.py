import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )

#statement
mycursor = mydb.cursor()

# 페이징 처리 가 아닌 이상 *를 사용하지 않는게 좋다. 하나씩 컬럼 적는게 좋다.
sql = "select col01,col02,col03 from sample"

mycursor.execute(sql)

# 실행결과를 fetchall()을 이용해 받아온다.
result = mycursor.fetchall()


print(result)
mydb.close()