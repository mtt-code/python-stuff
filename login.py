import sqlite3 as sq
from tkinter import ttk
from tkinter import *
import datetime
import os
import sys

def login():
    User = Username.get()
    Pass = Password.get()
    Timestamp = datetime.datetime.now()
    try:
        conn = sq.connect('users.db')
        cursor = conn.cursor()
        sql_select_query = """SELECT * FROM userinfo WHERE Username = ?"""
        cursor.execute(sql_select_query, (User,))
        record = cursor.fetchone()
        if(record[1] == Pass):
            print(record)
            print('Login Successfull !')
        else:
            print('Incorrect Password')
        cursor.close()
    except sq.Error as e:
        print(e)

def signup():
    User = Username.get()
    Pass = Password.get()
    try:
        conn = sq.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS userinfo
                       (Username, Password)''')
        cursor.execute('SELECT * FROM userinfo')
        rows = cursor.fetchall()
        for row in rows:
            if(row[0] == f'{User}'):
                print("User already registered")
                return
        cursor.execute(f"INSERT INTO userinfo VALUES ('{User}','{Pass}')")
        conn.commit()
        conn.close()
        print("Sign Up successfull")
    except sq.Error as e:
        print(e)
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Username : ").grid(column=0, row=0)
Username = ttk.Entry(frm)
Username.grid(column=1, row=0)
ttk.Label(frm, text="Password : ").grid(column=0, row=1)
Password = ttk.Entry(frm)
Password.grid(column=1, row=1)
ttk.Button(frm, text="Login", command=login).grid(column=0, row=2)
ttk.Button(frm, text="Sign Up", command=signup).grid(column=1, row=2)
Username = ttk.Entry(frm)
Username.grid(column=1, row=0)
root.mainloop()
