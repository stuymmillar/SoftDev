#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def makeTable(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.get(0))
        '''
        command = "CREATE TABLE " + filename[:len(filename) - 4] + " ("
        for column in reader[0].keys: 
            command += column + " BLOB, "
        c.execute(command[len(command) - 1] + ")")
        for row in reader:
            command2 = "INSERT INTO " + filename[:len(filename) - 2] + " VALUES ("
            for coldata in row.keys:
                command2 += coldata + ", "
            c.execute(command2[len(command2) - 2] + ")")
'''
            
        #for row in reader:
            #print(row)
makeTable("peeps.csv")

            
#command = ""          #build SQL stmt, save as string
#c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


