from flask import Flask, redirect, render_template, request, url_for 
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
def sign_up():
    return render_template('signup.html')

#checks submitted data from users and if valid puts on database
@app.route('/signup/verify', methods=['GET','POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    
    if (password == cpassword):
        #To do: enter into data base
        return redirect(url_for('signup/fail'))

    #if passwords don't match have user try again 
    return redirect(url_for('/submit/success'))

#If user enters incorrect data they are redirected to this page
@app.route('/submit/fail')
def sign_up_fail():
    return render_template('signupfail.html')

#User login page
@app.route('/login')
def login():
    return  render_template('login.html')

@app.route('/login/verify', methods=['GET', 'POST'])
def login_verf():
    email = request.form['email']
    password = request.form['password']
    
    #if email exists on database
    if():
        #verify credentials with database
        #if valid login
        if():
            return redirect(url_for('/userhome'))
        else: 
            return redirect(url_for('login/fail'))
    else: 
        return redirect(url_for('/signup/verify'))
    

if __name__ == '__main__':
    app.run()


