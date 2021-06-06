from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#ADMIN INTERFACE
@app.route('/admin-blog-list')
def blog_list():
    return render_template('admin/blog-list.html')

class Blog(db.model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('Category'), nullable=False)


if __name__ == '__main__':
    app.run(debug=True)