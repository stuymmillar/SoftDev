#Madison - Max Millar, Addison Huang


import sqlite3
import csv


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def findAvg(stuId):
    c.execute("SELECT mark FROM courses WHERE courses.id = '" + str(stuId) + "';")
    grades = c.fetchall()
    sum = 0
    for x in grades:
        sum += int(x[0])
    sum = int(sum / len(grades))
    return sum

def dispStudent(stuId):
    avg = findAvg(stuId)
    c.execute("SELECT name FROM peeps WHERE peeps.id = '" + str(stuId) + "';")
    name = c.fetchall()
    name = str(name[0])
    name = name[3:len(name) - 3]
    print("Id: " + str(stuId) + "|Name: " + name  + "|Average: " + str(avg)) 

def createTable():
    c.execute("CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)")
    for x in range(1,11):
        avg = findAvg(x)
        c.execute("INSERT INTO peeps_avg  VALUES(" + str(x) + ", " + str(avg) + ")")

def updateTable():
    c.execute("DROP TABLE peeps_avg")
    c.execute("CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)")
    for x in range(1,11):
        avg = findAvg(x)
        print("INSERT INTO peeps_avg(" + str(x) + ", " + str(avg) + ")")
        c.execute("INSERT INTO peeps_avg VALUES(" + str(x) + ", " + str(avg) + ")")

def addCourse(stu_id, course, grade):
    print("INSERT INTO courses VALUES('" + course + "', " + str(stu_id) + ", '" + str(grade) + ")")
    c.execute("INSERT INTO courses VALUES('" + course + "', '" + str(stu_id) + "', '" + str(grade) + "')")
    updateTable()
    
        
dispStudent(1)
#createTable()
updateTable()
addCourse(1, "ballroom", 1000)

db.commit()
db.close()
