from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from app.models import Person

class Registration(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Retype password", validators=[DataRequired(), EqualTo('password', message="Passwords must be the same")])
    submit = SubmitField("register")

    def validate_username(self, username):
        user = Person.query.filter_by(name = username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username")

    def validate_email(self, email):
        email = Person.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError("Please use a different email")


class LoginForm(FlaskForm):
    email = StringField("Email Please")
    password = PasswordField("Password please")
    submit = SubmitField("Hit me")

class Details(FlaskForm):
    name = StringField("Name Please")
    age = StringField("Age Please")
    profession = StringField("Profession Please")
    submit = SubmitField("Hit me")
