from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from feedo.models import User, Feedback

star_icon = './static/star_icon.svg'

class JoinForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    agree_cont = SubmitField('Agree & Continue')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class SigninForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    sign_in = SubmitField('Sign In')

class SearchForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    search = SubmitField('Search')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No such user exist in our database...')

class RateForm(FlaskForm):
    xyz = TextAreaField("xyz")
    save = SubmitField('Save')

class FeedbackForm(FlaskForm):
    feedback = TextAreaField("feedback")
    send = SubmitField('Send')
    #reset = SubmitField('Reset')


# logically idher validate_username check karega ki use h ki nahi. and if not,
# vo udher hi error de dega. na ki search kare. user ka time waste ho fir pata laga ki
# essa to koi user h hi nahi.        












        
