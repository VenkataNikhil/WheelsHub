from flask import redirect,url_for,Blueprint,Flask,render_template,request
import cx_Oracle as co


q4 = "select pass from login where username=(:2)"
q5 = "insert into login values(:2,:3)"

log = Blueprint('log','log')

connection = co.connect('nikhil/password')
cx = connection.cursor()

@log.route('/')  
def loger():
    return render_template("login.html")

@log.route('/login',methods=['POST','GET'])
def login():
    user = request.form['user']
    password = str(request.form['pass'])
    a = cx.execute(q4,[user])
    b = a.fetchone()
    
    if b is None :
        return render_template('login.html', error="entered username/password incorrect")
    
    if password == str(b[0]):
#       return redirect(url_for("mat.materials",user1 = user))
        return render_template('home.html')
    else:
        return render_template('login.html', error="entered username/password incorrect")


@log.route('/newuser', methods=['POST'])
def newuser():
    return render_template("newuser.html")


@log.route('/into' ,methods=['POST','GET'] )
def into():
    u = str(request.form['user'])
    p = str(request.form['pass'])
    cx.execute(q5,(u,p))
    connection.commit()
#   return redirect(url_for("mat.materials",user1 = u))
    return render_template('home.html')