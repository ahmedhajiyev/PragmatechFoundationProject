from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , TextAreaField
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    brth_day = StringField('Birthday', validators=[DataRequired()])
    adress = StringField('Adress', validators=[DataRequired()])
    zip_code = StringField('Zipcode', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Update')

class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Type your comment..."})
    submit = SubmitField('POST COMMENT')
    name= StringField('User Name',  validators=[DataRequired()] , render_kw={"placeholder": "Your Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})

class MessagesForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Message"})
    submit = SubmitField('Submit')
    name= StringField('User Name',  validators=[DataRequired()] , render_kw={"placeholder": "Your Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    subject = StringField('Subject',  validators=[DataRequired()] , render_kw={"placeholder": "Subject"})