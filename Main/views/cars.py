import cx_Oracle as co
from flask import redirect,url_for,Blueprint,Flask,request,render_template



cars = Blueprint('cars', 'cars', url_prefix='/car')

connection = co.connect('nikhil/password')
cx = connection.cursor()
q1 = "insert into car values(:2,:3,:4,:5,:6,:7)"
q2 = "select * from car M where M.regesdno = (:2)"
q3 = "select * from car"
q4 = "update car set make=(:2), model=(:3), engine=(:4),fuel=(:5),noofpass=(:6) where regesdno=(:7)"
q5 = "delete from car where regesdno=(:2)"



@cars.route('/home',methods=['post','get'])
def homee():
    return render_template('home.html')
    

@cars.route('/', methods=['post','get'])
def home():
    return render_template("cars.html")

    

@cars.route('/insert', methods=['post'])
def insert():
    matid =request.form['make']
    matename = request.form['model']
    matcost = request.form['engine']
    matqual = request.form['fuel']
    supid = int(request.form['noofpass'])
    supid2 = int(request.form['regesdno'])
    cx.execute(q1, (matid, matename, matcost, matqual,supid,supid2))
    connection.commit()
    return render_template("cars.html" , value1 = "successfully inserted")

@cars.route('/all' , methods = ['POST','get'])
def all():
    q11 = cx.execute(q3)
    q = q11.fetchall()
    return render_template("cars.html" , out = q)
    
@cars.route('/get1', methods=['post','get'])
def get1():
    mateid = request.form['qid']
    quer = cx.execute(q2,[mateid])
    que = quer.fetchall()
    return render_template("cars.html" , out = que)


@cars.route('/update', methods=['post', 'get'])
def update():
    if request.method == 'POST':
        upid = int(request.form['upid'])
        upname = request.form['upname']
        upcost = request.form['upcost']
        upengine = request.form['upquan']
        upfuel = request.form['upfuel']
        uppass = intrequest.form['uppass']
        cx.execute(q4,(upname,upcost,upengine,upfuel,uppass,upid))
        connection.commit()
        q = cx.execute(q2,[upid])
        return render_template("cars.html" , out = q)


@cars.route('/delete', methods=['post','get'])
def delete():
    if request.method == 'POST':
        upid = int(request.form['regesdno'])
        cx.execute(q5,[upid])
        connection.commit()
        return render_template("cars.html" , value3="successfully deleted")
























