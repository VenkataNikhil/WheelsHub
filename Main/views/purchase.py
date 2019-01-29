from datetime import datetime
import cx_Oracle as co
from flask import redirect,url_for,Blueprint,Flask,request,render_template



pur = Blueprint('pur', 'pur', url_prefix='/purchase')

connection = co.connect('nikhil/password')
cx = connection.cursor()
q1 = "insert into purchase values(:2,:3,:4,:5,:6,:7,:8)"
q2 = "select * from purchase M where M.cid = (:2)"
q3 = "select * from purchase"



@pur.route('/home',methods=['post','get'])
def homee():
    return render_template('home.html')
    

@pur.route('/', methods=['post','get'])
def home():
    return render_template("purchase.html")

   

@pur.route('/insert', methods=['post'])
def insert():
    pd11=[]
    pd1 = request.form['pdate']
    pd11.append(pd1.split('/'))
    print(pd11)
    pd1 = int(pd11[0][2])+1
    pd2 = int(str(datetime.now()).split(' ')[0].split('-')[0])
    if pd1 > pd2:
        if request.form['rnum'] !='':
            cid = request.form['pdate']
            cname = int(request.form['rnum'])
            cph = request.form['comname']
            lic = request.form['credit']
            lic2 = request.form['lic']
            lic3 = request.form['carmodel']
            lic4 = int(request.form['price'])
            cx.execute(q1, (cid,cname,cph,lic,lic2,lic3,lic4))
            connection.commit()
            return render_template("purchase.html" , value1 = "Inserted Succesfully")
        else:
            return render_template("purchase.html" , value1 = "please enter some value")
    else:
        return render_template("purchase.html" , value1 = "please enter another car details as the car expired")

@pur.route('/all' , methods = ['POST','get'])
def all():
    q11 = cx.execute(q3)
    q = q11.fetchall()
    return render_template("purchase.html" , out = q)
    
@pur.route('/get1', methods=['post','get'])
def get1():
    cid = int(request.form['qid'])
    quer = cx.execute(q2,[cid])
    que = quer.fetchall()
    return render_template("purchase.html" , out = que)























