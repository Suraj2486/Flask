from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="name can not be empty")])
    email = StringField("Email: ", validators=[DataRequired(message="email is required"), Email()])
    password = PasswordField("Password", validators=[DataRequired(message="length must be 6"), Length(min=6)])
    submit = SubmitField("Register")
    