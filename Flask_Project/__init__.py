from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app=Flask(__name__)

app.config['SECRET_KEY']='b4c8445552d18da562fa8da3a37df5c4'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'



db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'

from Flask_Project import routes
