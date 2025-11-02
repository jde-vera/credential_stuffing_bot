from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, Regexp, EqualTo, DataRequired

def CommonPasswords(form,field):
    common_passwords = ['123456','password','123456789','12345678','12345','sunshine','qwerty','iloveyou','princess','admin']
    if field.data in common_passwords:
        raise ValidationError("your password cannot be a common password")

class LoginForm(FlaskForm):
    username = StringField("enter your username", validators=[Length(min=3,max=30),Regexp('^[A-Za-z]+$'),DataRequired()])
    password = PasswordField("enter your password")
    confirm_password = PasswordField("confirm your password", validators=[EqualTo('password', 'passwords must be the same'),CommonPasswords,DataRequired()])
    exit = SubmitField("exit")