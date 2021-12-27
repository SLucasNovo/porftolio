from flask import Flask, render_template, send_from_directory, send_file
from flask_bootstrap import Bootstrap
# from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('flask_key')
Bootstrap(app)
db = SQLAlchemy(app)
# Create admin user table
# Create connection with postresql
# Create table with id/project_name/img/summary
# query to add 2 or 3 projects
# create project.html

#
# class Project(db.Model):
#     __tablename__= 'projects'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False, unique=True)
#     img = db.Column(db.String(250), nullable=False)
#     summary = db.Column(db.String(250), nullable=False)
#
#
# class User(UserMixin,db.Model):
#     __table_name__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     hash_pw = db.Column(db.String(250), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download')
def send_cv():
    path = 'static/uploads/Resume Sandro Novo.pdf'
    return send_file(path, as_attachment=True)

#
#
# @app.route('/projects/<project_name>')
# def projects(project):
#
#     return render_template('project.html', project=project_name)



if __name__ == '__main__':
    app.run(debug=True)