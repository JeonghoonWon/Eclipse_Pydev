from flask import Flask, render_template

app = Flask(__name__)
@app.route("/list")
def mylist():
    list = ["홍길동","전우치","김도윤"]                           
    return render_template('list.html', list = list) 
if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")