from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from Flask_Project.models import User

class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	phone=StringField('Phone Number',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired()])
	c_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('SignUp')



class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	submit=SubmitField('Login')

class PostProblems(FlaskForm):
	ptitle=StringField('Title',validators=[DataRequired()])
	pcity=SelectField('City',choices = [('Hyderabad', 'Hyderabad'), 
      ('Chennai', 'Chennai'),('Mumbai','Mumbai'),('Pune','Pune')])
	psector = SelectField('Sector', choices = [('Education', 'Education'), 
      ('Garbage', 'Garbage'),('Roads','Roads'),('Health','Health')])
	pdesc=TextAreaField('Description',validators=[DataRequired()])
	submit=SubmitField('POST')

class SolutionForm(FlaskForm):
	stitle=StringField('Solution Title',validators=[DataRequired()])
	sdesc=TextAreaField('Description',validators=[DataRequired()])
	submit=SubmitField('Submit  Solution')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    

    



