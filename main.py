from flask import Flask, render_template, request, redirect, url_for, session

import mysql.connector

app=Flask(__name__)

con=mysql.connector.connect(host='localhost',user='root',password='',database='mydatabase')

cur=con.cursor()




@app.route('/home/', methods =['GET', 'POST'])

def home():
    if request.method=='POST':
        username = request.form['user']
        email=request.form['email']
        role=request.form['role']
        password = request.form['password']
        sql="insert into register_table(username,email,role,password) values(%s,%s,%s,%s)"
        cur.execute(sql,(username,email,role,password))
        con.commit()
        cur.close()
        con.close()
        return render_template('login.html')
    return render_template('home.html')

@app.route('/')
@app.route('/login/', methods =['GET', 'POST'])

def login():
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:

        username = request.form['user']
        password = request.form['password']
        sql="select * from register_table where username=%s and password =%s"
        cur.execute(sql,(username,password))
        exe=cur.fetchone()
        if exe:
            return '<h1>Welcome</h1>'
        else:
            return '<h1>Error</h1>'

    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)


