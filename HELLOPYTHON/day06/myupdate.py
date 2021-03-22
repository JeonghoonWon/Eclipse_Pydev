import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )

mycursor = mydb.cursor()

sql = "update sample set col03='수정' where col02='1' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"행이 수정되었습니다.")
mydb.close()