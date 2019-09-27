
from flask import render_template, url_for, flash, redirect, request
from Flask_Project.forms import RegistrationForm,LoginForm,PostProblems,Solution
from Flask_Project.models import User,Problem,Solution
from Flask_Project import app,db,bcrypt
from sqlalchemy import desc
from flask_login import login_user, current_user, logout_user, login_required
import os
import smtplib



@app.route("/")
def hello():
	return "Hello World"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(name=form.username.data, email=form.email.data, password=hashed_password,phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)




@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('feed')) 
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			next_page=request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('feed'))
		else: 
			flash('Login unsuccessful ', 'Danger')
	return render_template('login.html',title='Login',form=form)



@app.route("/feed")
def feed():
    posts=Problem.query.all()
    return render_template('feed.html',title='feed',posts=posts)

@app.route("/post",methods=['GET', 'POST'])
@login_required
def post():
	form=PostProblems()
	if form.validate_on_submit():
		user=User.query.filter(User.id==current_user.id).first()
		usname=user.name
		post=Problem(problemName=form.ptitle.data,problemDesc=form.pdesc.data,city=form.pcity.data,sector=form.psector.data,uname=usname,userId=current_user.id)
		db.session.add(post)
		db.session.commit()
 
		EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
		EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
		with smtplib.SMTP('smtp.gmail.com',587) as smtp :
		    	smtp.ehlo()
		    	smtp.starttls()
		    	smtp.ehlo()
		 
		    	smtp.login('harshavardhan45123@gmail.com','sweethome2')
		    	subject = form.ptitle.data+'-Upgrading Society'
		    	body ='Title- '+form.ptitle.data+'\nCity- '+form.pcity.data+'\nSector- '+form.psector.data+'\nDescription- '+form.pdesc.data+'\n\nPosted by\n'+usname
		 
		    	msg = f'Subject: {subject}\n\n {body}'
	    		smtp.sendmail('harshavardhan45123@gmail.com','nitinvatti@gmail.com',msg)

		flash('Your post has beem created','success')
		return redirect(url_for('feed')) 
	return render_template('post.html',title='post',form=form)

@app.route("/solution")
def solution():
	form=Solution()
	return render_template('solution.html',title='Solution',form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('feed'))


@app.route("/account", methods=['GET', 'POST'])
@login_required

def account():
	image_file =url_for('static', filename='profile_pics/'+ current_user.image_file)
	return render_template('account.html',title='account',image_file=image_file)




	







	
