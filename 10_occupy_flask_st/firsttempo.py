# UnemploymentOffice - Brian Lee and Max Millar
# SoftDev1 pd6
# K#10 -- Jinja Tuning
# 2018-09-22
from flask import Flask, render_template
from random import uniform
import csv

app = Flask(__name__)

csvDict = {}
list1 = []

with open("data/occupations.csv","r") as csvF:
    csvR = csv.reader(csvF) # reads the csv file
    for line in csvR:
        if line[0] != "Job Class" and line[0] != "Total":
             csvDict[float(line[1])] = line[0]
             list1.append(float(line[1])) # also add the percentage to the list

list1 = sorted(list1)


def weight(list1):
    total = 0.0 # this will represent the total percentage(99.8)
    for i in list1: # this adds the actual percentages
        total += i
    rand = uniform(0, total)
    index = 0
    temp = 0.0
    for i in list1:
        temp += i
        if temp >= rand:
            return(csvDict[list1[index]])
            break
        else:
            index += 1


@app.route('/occupations/')
def render_test():
    return render_template("occ.html",
            keys = list(csvDict.keys()),
            jobs = csvDict, rando = weight(list1))	

if __name__ == '__main__':
    app.debug = True
    app.run()
