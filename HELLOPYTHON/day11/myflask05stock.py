from flask import Flask,request, render_template
import pymysql


# @app.route("/stockname", methods = ['POST'])
# def s_name():
    #
    # s_name = request.form.get('s_name')
    # return render_template('stock.html', s_name=s_name)
# if __name__ == "__main__":              
    # app.run(host="127.0.0.1", port="80")
arr = []
mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "python",
        database = "python"
        )
        
#statement
mycursor = mydb.cursor()
    
sql =   """
            
            SELECT
            s_code,
            s_name,
            s_price,    
            in_date
            FROM stock
            WHERE
            s_name = '""" +'삼성전자'+ """'
            
            """
            
            
mycursor.execute(sql)
    
    # 실행결과를 fetchall()을 이용해 받아온다.
    # rows 행 전체 출력

rows = mycursor.fetchall()
#print(rows)
for row in rows:
    arr.append(row)
print(arr)


app = Flask(__name__)
@app.route("/stock")
def mylist(arr):
    print(arr)
    arr = arr
    return render_template('stock.html', arr = arr)    
if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")