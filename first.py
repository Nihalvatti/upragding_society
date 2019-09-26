from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm,PostProblems,Solution
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY']='b4c8445552d18da562fa8da3a37df5c4'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'



db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    createdAt = db.Column(db.String)
    updatedAt = db.Column(db.String)
    problems=db.relationship('Problem',backref='author',lazy=True)
 
    def __init__(self, name, email, password, phone, createdAt, updatedAt ):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.createdAt = createdAt
        self.updatedAt = updatedAt
 
class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically\
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
    problemName = db.Column(db.String(40), unique=True, nullable=False)
    problemDesc = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    # phone = db.Column(db.String(20), nullable=False)
    sector = db.Column(db.String(20), nullable=False)
    createdAt = db.Column(db.String)
    updatedAt = db.Column(db.String)
 
    def __init__(self, userId , problemName, problemDesc, city, sector, createdAt, updatedAt ):
        self.userId = userId
        self.problemName = problemName
        self.problemDesc = problemDesc
        self.city = city
        # self.phone = phone
        self.sector = sector
        self.createdAt = createdAt
        self.updatedAt = updatedAt
 
class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key increases automatically\
    problemID=db.Column(db.Integer)
    solutionDesc = db.Column(db.String(150), nullable=False)
    voteCount=db.Column(db.Integer)
    createdAt = db.Column(db.String)
    updatedAt = db.Column(db.String)
 
    def __init__(self, problemID , solutionDesc, voteCount,  createdAt, updatedAt ):
        self.problemID = problemID
        self.solutionDesc = solutionDesc
        self.voteCount = voteCount
        self.createdAt = createdAt
        self.updatedAt = updatedAt


@app.route("/")
def hello():
	return "Hello World"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'nihalvatti@gmail.com' and form.password.data == 'nihal':
			flash('You have been logged in!', 'success')
			return redirect(url_for('feed'))
		else :
			flash('Login unsuccessful ', 'Danger')
	return render_template('login.html',title='Login',form=form)



@app.route("/feed")
def feed():
	return render_template('feed.html',title='feed')

@app.route("/post")
def post():
	form=PostProblems()
	return render_template('post.html',title='post',form=form)

@app.route("/solution")
def solution():
	form=Solution()
	return render_template('solution.html',title='Solution',form=form)