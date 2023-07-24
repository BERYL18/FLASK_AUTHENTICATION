from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)




@app.route('/')
def home():
     return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
