import time
import mysql.connector


def connect2Mysql():
    conn = mysql.connector.connect(
        user='root', password='as56210', database='flow4.0', use_unicode=True)
    cursor = conn.cursor()
    return conn, cursor


def readNotes():
    conn, cursor = connect2Mysql()
    cursor.execute(
        'SELECT * from flow_item')
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
    if len(values) != 0:  # find none
        cursor.execute(
            'UPDATE flow_item set status = 1 where item_id = %s', (item_id,))
        conn.commit()
    cursor.close()
    conn.close()


def touchNote(item_id, content):
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item where item_id = %s', (item_id,))
    values = cursor.fetchall()

    now = time.time()
    if len(values) == 0:  # find none
        cursor.execute('INSERT into flow_item (content, item_id, modify_time) values (%s, %s, %s)', [
                       content, item_id, now])
        cursor.execute(
            'UPDATE temp set value = 1 where name = %s', ('has_new',))

    else:  # find one
        cursor.execute('UPDATE flow_item set content = %s, modify_time = %s where item_id = %s', [
                       content, now, item_id])
    # insert_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()


def getHeaderText():
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from temp where name = "headerText" ')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values[0]


def writeHeaderText(text):
    conn, cursor = connect2Mysql()
    cursor.execute('UPDATE temp set str = %s where name = "headerText" ', [text, ])
    conn.commit()
    cursor.close()
    conn.close()

