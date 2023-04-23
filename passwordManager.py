#Python Password Stuff
import sqlite3
import datetime
import random 
import string 
import ccard
import names
conn = sqlite3.connect('pythonDB.db')

c = conn.cursor()
def databaseMake():
	c.execute("""CREATE TABLE IF NOT EXISTS USER (
    		Password REAL,
    		Username TEXT,
    		PRIMARY KEY (Username))""")
	c.execute("""CREATE TABLE IF NOT EXISTS CARD (
        	Username TEXT, 
        	Company TEXT, 
        	Fname TEXT, 
        	Lname TEXT, 
        	Number REAL, 
        	Month REAL, 
        	Year REAL, 
        	CVV REAL, 
        	PRIMARY KEY(Number), 
        	FOREIGN KEY(Username) 
        	REFERENCES USER(Username))""")
	conn.commit();
def loginInfo(username):
	c.execute("""SELECT * FROM USER WHERE Username=?""",(username,))
	userinfo=cursor.fetchall()
	
	return userinfo[0]
def getCards(username):
    c.execute("""SELECT * FROM CARD WHERE Email=?""",(Email))
    cards=cursor.fetchall()
    rval=""
    for card in cards:
         card_str=""
         for element in card:
              card_str+=element+", "
         card_str+="\n"
    rval=rval[:-2]
    return rval


def newUser(password,username):
    password = hash(password)
    c.execute("""INSERT INTO USER (Password, Username) VALUES(?, ?)""",
													(password, username))
 
    conn.commit()
def populate():
    for i in range(1000):
        fname=names.get_first_name()
        lname=names.get_last_name()
        month=random.randint(1,12)
	c_Year=datetime.datetime.now().year
        year=random.randint(c_year+1,c_year+8)
        CVV=random.randint(100,999)
        cmpnum=random.randint(1,3)
        company=""
        cardnum=0
        if(cmpnum==1):
            company="discover"
            cardnum=ccard.discover()
        if(cmpnum==2):
            company="visa"
            cardnum=ccard.visa()
        if(cmpnum==3):
            company="mastercard"
            cardnum=ccard.mastercard()
        password=random.choices(string.ascii_letters, k=8)
        c.execute("INSERT INTO USER (Password, Username) VALUES(?, ?)",
													(password, name))
        c.execute("""INSERT INTO CARD (
            Username, 
            Company, 
            Fname, 
            Lname, 
            Number, 
            Month, 
            Year, 
            CVV) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",(fname+lname, ,fname,lname,arr[2],month,year,CVV)) 
    conn.commit()    

