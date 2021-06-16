from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    brth_day = StringField('Birthday', validators=[DataRequired()])
    adress = StringField('Adress', validators=[DataRequired()])
    zip_code = StringField('Zipcode', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Update')

# class CommentForm(FlaskForm):
#     content = StringField('Content', validators=[DataRequired()], render_kw={"placeholder": "Type your comment..."})
#     submit = SubmitField('Submit')
