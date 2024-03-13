from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_mail import *
from random import randint


app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='hoangquan02072002@gmail.com'
app.config['MAIL_PASSWORD']='afsttrhngukehkpx'                    
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import TaxiService,Order

@app.route('/')
def index():
  return render_template('index.html' )

@app.route('/informationdriver')
def informationdriver():
  infordrivers = TaxiService.query.all()
  return render_template('informationdriver.html',infordrivers=infordrivers)

@app.route('/OrderTaxi/<int:id>', methods=['GET'])
def order(id):
  infordriver = TaxiService.query.get_or_404(id)
  return render_template('order.html',infordriver=infordriver)


# @app.route('/OrderTaxi/authentication', methods=['POST'])
# def authentication():
#   cms=request.form.get('code')
#   cms_code= Order.query.filter_by(cmc_code=cms).first()
#   if cms_code:
#     return render_template('success.html',cms_code=cms_code)
#   else:
#     return render_template('404.html')

@app.route('/verify',methods=["POST"])
def verify():
    email=request.form['email']
    msg=Message(subject='OTP',sender='hoangquan02072002@gmail.com',recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('setup-2fa.html')
@app.route('/validate',methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return "<h3>Email verification succesfull</h3>"
    return "<h3>Please Try Again</h3>"

