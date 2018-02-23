#!/usr/bin/env python
import mysql.connector


def connect2Mysql():
    conn = mysql.connector.connect(
        user='root', password='as56210', database='flow4.0', use_unicode=True)
    cursor = conn.cursor()
    return conn, cursor


def readNotes():
    conn, cursor = connect2Mysql()
    cursor.execute('select * from flow_item')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


def readNotesById(item_id):
    conn, cursor = connect2Mysql()
    cursor.execute('select * from flow_item where item_id = %s', (item_id,))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values
