from flask import Flask, redirect, render_template, request, url_for, send_from_directory 
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
import os

class user:
    def __init__(self, fname, lname, email, pword, db):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pword = pword
        self.db = db

app = Flask(__name__)

#connects to databases
sys.path.append('/home/ubuntu/440-Honeypot')
import passwordManager.py;

#Home page
@app.route('/')
def index():
    image_url = 'static\images\cclogo.png'
    return render_template('homepage.html', image_url=image_url)

#sign up page
@app.route('/signup')
def sign_up():
    image_url = 'static\images\cclogo.png'
    return render_template('signup.html', image_url=image_url)

#checks submitted data from users and if valid puts on database
@app.route('/signup/verify', methods=['GET','POST'])
def submit():
    newuser = user('', '', '', '', '')
    newuser.fname = request.form['fname']
    newuser.lname = request.form['lname']
    newuser.email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    
    if (password == cpassword):
        passwordManager.newUser(newuser.password,newuser.email,newuser.fname,newuser.lname)
        newuser.pword = password
        return redirect(url_for('signup/fail'))

    #if passwords don't match have user try again 
    return redirect(url_for('/submit/success'))

#If user enters incorrect data they are redirected to this page
@app.route('/signup/fail')
def sign_up_fail():
    image_url = 'static\images\cclogo.png'
    return render_template('signupfail.html', image_url=image_url)

@app.route('/signup/success')
def sign_up_success():
    image_url = 'static\images\cclogo.png'
    return render_template('signupsuccess.html', image_url=image_url)

#User login page
@app.route('/login')
def login():
    image_url = 'static\images\cclogo.png'
    return  render_template('login.html', image_url=image_url)

@app.route('/login/verify', methods=['GET', 'POST'])
def login_verf():
    email = request.form['email']
    password = request.form['password']    
    #if email exists on database
    if(passwordManager.checkEmail(email)):
        #verify credentials with database
        #if valid login
        if(passwordManager.loginInfo(email)==password):
            return redirect(url_for('/home'))
        else: 
            return redirect(url_for('login/fail'))
    else: 
        return redirect(url_for('/signup/verify'))
    
@app.route('/home')
def home():
    image_url = 'static\images\cclogo.png'
    passwordManager.getCards(userdb.email) #possibly update depending on how we store email
    #userdb = 
    return render_template('home.html', image_url=image_url) #, userdb=userdb) 

if __name__ == '__main__':
    app.run()
