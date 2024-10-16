import sqlite3 as sq
from tkinter import ttk
from tkinter import *
import datetime
import os

Admins = ["mttcode", "admin"]

def addItem():
    Item = Changes.get().lower().title()
    Qty = QtyChanges.get()
    if(Qty.isdigit):
        try:
            conn = sq.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                           (Item, Quantity)''')
            cursor.execute('SELECT * FROM inventory')
            rows = cursor.fetchall()
            for row in rows:
                if(row[0] == f'{Item}'):
                    sql_update_query = """UPDATE inventory SET Quantity = ? WHERE Item = ?"""
                    sql_search_query = """SELECT * FROM inventory WHERE Item = ?"""
                    cursor.execute(sql_search_query, (Item,))
                    record = cursor.fetchone()
                    inQty = int(record[1])
                    NewQty = inQty + Qty 
                    cursor.execute(sql_update_query, (NewQty, Item,))
                    conn.commit()
                    conn.close()
                    return
            cursor.execute(f"INSERT INTO inventory VALUES ('{Item}','{Qty}')")
        except sq.Error as e:
            print(e)


def removeItem():
    Item = Changes.get().lower().title()
    Qty = QtyChanges.get()
    if(Qty.isdigit):
        try:
            conn = sq.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM inventory')
            rows = cursor.fetchall()
            for row in rows:
                if(row[0] == f'{Item}'):
                    sql_update_query = """UPDATE inventory SET Quantity = ? WHERE Item = ?"""
                    sql_search_query = """SELECT * FROM inventory WHERE Item = ?"""
                    cursor.execute(sql_search_query, (Item,))
                    record = cursor.fetchone()
                    inQty = int(record[1])
                    NewQty = inQty - Qty 
                    cursor.execute(sql_update_query, (NewQty, Item,))
                    conn.commit()
                    conn.close()
                    return
        except sq.Error as e:
            print(e)

def openWindow(Name = ""):
    root.destroy()
    Shop = Tk()
    Shopfrm = ttk.Frame(Shop, padding=10)
    Shopfrm.grid()
    ttk.Label(Shopfrm, text="Shop").grid(column=0, row=0)  
    ttk.Label(Shopfrm, text="Inventory :").grid(column=0, row=1)
    global TextInventory
    TextInventory = ""
    TextInventory = TextInventory.rstrip()
    global InvLabel
    InvLabel = ttk.Label(Shopfrm, text="").grid(column=1, row=1)
    for Admin in Admins:
        if (Name == Admin.lower()): #Admin username here
            ttk.Label(Shopfrm, text="Admin").grid(column=1, row=0)
            ttk.Label(Shopfrm, text="Shop Inventory").grid(column=0, row=2) 
            global Changes 
            Changes = ttk.Entry(Shopfrm)
            Changes.grid(column=0, row=3)
            global QtyChanges
            QtyChanges = ttk.Entry(Shopfrm, "1")
            QtyChanges.grid(column=1, row=3)
            ttk.Button(Shopfrm, text="Add Item", command=addItem).grid(column=1, row=3)
            ttk.Button(Shopfrm, text="Remove Item", command=removeItem).grid(column=2, row=3)
    Shop.mainloop()

def login():
    User = Username.get().lower()
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
            openWindow(User)
        else:
            print('Incorrect Password')
        cursor.close()
    except sq.Error as e:
        print(e)

def signup():
    User = Username.get().lower()
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
        openWindow(User)
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
