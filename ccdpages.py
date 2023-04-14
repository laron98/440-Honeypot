from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape


app = Flask(__name__)

#connects to databases

#Home page
@app.route('/')
def index():
    return render_template('homepage.html')

#sign up page
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit')
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    
    if (password == cpassword):
        #To do: enter into data base
        return render_template('/signup/success')
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()

