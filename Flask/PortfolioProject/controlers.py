import re
from PortfolioProject import app, os, db
from flask import render_template, redirect, request
from werkzeug.utils import secure_filename
from PortfolioProject.models import Blog, BlogCategory, About, Comment, Resume, Home, Messages
from flask.helpers import url_for
from flask.templating import render_template_string
from PortfolioProject.forms import AboutForm, CommentForm, MessagesForm




#ADMIN INTERFACE
@app.route('/admin')
def admin_panel():
    return render_template('admin/base.html/')


@app.route('/admin/home-add', methods=['GET', "POST"])
def home_add():
    homes = Home.query.all()
    if request.method == 'POST':
        file =request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD__FOLDER'], filename))
        home = Home(
            title=request.form['title'],
            description=request.form['description'],
            short_description=request.form['short-desc'],
            image = filename
        )
        db.session.add(home)
        db.session.commit()
        return redirect(url_for('home_list'))
    return render_template('admin/home-add.html', homes=homes)

@app.route('/admin/home-list')
def home_list():
    homes = Home.query.all()
    return render_template('admin/home-list.html', homes=homes)

@app.route("/admin/home-edit/<int:id>", methods=['GET', "POST"])
def home_edit(id):
    home = Home.query.get_or_404(id)
    if request.method == 'POST':
        file =request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD__FOLDER'], filename))
        home.title = request.form['title']
        home.description = request.form['description']
        home.short_description = request.form['short-desc']
        home.image = filename
        db.session.commit()
        return redirect(url_for('home_list'))
    return render_template('admin/home-edit.html', home=home)

@app.route("/admin/home-delete/<int:id>")
def home_delete(id):
    home = Home.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('home_list'))


@app.route('/admin/about-edit', methods=['GET', "POST"])
def about_edit():
    abouts = About.query.all()
    form = AboutForm()
    if form.validate_on_submit():   
        about = About(
            name=form.name.data,
            brth_day=form.brth_day.data,
            adress=form.adress.data,
            zip_code=form.zip_code.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(about)
        db.session.commit()
        return redirect(url_for('admin_about'))

    return render_template('admin/about-edit.html', abouts=abouts, form=form)




@app.route('/admin/about', methods=['GET', 'POST'])
def admin_about():
    abouts = About.query.all()[-1:]
    return render_template('admin/about.html', abouts=abouts)

# @app.route("/admin/about-edit/<int:id>", methods=['GET', "POST"])
# def about_edit(id):
#     abouts = About.query.all(id)
#     form = AboutForm()
#     if form.validate_on_submit():   
#         about = About(
#             name=form.name.data,
#             brth_day=form.brth_day.data,
#             adress=form.adress.data,
#             zip_code=form.zip_code.data,
#             email=form.email.data,
#             phone=form.phone.data
#         )
#         db.session.add(about)
#         db.session.commit()
#         return redirect(url_for('admin_about'))
#     return render_template('admin/about-edit.html', abouts=abouts, form=form)


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


@app.route('/admin/resume-list')
def resume_list():
    resumes = Resume.query.all()
    return render_template('admin/resume-list.html', resumes=resumes)

@app.route('/admin/resume-add', methods=['GET', "POST"])
def resume_add():
    resume = Resume.query.all()
    if request.method == 'POST':
        res = Resume(
            date=request.form['date'],
            degree=request.form['degree'],
            company_name = request.form['company-name'],
            description=request.form['description']
        )
        db.session.add(res)
        db.session.commit()
        return redirect(url_for('resume_list'))
    return render_template('admin/resume-add.html', resume=resume)

@app.route("/admin/resume-edit/<int:id>", methods=['GET', "POST"])
def resume_edit(id):
    resume = Resume.query.get_or_404(id)
    resumes = Resume.query.all()
    if request.method == 'POST':
        resume.date = request.form['date']
        resume.degree = request.form['degree']
        resume.company_name = request.form['company-name']
        resume.description = request.form['description']
        db.session.commit()
        return redirect(url_for('resume_list'))
    return render_template('admin/resume-edit.html', resumes=resumes)

@app.route("/admin/resume-delete/<int:id>")
def resume_delete(id):
    resume = Resume.query.get_or_404(id)
    db.session.delete(resume)
    db.session.commit()
    return redirect(url_for('resume_list'))



@app.route('/admin/blog-list')
def blog_list():
    blogs = Blog.query.all()
    return render_template('admin/blog-list.html', blogs=blogs)



@app.route('/admin/blog-add', methods=['GET', "POST"])
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

@app.route("/admin/blog-edit/<int:id>", methods=['GET', "POST"])
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


@app.route("/admin/blog-delete/<int:id>")
def blog_delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog_list'))


@app.route("/admin/messages")
def messages():
    messages = Messages.query.all()
    return render_template('admin/messages.html', messages=messages)

@app.route("/admin/messages/<int:id>")
def messages_delete(id):
    messages = Messages.query.get_or_404(id)
    db.session.delete(messages)
    db.session.commit()
    return redirect(url_for('messages'))

@app.route("/admin/comments")
def comments():
    comments = Comment.query.all()
    return render_template('admin/comments.html', comments=comments)

@app.route("/admin/comments/<int:id>")
def comments_delete(id):
    comments = Comment.query.get_or_404(id)
    db.session.delete(comments)
    db.session.commit()
    return redirect(url_for('comments'))

#USER INTERFACE ROUTES
@app.route('/', methods=["GET", "POST"])
def main_page():
    blogs = Blog.query.all()[-3:]
    about = About.query.filter_by().first()
    resume = Resume.query.all()[-6:]
    home = Home.query.all()
    form = MessagesForm()
    if form.validate_on_submit():
        messages = Messages(user_name=form.name.data, email=form.email.data, content=form.content.data, subject=form.subject.data)
        db.session.add(messages)
        db.session.commit()
        return redirect(url_for('main_page',messages=messages))
    return render_template('index.html/',  blogs=blogs,about=about, resume=resume,  home=home, form=form)





@app.route('/blog-list')
def user_blog_list():
    blogs = Blog.query.all()[-3:]
    about = About.query.filter_by().first()
    home = Home.query.all()
    return render_template('index.html/', blogs=blogs,about=about)

@app.route('/single-blog/<int:id>' , methods=['GET','POST'])
def single_blog(id):
    blog = Blog.query.get_or_404(id)
    blogs = Blog.query.all()[-3:]
    blogcategories = BlogCategory.query.all()
    comments = blog.comments
    comment_count = Comment.query.filter(Comment.blog_id == blog.id).count()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(user_name=form.name.data, email=form.email.data, content=form.content.data, host=blog)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('single_blog',id=blog.id , comment=comment, comments=comments, comment_count=comment_count))
    return render_template('blog.html/', blog=blog, blogs=blogs, form=form , comments=comments, comment_count=comment_count, blogcategories=blogcategories)


@app.route('/categories')
def categories():

    return render_template('categories.html/')

@app.route('/about')
def about():
    about = About.query.filter_by(id='-1').first()
    blogs = Blog.query.all()[-3:]
   
    return render_template('index.html/', about=about, blogs=blogs)



    