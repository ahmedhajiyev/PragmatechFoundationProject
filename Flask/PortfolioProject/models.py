from PortfolioProject import db
from datetime import datetime


class Home(db.Model):

    __tablename__ = 'home'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(100))
    image = db.Column(db.String(20), default='uploads/default.jpeg')

    def __repr__(self):
        return f'Home {self.title}'



class About(db.Model):

    __tablename__= 'about'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brth_day = db.Column(db.Integer, nullable=False)
    adress = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'About {self.name}'



class Blog(db.Model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    short_description = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)
    comments = db.relationship('Comment', backref='host', lazy=True)

    def __repr__(self):
        return f'Blog {self.title}'

    

class BlogCategory(db.Model):

    __tablename__ = 'blogcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.relationship(Blog, backref='blogcategories', lazy=True, cascade='all,delete')

    def __repr__(self):
        return f'Category {self.title}'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_writed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content})"

class Resume(db.Model):

    __tablename__ = 'resume'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Blog {self.date}'


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_writed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Messages('{self.content})"