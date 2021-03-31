import sqlite3

def returnConnection():
    connection = sqlite3.connect("db.sqlite3")
    return connection