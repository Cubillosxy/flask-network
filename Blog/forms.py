from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo


class BaseUserForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired, Email()]
    )

    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class RegistrationForm(BaseUserForm):

    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=2, max=20)],
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
    )


class LoginForm(BaseUserForm):
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
