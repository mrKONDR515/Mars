from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_a = StringField('id астронавта', validators=[DataRequired()])
    password_a = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_c = StringField('id капитана', validators=[DataRequired()])
    password_c = PasswordField('Пароль капитана', validators=[DataRequired()])
    enter = SubmitField('Доступ')
