from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, length, ValidationError
from app.models import User
from flask import flash



class TitleForm(FlaskForm):
    title = StringField('What should the title say?',
    validators=[DataRequired()])
    submit = SubmitField('Change Title')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = TextAreaField('Bio')
    url = StringField('Profile Pic URL')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(),
    EqualTo('password')])
    submit = SubmitField('Register')

    # setup validation methods to be checked when form is submitted
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in user')
            raise ValidationError('Use a different username/email.') # always make username and email ambigous to deter hacking

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in user')
            raise ValidationError('Use a different username/email.')


class ContactForm(FlaskForm):
    name = StringField('Full Name:')
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    message = TextAreaField('Message:', validators=[DataRequired(), length(max=500)])
    submit = SubmitField('Contact')

class PostForm(FlaskForm):
    tweet = StringField('What are you doing?', validators=[DataRequired(), length(max=140)])
    submit = SubmitField('Tweet')
