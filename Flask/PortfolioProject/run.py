import re
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from flask.templating import render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


import flask_sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
#PHOTO UPLOAD
from werkzeug.utils import secure_filename, os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')
app.config['UPLOAD__FOLDER'] = UPLOAD_FOLDER

#ADMIN INTERFACE
@app.route('/admin-blog-list')
def blog_list():
    blogs = Blog.query.all()
    return render_template('admin/blog-list.html', blogs=blogs)

@app.route('/admin-blog-add', methods=['GET', "POST"])
def blog_add():
    categories = BlogCategory.query.all()
    if request.method == 'POST':
        file =request.files['file']
        filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            title=request.form['title'],
            description=request.form['description'],
            short_description=request.form['short-desc'],
            image = filename,
            category = request.form['category']
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-add.html', categories=categories)

@app.route("/admin-blog-edit/<int:id>", methods=['GET', "POST"])
def blog_edit(id):
    blog = Blog.query.get_or_404(id)
    categories = BlogCategory.query.all()
    if request.method == 'POST':
        file =request.files['file']
        filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog.title = request.form['title']
        blog.short_description = request.form['short-desc']
        blog.description = request.form['description']
        blog.image = filename
        blog.category = request.form['category']
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-edit.html', categories=categories)


@app.route("/admin-blog-delete/<int:id>")
def blog_delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog_list'))


#USER INTERFACE ROUTES

@app.route('/blog-list')
def user_blog_list():
    blogs = Blog.query.all()
    return render_template('index.html/', blogs=blogs)


@app.route('/single-blog/<int:id>')
def single_blog(id):
    blog = Blog.query.get_or_404(id)
    return render_template('blog.html', blog=blog)


class Blog(db.Model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    short_description = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)

    def __repr__(self):
        return f'Blog {self.title}'

    

class BlogCategory(db.Model):

    __tablename__ = 'blogcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.relationship(Blog, backref='blogcategories', lazy=True, cascade='all,delete')

    def __repr__(self):
        return f'Category {self.title}'



if __name__ == '__main__':
    app.run(debug=True)

