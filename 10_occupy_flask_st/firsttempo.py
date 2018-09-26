# UnemploymentOffice - Brian Lee and Max Millar
# SoftDev1 pd6
# K#10 -- Jinja Tuning
# 2018-09-22
from flask import Flask, render_template
from util import randoccup #import functions from util

app = Flask(__name__)

@app.route('/') #page that links to occupations
def intro_page():
    return '''<h1> Welcome! </h1>
    <div> <a href="/occupations"> Click here for Occupations table. </a> </div> ''' 

csvDict = randoccup.makeCsvDict() #create dictionary of occupations and percentages

@app.route('/occupations/')
def render_test():
    return render_template("occ.html",
            keys = list(csvDict.keys()),#just the percentages
            jobs = csvDict, #the whole dictionary
            rando = randoccup.weight(csvDict))	#the random occupation

if __name__ == '__main__':
    app.debug = True
    app.run()
