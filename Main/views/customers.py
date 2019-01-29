import cx_Oracle as co
from flask import redirect,url_for,Blueprint,Flask,request,render_template



cus = Blueprint('cus', 'cus', url_prefix='/customer')

connection = co.connect('nikhil/password')
cx = connection.cursor()
q1 = "insert into customer values(:2,:3,:4,:5,:6)"
q2 = "select * from customer M where M.cid = (:2)"
q3 = "select * from customer"
q4 = "update customer set custname=(:2), custphn=(:3), custaddress=(:4), license=(:5) where cid=(:6)"
q5 = "delete from customer where cid=(:2)"



@cus.route('/home',methods=['post','get'])
def homee():
    return render_template('home.html')
    

@cus.route('/', methods=['post','get'])
def home():
    return render_template("customers.html")

@cus.route('/insert', methods=['post'])
def insert():
    if request.form['cid'] !='':
        cid = int(request.form['cid'])
        cname = request.form['cname']
        cph = int(request.form['cph'])
        cadd = request.form['cadd']
        lic = request.form['lic']
        cx.execute(q1, (cname,cph,cadd,lic,cid))
        connection.commit()
        return render_template("customers.html" , value1 = "successfully inserted")
    else:
        return render_template("customers.html" , value1 = "please enter some value")

@cus.route('/all' , methods = ['POST','get'])
def all():
    q11 = cx.execute(q3)
    q = q11.fetchall()
    return render_template("customers.html" , out = q)
    
@cus.route('/get1', methods=['post','get'])
def get1():
    cid = int(request.form['qid'])
    quer = cx.execute(q2,[cid])
    que = quer.fetchall()
    return render_template("customers.html" , out = que)


@cus.route('/update', methods=['post', 'get'])
def update():
    if request.method == 'POST':
        upid = int(request.form['upid'])
        upname = request.form['upname']
        upph = int(request.form['upph'])
        upadd = request.form['upadd']
        uplic = request.form['uplic']
        cx.execute(q4,(upname,upph,upadd,uplic,upid))
        connection.commit()
        q = cx.execute(q2,[upid])
        return render_template("customers.html" , out = q) 


@cus.route('/delete', methods=['post','get'])
def delete():
    if request.method == 'POST':
        upid = int(request.form['did'])
        cx.execute(q5,[upid])
        connection.commit()
        return render_template("customers.html" , value3="successfully deleted")
























