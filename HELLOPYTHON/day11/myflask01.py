from flask import Flask

app = Flask(__name__)
@app.route("/hello1")
def hello():                           
    return "<h1>Hello Flask</h1>"

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")