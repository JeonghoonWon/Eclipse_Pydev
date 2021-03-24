from flask import Flask, request
from flask import render_template
import pymysql

def mySelect(s_name):
    db = pymysql.connect(host="localhost", user="root", passwd="python", db="python", charset="utf8")
    cur = db.cursor()
    
    sql = "SELECT s_code, s_name, s_price, in_date FROM stock WHERE s_name='" + s_name + "' LIMIT 10"
    cur.execute(sql)
    
    rows = cur.fetchall()                           
    
    return rows

app = Flask(__name__)

@app.route("/stock") 
def myStock():  
    s_name = request.args.get("s_name", "삼성전자")          
    list = mySelect(s_name)   
    return render_template("stock.html", list=list)
    
if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")
    

