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
    description = StringField('Description', validators=[DataRequired()])
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


    #  <div class="slider">
    #             <div class="main-hello">
    #                 <div class="main-text ">
    #                     <span class="main-text-hello">{{home.title}}</span>
    #                     <h1 class="main-text-about">{{home.description}}</h1>
    #                     <h2>{{home.short_description}}</h2>
    #                     <div class="button">
    #                         <a href="" class="hire-me">Hire Me</a>
    #                         <a href="" class="my-works">My Works</a>
    #                     </div>
    #                 </div>
    #                 <img src="static/uploads/{{home.image}}" alt="">
    #             </div>
    #         </div>