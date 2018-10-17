from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import sqlite3

DB_FILE="blogger.db"

app = Flask(__name__)

app.secret_key = os.urandom(32)

#user = {"john" : "doe"}
errors = False

@app.route('/')
def render_test():
    if 'user' in session:
        username = session['user']
    else:
        return redirect("/login")
    #print(username)
    #try:
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #print(user)
    #print("SELECT title FROM blog where username='" + user + "';")
    c.execute("SELECT title FROM blog;")
    titles = c.fetchall()
    c.execute("SELECT body FROM blog;")
    bodies = c.fetchall()
    c.execute("SELECT post_id FROM blog;")
    ids = c.fetchall()
    c.execute("SELECT username FROM blog;")
    users= c.fetchall()
    db.commit()
    db.close()
    #print(bodies)
    length = len(titles)
    return render_template("index.html", username=username, titles=titles, bodies=bodies, ids=ids, length=length, users=users)
    '''except:
        flash("Big error.")
        return redirect("/")
    '''
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
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("SELECT password FROM login where username='" + str(u_name) + "';")
        password = c.fetchall()
        db.commit()
        db.close()
        #print(u_pass)
        #print(password)
        if u_pass != password[0][0]:
            flash("Incorrect password.")
            errors = True
    except:
        flash("Incorrect username or password.")
        errors = True
    if not errors:
        session['user'] = u_name
        flash("Success!")
        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    if 'user' not in session:
        return redirect("/login")
    session.pop('user')
    flash("Successfully logged out")
    return redirect("/login")

@app.route('/register')
def register():
    if 'user' in session:
        flash("You must log out to create a new account.")
        return redirect("/")
    return render_template("register.html")

@app.route('/makereg')
def makereg():
    if 'user' in session:
        flash("You must log out to create a new account.")
        return redirect("/")
    u_name = request.args.get("username")
    u_pass = request.args.get("password")
    if u_name == None or u_pass == None:
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username FROM login WHERE username='" + str(u_name) + "';")
    check_u = c.fetchall()
    #print(check_u)
    #print(u_name)
    if check_u != []:
        db.commit()
        db.close()
        flash("Username taken.")
        return redirect("/login")
    else:
        c.execute("INSERT INTO login VALUES('" + str(u_name) + "', '" + str(u_pass) + "');")
        db.commit()
        db.close()
        session['user'] = u_name
        flash("Account successfully created!")
        return redirect("/")

@app.route('/user/<user>')
def dispUser(user):
    if 'user' not in session:
        return redirect("/login")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        #print(user)
        #print("SELECT title FROM blog where username='" + user + "';")
        c.execute("SELECT title FROM blog where username='" + str(user) + "';")
        titles = c.fetchall()
        c.execute("SELECT body FROM blog where username='" + str(user) + "';")
        bodies = c.fetchall()
        c.execute("SELECT post_id FROM blog where username='" + str(user) + "';")
        ids = c.fetchall()
        db.commit()
        db.close()
        print(bodies)
        length = len(titles)
        return render_template("user.html", titles=titles, bodies=bodies, ids=ids, length=length, user=user)
    except:
        flash("Error, user does not exist.")
        return redirect("/")

@app.route('/mypage')
def myPage():
    if 'user' not in session:
        return redirect("/login")
    return redirect("/user/" + session['user'])
    
@app.route("/user/<user>/<post_id>")
def dispPost(user, post_id):
    if 'user' not in session:
        return redirect("/login")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        #print(user)
        c.execute("SELECT title FROM blog where username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        title = c.fetchall()
        c.execute("SELECT body FROM blog where username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        body = c.fetchall()
        c.execute("SELECT post_id FROM blog where username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        pid = c.fetchall()
        db.commit()
        db.close()
        #print(body)
        title = title[0][0]
        body = body[0][0]
        if session['user'] == user:
            print("logged in")
            this_user = True
        else:
            this_user = False
        return render_template("post.html", title=title, body=body, post_id=post_id, user=user, this_user=this_user)
    except:
        flash("Error, post does not exist.")
        return redirect("/")

@app.route("/edit/<user>/<post_id>")
def editEntry(user, post_id):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to edit other user's posts.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        #print(user)
        c.execute("SELECT body FROM blog where username='" + str(user) + "' AND post_id =" + str(post_id) + ";")
        body = c.fetchall()
        c.execute("SELECT title FROM blog where username='" + str(user) + "' AND post_id =" + str(post_id) + ";")
        title = c.fetchall()
        db.commit()
        db.close()
        #print(body)
        title = title[0][0]
        body = body[0][0]
        return render_template("edit.html", title=title, body=body, user=user, post_id=post_id)
    except:
        flash("Error, post does not exist.")
        return redirect("/")

@app.route("/doedit/<user>/<post_id>", methods=['POST','GET'])
def makeEdit(user, post_id):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/login")
    ntitle = request.form.get("ntitle")
    nbody = request.form.get("nbody")
    if nbody == None or ntitle == None:
        flash("You weren't supossed to be here.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        #print(entry)
        c.execute("UPDATE blog SET body='" + str(nbody) + "'  WHERE username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        c.execute("UPDATE blog SET title='" + str(ntitle) + "'  WHERE username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        db.commit()
        db.close()
        flash("Success! Post has been updated.")
        return redirect("/")
    except:
        flash("Error, post does not exist.")
        return redirect("/")

@app.route("/add")
def addStart():
    if 'user' not in session:
        flash("You need to be logged in to add entries.")
        return redirect("/")
    return render_template("add.html")

@app.route("/makeadd")
def addNew():
    if 'user' not in session:
        flash("You need to be logged in to add entries.")
        return redirect("/")
    user = session['user']
    title = request.args.get("title")
    nbody = request.args.get("nbody")
    if nbody == None or title == None:
        flash("The title and body of the entry must not be left blank.")
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    try:
        c.execute("SELECT post_id FROM blog WHERE username='" + str(user) + "';")
        post_id = c.fetchall()
        #print(post_id)
        #print(len(post_id[0]) - 1)
        post_id = (post_id[len(post_id) - 1][0] + 1)
        #print(post_id)
    except:
        post_id = 1
    c.execute("INSERT INTO blog VALUES('" + str(user) + "', '" + str(title) + "', '" + str(nbody) + "', " + str(post_id) + ");")
    db.commit()
    db.close()
    flash("Success! New post has been added.")
    return redirect("/user/" + str(user) + "/" + str(post_id))

@app.route("/search")
def findEntry():
    query = request.args.get("query")
    if query == None:
        flash("The user search field must not be left blank.")
        return redirect("/")
    return redirect("/user/" + str(query))

@app.route("/delete/<user>/<post_id>")
def delEntry(user, post_id):
    if 'user' not in session:
        flash("You need to be logged in to delete posts.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to delete other user's posts.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("DELETE FROM blog where username='" + str(user) + "' AND post_id=" + str(post_id) + ";")
        db.commit()
        db.close()
        flash("Success! Your post has been deleted.")
        return redirect("/")
    except:
        flash("Error, post does not exist.")
        return redirect("/")

    
if __name__ == '__main__':
    app.debug = True
    app.run()
