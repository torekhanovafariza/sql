import sqlite3 

a = sqlite3.connect("mydatabase.db")
malumat = a.cursor()
malumat.execute(''' 
CREATE TABLE IF NOT EXISTS kompyuterlar(
    nomi TEXT
    narxi TEXT
    xotira TEXT)
'''
)

malumat.execute(''' 
CREATE TABLE IF NOT EXISTS odamchalar(
    ism TEXT
    fami TEXT
    yosh TEXT
)'''
)

malumat.execute(''' 
CREATE TABLE IF NOT EXISTS hayvonlar(
    turi TEXT
    yashash joi TEXT
    oziqlanuvchi TEXT
    rangi TEXT
)'''
)

malumat.execute(''' 
CREATE TABLE IF NOT EXISTS uychalar(
    narhi TEXT
    shahar TEXT
    qishloq TEXT
)'''
)
