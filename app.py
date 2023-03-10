from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqplite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db.init_app(app)
# database = {'Manager1': 'Manager@123'}


class User(db.Model, UserMixin):


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('home.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('home.html', info='Invalid Password')
        else:
            return render_template('dashboard.html', name=name1)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/check', methods=['POST', 'GET'])
def check():
    return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)
