#!/usr/bin/python3.5 -tt
# -*- coding: utf-8 -*-
import sqlite3
import datetime


def connect(detail, car, email):
    conn = sqlite3.connect('base.db')
    dtime ='%s-%s-%s' % (datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    c = conn.cursor()
    #c.execute(""" drop TABLE sbase""")
    #c.execute("""CREATE TABLE sbase (ID INTEGER PRIMARY KEY   AUTOINCREMENT, detail VARCHAR NOT NULL, car VARCHAR NOT NULL, email VARCHAR UNIQUE, status VARCHAR DEFAULT waiting, date datetime)""")
    try:
        c.execute("""INSERT OR IGNORE INTO sbase (detail, car, email, status, date) VALUES (?, ?, ?, ?, ?)""", (detail, car, email, "waiting", dtime))
        print('DATABASE CONNECTION ESTABLISHED %s' % str(datetime.datetime.now()))
    except:
        print('INSERT DATA ERROR!!!\n')
    finally:
        conn.commit()
        c.close()