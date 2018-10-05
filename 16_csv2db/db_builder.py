# Taxes - Max Millar and Tim Marder
#SoftDev1 pd6
#K#16 -- No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def makeTable(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #print(reader.get(0))
        first = True
        for row in reader:
            if first:
                command = "CREATE TABLE " + filename[:len(filename) - 4] + " ("
                for column in row.keys(): 
                    command += "'" + column + "' BLOB, "
                    #print(command[:len(command) - 2] + ")")
                c.execute(command[:len(command) - 2] + ")")
                db.commit
                first = False
            command2 = "INSERT INTO " + filename[:len(filename) - 4] + " VALUES ("
            for coldata in row.keys():
                command2 += "'" + row[coldata] + "', "
            c.execute(command2[:len(command2) - 2] + ")")
            db.commit()
        #for row in reader:
            #print(row)

makeTable("peeps.csv")
makeTable("courses.csv")
c.execute("SELECT * FROM peeps")
print(c.fetchall())
c.execute("SELECT * FROM courses")
print(c.fetchall())

db.commit() #save changes
db.close()  #close database


