from flask import Flask, request, render_template,blueprints,views
import cx_Oracle as co

from views.login import log
from views.customers import cus
from views.cars import cars
from views.garage import garage
from views.purchase import pur

app = Flask(__name__)

app.register_blueprint(log)
app.register_blueprint(cus)
app.register_blueprint(cars)
app.register_blueprint(garage)
app.register_blueprint(pur)

if __name__=="__main__":
    app.run(debug=True)
