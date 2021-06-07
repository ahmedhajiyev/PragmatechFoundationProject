from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import flask_sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#ADMIN INTERFACE
@app.route('/admin-blog-list')
def blog_list():
    return render_template('admin/blog-list.html')

class Blog(db.Model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    short_descrition = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)

    def __repr__(self):
        return f'Blog {self.title}'

    def __init__(self, title, date_posted, image, category):
        self.title = title
        self.date_posted = date_posted
        self.image = image
        self.category = category

class BlogCategory(db.Model):

    __tablename__ = 'blogcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.relationship(Blog, backref='blogcategories', lazy=True, cascade='all,delete')

    def __repr__(self):
        return f'Blog {self.title}'

if __name__ == '__main__':
    app.run(debug=True)