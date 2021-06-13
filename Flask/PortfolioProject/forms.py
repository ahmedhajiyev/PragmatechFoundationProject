from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    brth_day = StringField('birthday', validators=[DataRequired()])
    adress = StringField('adress', validators=[DataRequired()])
    zip_code = StringField('zipcode', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone', validators=[DataRequired()])
    submit = SubmitField('update')
