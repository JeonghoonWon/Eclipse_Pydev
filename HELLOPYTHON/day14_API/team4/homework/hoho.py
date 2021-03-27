import json

from flask import Flask, render_template, request, redirect, session, escape, url_for, jsonify
import requests 


app = Flask(__name__,static_url_path="", static_folder="static")
app.secret_key = 'abcdefg'

@app.route("/pay", methods = ['POST']) 
def pay():
    url = "https://kapi.kakao.com"
    
    headers = {
        "Authorization": "KakaoAK " + "0bde65fbf3b994384f8c2c9648b180e6", 
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
    params = {
        
        "cid": "TC0ONETIME",    # 테스트용 코드
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": "german",    # 유저 아이디
        "item_name": "초코파이",        # 구매 물품 이름
        "quantity": "1",                # 구매 물품 수량
        "total_amount": "2200",        # 구매 물품 가격
        "vat_amount":"200",
        "tax_free_amount": "0",         # 구매 물품 비과세
        "approval_url": "http://localhost:9998/success.html",
        "cancel_url": "http://localhost:9998/cancle.html",
        "fail_url": "http://localhost/fail.html"
        }
    
    response = requests.post(url+"/v1/payment/ready", headers=headers, params=params)
    print("상태코드 : ", response)
    response = json.loads(response.text)
    print(response)
    session['tid'] = response['tid']
    result = '%s' % escape(session['tid'])
    print("result", result)
    print(response["next_redirect_pc_url"])
    #return jsonify(resp = response)
    return redirect(response["next_redirect_pc_url"])
    
    #return render_template('index2.html', result = result )





@app.route('/view', methods = ['POST']) 
def view(): 
    result = '%s' % escape(session['tid'])
    
    url = "https://kapi.kakao.com"
    headers = {
        "Authorization": "KakaoAK " + "0bde65fbf3b994384f8c2c9648b180e6", 
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
    params = {
        "cid": "TC0ONETIME",
        "tid" : result
        }
    response = requests.post(url+"/v1/payment/order", headers=headers, params=params)
    
    print("상태코드 : ", response)
    response = json.loads(response.text)
    print(response)
    
    return render_template('index2.html', result = result)



@app.route('/approve', methods = ['POST']) 
def view_2(): 
    result = '%s' % escape(session['tid'])
    pg_token = request.form['tid_code']
    print(result,"----",pg_token)
    
    url = "https://kapi.kakao.com"
    headers = {
        "Authorization": "KakaoAK " + "0bde65fbf3b994384f8c2c9648b180e6", 
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
    params = {
        "cid": "TC0ONETIME",
        "tid" : result,
        "partner_order_id":"1001" ,
        "partner_user_id":"german" ,
        "pg_token": pg_token
        
        }
    response = requests.post(url+"/v1/payment/approve", headers=headers, params=params)
    print("상태코드 : ", response)
    response = json.loads(response.text)
    print(response)
    
    return render_template('index2.html', result = result)






@app.route('/') 
def home():

    return render_template('index.html')


@app.route('/cancle', methods = ['POST']) 
def cancle():
    result = '%s' % escape(session['tid'])
    print("1",result)
    url = "https://kapi.kakao.com"
    headers = {
        "Authorization": "KakaoAK " + "0bde65fbf3b994384f8c2c9648b180e6", 
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
    params = {
        "cid": "TC0ONETIME",
        "tid" : result,
        "cancel_amount":"2200",
        "cancel_tax_free_amount":"0",
        "cancel_vat_amount":"200"
        }
    response = requests.post(url+"/v1/payment/cancel", headers=headers, params=params)
    
    print("상태코드 : ", response)
    response = json.loads(response.text)
    print(response)
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1",port="9998")