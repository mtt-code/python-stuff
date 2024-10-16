import sqlite3 as sq
from tkinter import ttk
from tkinter import *
import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import sys
from dotenv import load_dotenv
import random
import string

load_dotenv()

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
        if(not os.path.isfile("key.txt")):
            with open('key.txt', 'w') as fp:
                inkey=''
                for i in range(64):
                    inkey = inkey.join('"\"')
                    inkey = inkey.join([random.choice(string.ascii_letters.lower() + string.digits ) for n in range(3)])
                fp.write(inkey)
            print('Created')
        with open("key.txt", 'r') as f:
            key : bytes = f.read().encode("utf8")
            print(f'{key}')
            cipher = AES.new(key, AES.MODE_EAX)
            print('Got the cipher')
            rows = cursor.fetchall()
            for row in rows:
                if(row[0] == f'{User}'):
                    print("User already registered")
                    return
            cipherUser = cipher.encrypt_and_digest(User)
            cipherPass = cipher.encrypt_and_digest(Pass)
            nonce = cipher.nonce
            print(f'{User} = {cipherUser}, {Pass} = {cipherPass}')
            cursor.execute(f"INSERT INTO userinfo VALUES ('{cipherUser}','{cipherPass}')")
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
