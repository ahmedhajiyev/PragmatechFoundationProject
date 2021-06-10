from PortfolioProject import db
from datetime import datetime


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
