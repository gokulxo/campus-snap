from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

DEPARTMENTS = ['IT', 'CSE', 'ECE', 'Mech', 'Civil', 'EEE']

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100))
    department = db.Column(db.String(50))
    caption = db.Column(db.String(200))
    image = db.Column(db.String(200))
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    dept_filter = request.args.get('dept', 'All')
    if dept_filter == 'All':
        posts = Post.query.order_by(Post.created_at.desc()).all()
    else:
        posts = Post.query.filter_by(department=dept_filter).order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts, departments=DEPARTMENTS, selected=dept_filter)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        student_name = request.form['student_name']
        department = request.form['department']
        caption = request.form['caption']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        new_post = Post(student_name=student_name, department=department, caption=caption, image=file.filename)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    return render_template('upload.html', departments=DEPARTMENTS)

@app.route('/like/<int:id>')
def like(id):
    post = Post.query.get(id)
    post.likes += 1
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)