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
    with open(filename, 'r') as csvfile: # open csv file
        reader = csv.DictReader(csvfile) #read it in as a set of dictionaries
        #print(reader.get(0))
        first = True #to only perform this on the first iteration
        for row in reader:
            if first:
                command = "CREATE TABLE " + filename[:len(filename) - 4] + " (" #initialize name of table and beginning of creation statement
                for column in row.keys(): 
                    command += "'" + column + "' BLOB, " #add each column in generically typed
                    #print(command[:len(command) - 2] + ")")
                c.execute(command[:len(command) - 2] + ")") #execute commmand
                first = False #make sure this section does not run again
            command2 = "INSERT INTO " + filename[:len(filename) - 4] + " VALUES (" #initialize insert statement with table name
            for coldata in row.keys():
                command2 += "'" + row[coldata] + "', " #add each column of data to statement
            c.execute(command2[:len(command2) - 2] + ")") #execute command

makeTable("peeps.csv")
makeTable("courses.csv") #run for both csv files
c.execute("SELECT * FROM peeps")
print(c.fetchall())
c.execute("SELECT * FROM courses")
print(c.fetchall()) #print data from each table


db.commit() #save changes
db.close()  #close database


