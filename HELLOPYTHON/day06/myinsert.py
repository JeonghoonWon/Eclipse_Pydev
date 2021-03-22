import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )
# db와 상호작용하기위해 cursor 설정을 해줘야 함.
#DictCursor가 아닌 일반 cursor를 사용하면 결과가 일반적으로는 튜플 형태로 리턴됨
mycursor = mydb.cursor()


sql = "insert into sample(col01,col02,col03)values(%s,%s,%s)"
val = ("가","나","다")

cnt = mycursor.execute(sql,val)

#print("cnt",cnt)

mydb.commit()

print(mycursor.rowcount,"행이 추가되었습니다.")
mydb.close()
