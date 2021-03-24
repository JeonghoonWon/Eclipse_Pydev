from flask import Flask,render_template,  jsonify ,request
from day12.mydao import MyEmpDao

app = Flask(__name__,static_url_path="",static_folder='static')
@app.route("/") #welcome
@app.route("/emp")
def emp():
    list = MyEmpDao().getEmps()                           
    return render_template('emp.html',list=list)

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    print(data)
    sabun  = data['sabun']
    name   = data['name']
    dept   = data['dept']
    mobile = data['mobile']
    
    # sabun = request.form.get('sabun')
    # name = request.form.get('name')
    # dept = request.form.get('dept')
    # mobile = request.form.get('mobile')
    
    cnt = MyEmpDao().insEmp(sabun, name, dept, mobile)
    result = "fail"
    if cnt == 1:
        result = "success"
    return jsonify(result = result)

@app.route('/del.ajax', methods=['POST'])
def del_ajax():
    data = request.get_json()
    print(data)
    
    sabun = data['sabun']
    
    cnt = MyEmpDao().delEmp(sabun)
    result = "fail"
    if cnt == 1:
        result = "success"
    return jsonify(result = result)

@app.route('/mod.ajax', methods=['POST'])
def mod_ajax():
    data = request.get_json()
    print(data)
    sabun  = data['sabun']
    name   = data['name']
    dept   = data['dept']
    mobile = data['mobile']
    
    # sabun = request.form.get('sabun')
    # name = request.form.get('name')
    # dept = request.form.get('dept')
    # mobile = request.form.get('mobile')
    
    cnt = MyEmpDao().updEmp(sabun, name, dept, mobile)
    result = "fail"
    if cnt == 1:
        result = "success"
    return jsonify(result = result)



if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="80")