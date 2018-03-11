import mysql.connector
from task import Task
import os
#import mysql.connector

t = Task()


def connect2Mysql():
    conn = mysql.connector.connect(
        user='root', password='as56210', database='flow4.0', use_unicode=True)
    cursor = conn.cursor()
    return conn, cursor


def readNotes():
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from flow_item where status = 0 Order By modify_time Desc')
    values = cursor.fetchall()

    cursor.execute('UPDATE temp set value = 0 where name = %s', ('has_new',))
    conn.commit()        

    cursor.close()
    conn.close()
    return values

def getNewStatus():
    conn, cursor = connect2Mysql()
    cursor.execute('SELECT * from temp where name = %s', ('has_new',))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


for x in range(20000):
    print('[第%d轮]' % x)
    notes = readNotes()
    length = len(notes)
    
    for i in range(length):
        status = getNewStatus()[0][2]
        print(status)
        if status == 1:
            break                            
        content = notes[i][2]
        if len(content) > 10:
            print('[第%d轮]' % x)
            print('    当前第%d段,一共%d段:' % (i, length))
            trimmedContent = content.strip()
            print(trimmedContent[:20])
            t.readTxtLine(trimmedContent)
