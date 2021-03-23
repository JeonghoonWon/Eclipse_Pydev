from flask import Flask,request


#
app = Flask(__name__)
# @app.route("/get") # annotation
# def hello(): # doget / dopost 방식으로 들어감. 여기선 동시에 들어옴.                          
    #
    #
    # #post와 get 이 나눠져있음. 받는 방식이 다르다.
    # a = request.args.get('a',"하ㅏ하ㅏㅏ")
    # return "<h1>Hello Flask" +a +"</h1>"
    #


@app.route("/post", methods=['POST'])
def hellopost(): # doget / dopost 방식으로 들어감. 여기선 동시에 들어옴.                          
    
    
    #post와 get 이 나눠져있음. 받는 방식이 다르다.
    a = request.form.get('a',"하ㅏ하ㅏㅏ")
    return "<h1>Hello Flask" +a +"</h1>"

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")
    
    