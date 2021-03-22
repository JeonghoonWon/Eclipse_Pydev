import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )

mycursor = mydb.cursor()

sql = """
        delete from sample 
        where 
            col03 = %s
      """
mycursor.execute(sql,"다")

mydb.commit()

print(mycursor.rowcount,"행이 삭제되었습니다.")
mydb.close()