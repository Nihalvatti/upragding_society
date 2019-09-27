from Flask_Project import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg')
    problems=db.relationship('Problem',backref='author',lazy=True)

    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
    
 
class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically\
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
    uname = db.Column(db.String(40), unique=False, nullable=False)
    problemName = db.Column(db.String(40), nullable=False)
    problemDesc = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    sector = db.Column(db.String(20), nullable=False)
    def __init__(self, userId , problemName, problemDesc, city, sector,uname):
        self.userId = userId
        self.problemName = problemName
        self.problemDesc = problemDesc
        self.city = city
        self.uname=uname
        # self.phone = phone
        self.sector = sector
 
class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically\
    problemID=db.Column(db.Integer)
    solutionTitle=db.Column(db.String(150))
    solutionDesc = db.Column(db.String(150), nullable=False)
    voteCount=db.Column(db.Integer)
 
    def __init__(self, problemID , solutionDesc, voteCount,solutionTitle):
        self.problemID = problemID
        self.solutionDesc = solutionDesc
        self.voteCount = voteCount
        self.solutionTitle=solutionTitle
