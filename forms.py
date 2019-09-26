from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	c_password=PasswordField('C_Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('SignUp')



class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember_Me')
	submit=SubmitField('Login')

class PostProblems(FlaskForm):
	ptitle=StringField('Title',validators=[DataRequired()])
	pcity=SelectField('City',choices = [('Hyderabad', 'Hyderabad'), 
      ('Chennai', 'Chennai'),('Mumbai','Mumbai'),('Pune','Pune')])
	psector = SelectField('Sector', choices = [('Education', 'Education'), 
      ('Garbage', 'Garbage'),('Roads','Roads'),('Health','Health')])
	pdesc=TextAreaField('Description',validators=[DataRequired()])
	submit=SubmitField('POST')

class Solution(FlaskForm):
	stitle=StringField('Solution Title',validators=[DataRequired()])
	sdesc=TextAreaField('Description',validators=[DataRequired()])
	submit=SubmitField('Submit  Solution')



