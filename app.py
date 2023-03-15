# import sys
# print(sys.path)
from flask import Flask, render_template, url_for, request, session, redirect, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'thisisasecretkey'
# db = SQLAlchemy(app)

# db.init_app(app)


database = {'Manager1': 'Manager@123'}
app.secret_key = "hello"


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(80), nullable=False)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = request.form['username']
    pwd = request.form['password']
    if name not in database:
        return render_template('home.html', info='Invalid User')
    else:
        if database[name] != pwd:
            return render_template('home.html', info='Invalid Password')
        else:
            session["name"] = name
            flash('Login Successfull.')
            return redirect(url_for("dashboard"))


@app.route('/dashboard')
def dashboard():
    # name = session.get['name']
    return render_template('check.html', username=session["name"])


@app.route('/logout')
def logout():
    session.pop("name", None)
    flash('Logged Out Successfull.')
    return redirect(url_for("home"))


# @app.route('/check', methods=['POST', 'GET'])
# def check():
#     return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)
