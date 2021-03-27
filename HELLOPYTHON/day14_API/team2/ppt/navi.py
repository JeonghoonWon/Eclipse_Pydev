from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")     # 웰컴 페이지의 의미가 있다.
@app.route("/navi")
def navi():
    return render_template('navi.html')

if __name__ == "__main__":              
    app.run(host="192.168.0.88", port="80")
