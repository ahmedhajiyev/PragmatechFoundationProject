from PortfolioProject import app, os, db
from flask import render_template, redirect, request
from werkzeug.utils import secure_filename
from PortfolioProject.models import Blog, BlogCategory, About
from flask.helpers import url_for
from flask.templating import render_template_string




#ADMIN INTERFACE


@app.route('/admin-about-edit', methods=['GET', "POST"])
def about_edit():
    abouts = About.query.all()
    if request.method == 'POST':
        about= About(
            name=request.form['title'],
            brth_day=request.form['brth-day'],
            adress=request.form['adrss'],
            zip_code=request.form['zip-code'],
            email = request.form['my_email']
        )
        db.session.add(about)
        db.session.commit()

    return render_template('admin/about-edit.html', abouts=abouts)




@app.route('/admin-about')
def admin_about():
    about = About.query.all()
    return render_template('admin/about.html', about=about)


# @app.route("/admin-blog-edit/<int:id>", methods=['GET', "POST"])
# def about_edit(id):
#     abouts = Blog.query.get_or_404(id)
#     if request.method == 'POST':
#         about_edit.name = request.form['title']
#         about_edit.brth_day = request.form['short-desc']
#         blog.description = request.form['description']
#         blog.image = filename
#         blog.category = request.form['category']
#         db.session.commit()
#         return redirect(url_for('blog_list'))
#     return render_template('admin/blog-edit.html', abouts=abouts)








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
        file.save(os.path.join(app.config['UPLOAD__FOLDER'], filename))
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
        file.save(os.path.join(app.config['UPLOAD__FOLDER'], filename))
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
    return render_template('blog.html/', blog=blog)


@app.route('/about')
def about():
    about = About.query.all()
    return render_template('index.html/', about=about)
    