from flask import Flask,render_template,redirect,request,url_for,flash
import psycopg2
import psycopg2.extras
import sys, os
import numpy as np
import pandas as pd
import pandas.io.sql as psql

app = Flask(__name__)
app.secret_key = "9340"

DB_HOST = "jelani.db.elephantsql.com"
DB_NAME = 'fvxjffat'
DB_USER = "fvxjffat"
DB_PASS = "YDdsW8gqyUa9zjvBCt1MIO5wCXoBohaC"

conn_string = "host="+ DB_HOST +" dbname="+ DB_NAME  +" user=" + DB_USER +" password="+DB_PASS
conn=psycopg2.connect(conn_string)
print("Connected!")

@app.route('/')
def home():
    cur = conn.cursor()
    s = "SELECT * FROM persons"
    cur.execute(s)
    list_student = cur.fetchall()
    return render_template('index.html',list_student=list_student)

# @app.route('/')
# def home():
#     # cur = conn.cursor()
#     # s = "SELECT * FROM person"
#     # cur.execute(s)
#     # list_student = cur.fetchall()
#     return render_template('index.html')


@app.route('/add_student',methods=['POST'])
def add_student():
    cur = conn.cursor()
    if request.method == 'POST':
        reg =  request.form['reg']
        fname = request.form['fname']
        lname = request.form['lname']
        branch = request.form['branch']
        email = request.form['email']
        mobile = request.form['mobile']
        cur.execute("INSERT INTO persons VALUES(%s,%s,%s,%s,%s,%s)",(reg,fname,lname,branch,email,mobile))
        conn.commit()
        flash("Form value is saved")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')