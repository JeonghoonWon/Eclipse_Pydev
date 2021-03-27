# 네이버 캡차 API예제는 1) 캡차 키 발급 2) 캡차 이미지 수신 3) 캡차 입력값 비교 예제로 구성되어 있습니다.

# 네이버 캡차 API 예제 - 키발급
import os
import sys
import urllib.request
import json
from flask import Flask, render_template, request


app = Flask(__name__, static_url_path="", static_folder='static')

@app.route("/captcha")
def captcha():
    client_id = "EosLbjeD2Ad2CfIN_FAA"
    client_secret = "FlozGi2tze"
    code = "0"
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    
    k = response_body.decode('utf-8')
    json_data = json.loads(k)
    global keyy
    keyy = json_data['key']
    
    key = json_data['key'] # 캡차 Key 값
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        print("캡차 이미지 저장")
        response_body = response.read()
        with open('D:/workspace_python/HELLOPYTHON/captcha/static/image/captcha.jpg', 'wb') as f:
            f.write(response_body)
            print(f.write(response_body))
    else:
        print("Error Code:" + rescode)
        
    return render_template("navercaptcha.html", captcha_image="image/captcha.jpg")  



@app.route("/captcha.check", methods=["POST"])
def captchacheck():
    nnn = request.form["nnn"]
    client_id = "EosLbjeD2Ad2CfIN_FAA"
    client_secret = "FlozGi2tze"
    code = "1"
    key = keyy
    value = nnn
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
    request1 = urllib.request.Request(url)
    request1.add_header("X-Naver-Client-Id",client_id)
    request1.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        body = response_body.decode('utf-8')
        json_data = json.loads(body)
        
        if json_data["result"]:
            result="성공"
        else:
            result="실패"
    else:
        print("Error Code:" + rescode)
        
    return render_template("success.html", result=result) 
    


    
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="80")