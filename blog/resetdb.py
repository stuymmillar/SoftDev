import sqlite3
import csv

DB_FILE="blogger.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def resetTable():
    try:
        c.execute("DROP TABLE blog")
        c.execute("DROP TABLE login")
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("CREATE TABLE blog(username TEXT, title TEXT, body TEXT, post_id INTEGER)")
        c.execute("INSERT INTO login VALUES('john', 'doe')")
        c.execute("INSERT INTO login VALUES('jane', 'doe')")
        c.execute("INSERT INTO blog VALUES('john', 'Test', 'TEST POST 1', 1)")
        c.execute("INSERT INTO blog VALUES('jane', 'mest', 'MEST POST 1', 1)")
    except:
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("CREATE TABLE blog(username TEXT, title TEXT, body TEXT, post_id INTEGER)")
        c.execute("INSERT INTO login VALUES('john', 'doe')")
        c.execute("INSERT INTO login VALUES('jane', 'doe')")
        c.execute("INSERT INTO blog VALUES('john', 'Test', 'TEST POST 1', 1)")
        c.execute("INSERT INTO blog VALUES('jane', 'mest', 'MEST POST 1', 1)")
        
def readFrom():
    c.execute("SELECT * FROM login")
    print(c.fetchall())
    c.execute("SELECT * FROM blog")
    print(c.fetchall())

resetTable()
readFrom()
    
db.commit()
db.close()
