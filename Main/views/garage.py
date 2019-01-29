import cx_Oracle as co
from flask import redirect,url_for,Blueprint,Flask,request,render_template



garage = Blueprint('garage', 'garage', url_prefix='/garage')

connection = co.connect('nikhil/password')
cx = connection.cursor()
q1 = "insert into garage values(:2,:3,:4)"
q2 = "select * from garage M where M.gname = (:2)"
q3 = "select * from garage"


logindataa=False

@garage.route('/home',methods=['post','get'])
def homee():
    return render_template('home.html')
    

@garage.route('/', methods=['post','get'])
def home():
    return render_template("garage.html")

    

@garage.route('/insert', methods=['post'])
def insert():
    if request.form['matnum'] !='':
        matid = request.form['matnum']
        matename = request.form['matname']
        matcost = request.form['matcost']
        cx.execute(q1, (matid, matename, matcost))
        connection.commit()
        return render_template("garage.html" , value1 = "successfully inserted")
    else:
        return render_template("garage.html" , value1 = "please enter some value")

@garage.route('/all' , methods = ['POST','get'])
def all():
    q11 = cx.execute(q3)
    q = q11.fetchall()
    return render_template("garage.html" , out = q)
    
@garage.route('/get1', methods=['post','get'])
def get1():
    mateid = int(request.form['qid'])
    quer = cx.execute(q2,[mateid])
    que = quer.fetchall()
    return render_template("garage.html" , out = que)

























