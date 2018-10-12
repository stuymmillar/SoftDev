import sqlite3
import csv

DB_FILE="entries.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def resetTable():
    try:
        c.execute("DROP TABLE entries")
        c.execute("CREATE TABLE entries(name TEXT, entry TEXT)")
    except:
        c.execute("CREATE TABLE entries(name TEXT, entry TEXT)")
    
def insertInto(name, entry):
    params = (name,entry)
    c.execute("INSERT INTO entries VALUES(?,?)", params)

def readFrom():
    c.execute("SELECT * FROM entries")
    print(c.fetchall())

resetTable()
insertInto('john', 'John is our first test entry')
readFrom()
    
db.commit()
db.close()
