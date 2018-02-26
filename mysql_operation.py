#!/usr/bin/env python
import mysql.connector


def connect2Mysql():
    conn = mysql.connector.connect(
        user='root', password='as56210', database='flow4.0', use_unicode=True)
    cursor = conn.cursor()
    return conn, cursor


def readNotes():
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


def readNotesById(item_id):
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item where item_id = %s', (item_id,))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


def deleteNote(item_id):
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item where item_id = %s', (item_id,))
    values = cursor.fetchall()
    if len(values) != 0: # find none
        cursor.execute('DELETE from flow_item where item_id = %s', (item_id,))
        conn.commit()        
    cursor.close()
    conn.close()


def touchNote(item_id, content):
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item where item_id = %s', (item_id,))
    values = cursor.fetchall()
    if len(values) == 0: # find none
        cursor.execute('INSERT into flow_item (content, item_id) values (%s, %s)', [content, item_id])
    else:# find one
        cursor.execute('UPDATE flow_item set content = %s where item_id = %s', [content, item_id])
    # insert_id = cursor.lastrowid
    conn.commit()        
    cursor.close()
    conn.close()


