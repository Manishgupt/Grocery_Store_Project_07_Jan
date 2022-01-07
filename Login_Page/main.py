from enum import EnumMeta
import re
from flask import Flask,render_template,url_for,request,redirect,session
from flask.wrappers import Request
import os 
import mysql.connector

app = Flask(__name__)
app.secret_key=os.urandom(24) 

conn=mysql.connector.connect(host="remotemysql.com",user="91yKbjoVQb",password="hu2iwKd7wK",database="91yKbjoVQb")
cursor=conn.cursor()


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def about():
    return render_template("register.html")


@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@app.route('/showproducts')
def showproducts():
    return render_template('manage-product.html')

@app.route('/orders')
def orders():
    return render_template('order.html')

@app.route('/about')
def about1():
    return render_template('blogdescription.html')


@app.route("/login_validation",methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    query="""select * from `users` where `email` like '{}' And `password` like '{}'""".format(email,password)
    cursor.execute(query)
    user=cursor.fetchall()
    if(len(user)>0):
        session['user_id']=user[0][0]
        return redirect('/home')
    else:
        return redirect('/')
    
@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    query="""insert into `users` (`name`,`email`,`password`) values('{}','{}','{}')""".format(name,email,password)
    cursor.execute(query)
    conn.commit()

    cursor.execute("""select * from `users` where `email` like '{}' """.format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/home') 

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/forget')
def forget():
    return render_template("forgetpassword.html")


@app.route('/forgetpassword',methods=['POST'])
def forgetpassword():
    email=request.form.get('femail')
    password=request.form.get('fpassword')
    conform_pass=request.form.get('fconformpassword')

    if(password==conform_pass):
        query="""update `users` set `password`='{}' where `email`='{}'""".format(password,email)
        cursor.execute(query)
        conn.commit()
        return redirect('/')
    else:
        return render_template("forget.html")



if __name__ == '__main__':
    app.run(debug=True)
 