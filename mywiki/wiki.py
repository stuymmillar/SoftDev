from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import sqlite3

DB_FILE="entries.db"

app = Flask(__name__)

app.secret_key = os.urandom(32)

user = {"john" : "doe"}
errors = False

#username = "notlogged"

@app.route('/')
def render_test():
    if 'user' in session:
        username = session['user']
    else:
        username = 'notlogged'
    #print(username)
    return render_template("index.html", username=username)
    
@app.route('/login')
def login():
    #print('user' in session)
    if 'user' in session:
        flash("You are already logged in.")
        return redirect("/")
    return render_template("login.html")
    
@app.route('/auth')
def authenticate():
    errors = False
    u_name = request.args.get("username")
    u_pass = request.args.get("password")
    if u_name not in user.keys():
        flash("Incorrect username")
        errors = True
    elif u_pass != user[u_name]:
        flash("Incorrect password")
        errors = True
    if not errors:
        session['user'] = u_name
        flash("Success!")
        return redirect(url_for('render_test'))
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user')
    flash("Successfully logged out")
    return redirect(url_for('render_test'))

@app.route('/entry/<entry>')
def dispEnt(entry):
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        print(entry)
        c.execute("SELECT entry FROM entries where name='" + entry + "';")
        body = c.fetchall()
        db.commit()
        db.close()
        #print(body)
        body = body[0][0]
        if 'user' in session:
            username = session['user']
        else:
            username = "notlogged"
        return render_template("entry.html", username=username, body=body, entry=entry)
    except:
        flash("Error, entry does not exist.")
        return redirect("/")

@app.route("/edit/<entry>")
def editEntry(entry):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        print(entry)
        c.execute("SELECT entry FROM entries where name='" + entry + "';")
        body = c.fetchall()
        db.commit()
        db.close()
        #print(body)
        body = body[0][0]
        #print(body)
        return render_template("edit.html", entry=entry, body=body)
    except:
        flash("Error, entry does not exist.")
        return redirect("/")

@app.route("/doedit/<entry>", methods=['POST','GET'])
def makeEdit(entry):
    nbody = request.form.get("nbody")
    if nbody == None:
        flash("You weren't supossed to be here.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        print(entry)
        c.execute("UPDATE entries SET entry='" + nbody + "'  WHERE name='" + entry + "';")
        db.commit()
        db.close()
        flash("Success! Entry " + entry + " has been updated.")
        return redirect("/")
    except:
        flash("Error, entry does not exist.")
        return redirect("/")

@app.route("/add")
def addStart():
    if 'user' not in session:
        flash("You need to be logged in to add entries.")
        return redirect("/")
    return render_template("add.html")

@app.route("/makeadd")
def addNew():
    entry = request.args.get("entry")
    nbody = request.args.get("nbody")
    if nbody == None:
        flash("The title and body of the entry must not be left blank.")
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    entry = entry.lower()
    c.execute("INSERT INTO entries VALUES('" + entry + "', '" + nbody + "');")
    db.commit()
    db.close()
    flash("Success! Entry " + entry + " has been added.")
    return redirect("/entry/" + entry)

@app.route("/search")
def findEntry():
    query = request.args.get("query")
    if query == None:
        flash("The entry search field must not be left blank.")
        return redirect("/")
    return redirect("/entry/" + query)

@app.route("/delete/<entry>")
def delEntry(entry):
    if 'user' not in session:
        flash("You need to be logged in to delete entries.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("DELETE FROM entries where name='" + entry + "';")
        db.commit()
        db.close()
        flash("Success! Entry " + entry + " has been deleted.")
        return redirect("/")
    except:
        flash("Error, entry does not exist.")
        return redirect("/")

    
if __name__ == '__main__':
    app.debug = True
    app.run()
