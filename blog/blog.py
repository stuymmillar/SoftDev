from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import sqlite3

DB_FILE = "blogger.db"

app = Flask(__name__)

app.secret_key = os.urandom(32)

# user = {"john" : "doe"}
errors = False


@app.route('/')
def render_test():
    if 'user' in session:
        username = session['user']
    else:
        return redirect("/login")
    # print(username)
    # try:
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # print(user)
    # print("SELECT title FROM blog where username='" + user + "';")
    c.execute("SELECT blog_title FROM blog;")
    titles = c.fetchall()
    c.execute("SELECT description FROM blog;")
    descriptions = c.fetchall()
    c.execute("SELECT blog_id FROM blog;")
    ids = c.fetchall()
    c.execute("SELECT username FROM blog;")
    users = c.fetchall()
    db.commit()
    db.close()
    # print(bodies)
    length = len(descriptions)
    return render_template("index.html", username=username, titles=titles, descriptions=descriptions, ids=ids,
                           length=length, users=users)
    '''except:
        flash("Big error.")
        return redirect("/")
    '''


@app.route('/login')
def login():
    # print('user' in session)
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
        # print(u_pass)
        # print(password)
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
    # print(check_u)
    # print(u_name)
    if check_u != []:
        db.commit()
        db.close()
        flash("Username taken.")
        return redirect("/login")
    else:
        c.execute("INSERT INTO login VALUES('" + str(u_name).lower() + "', '" + str(u_pass).lower() + "');")
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
        # print(user)
        # print("SELECT title FROM blog where username='" + user + "';")
        c.execute("SELECT blog_title FROM blog where username='" + str(user) + "';")
        titles = c.fetchall()
        c.execute("SELECT description FROM blog where username='" + str(user) + "';")
        descriptions = c.fetchall()
        c.execute("SELECT blog_id FROM blog where username='" + str(user) + "';")
        ids = c.fetchall()
        db.commit()
        db.close()
        if titles == [] or descriptions == [] or ids == []:
            flash("Error, user does not exist.")
            return redirect("/")
        print(descriptions)
        length = len(descriptions)
        return render_template("user.html", titles=titles, descriptions=descriptions, ids=ids, length=length, user=user)
    except:
        flash("Error, user does not exist.")
        return redirect("/")


@app.route('/mypage')
def myPage():
    if 'user' not in session:
        return redirect("/login")
    return redirect("/user/" + session['user'])


@app.route("/user/<user>/<blog_id>")
def dispBlog(user, blog_id):
    if 'user' not in session:
        return redirect("/login")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # print(user)
        c.execute("SELECT blog_title FROM blog where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        title = c.fetchall()
        c.execute("SELECT description FROM blog where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        description = c.fetchall()
        c.execute("SELECT blog_id FROM blog where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        pid = c.fetchall()
        c.execute("SELECT post_title FROM post where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        titles = c.fetchall()
        c.execute("SELECT body FROM post where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        bodies = c.fetchall()
        c.execute("SELECT post_id FROM post where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        ids = c.fetchall()
        c.execute("SELECT timestamp FROM post where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        times = c.fetchall()
        db.commit()
        db.close()
        # print(description)
        title = title[0][0]
        description = description[0][0]
        length = len(titles)
        if session['user'] == user:
            print("logged in")
            this_user = True
        else:
            this_user = False
        return render_template("blog.html", title=title, description=description, blog_id=blog_id, user=user,
                           this_user=this_user, length=length, titles=titles, bodies=bodies, ids=ids, times=times)
    except:
        flash("Error, blog does not exist.")
        return redirect("/")


@app.route("/user/<user>/<blog_id>/<post_id>")
def dispPost(user, blog_id, post_id):
    if 'user' not in session:
        return redirect("/login")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # print(user)
        c.execute("SELECT post_title FROM post where username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        title = c.fetchall()
        c.execute("SELECT body FROM post where username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        body = c.fetchall()
        c.execute("SELECT timestamp FROM post where username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        time = c.fetchall()
        db.commit()
        db.close()
        # print(body)
        title = title[0][0]
        body = body[0][0]
        print(body)
        time = time[0][0]
        if session['user'] == user:
            print("logged in")
            this_user = True
        else:
            this_user = False
        return render_template("post.html", title=title, body=body, post_id=post_id, user=user, this_user=this_user, blog_id=blog_id, time=time)
    except:
        flash("Error, post does not exist.")
        return redirect("/")

@app.route("/edit/<user>/<blog_id>")
def editBlog(user, blog_id):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to edit other user's posts.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # print(user)
        c.execute("SELECT description FROM blog where username='" + str(user) + "' AND blog_id =" + str(blog_id) + ";")
        description = c.fetchall()
        c.execute("SELECT blog_title FROM blog where username='" + str(user) + "' AND blog_id =" + str(blog_id) + ";")
        title = c.fetchall()
        db.commit()
        db.close()
        # print(description)
        title = title[0][0]
        description = description[0][0]
        return render_template("editb.html", title=title, description=description, user=user, blog_id=blog_id)
    except:
        flash("Error, post does not exist.")
        return redirect("/")


@app.route("/doedit/<user>/<blog_id>", methods=['POST', 'GET'])
def makeEditBlog(user, blog_id):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/login")
    ncategory = request.form.get("ncategory")
    ntitle = request.form.get("ntitle")
    ndescription = request.form.get("ndescription")
    if ncategory == None or ndescription == None or ntitle == None:
        flash("You weren't supossed to be here.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # print(entry)
        c.execute(
            "UPDATE blog SET category='" + str(ncategory) + "'  WHERE username='" + str(user) + "' AND blog_id=" + str(
                blog_id) + ";")
        c.execute("UPDATE blog SET description='" + str(ndescription) + "'  WHERE username='" + str(
            user) + "' AND blog_id=" + str(blog_id) + ";")
        c.execute("UPDATE blog SET blog_title='" + str(ntitle) + "'  WHERE username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + ";")
        db.commit()
        db.close()
        flash("Success! Blog has been updated.")
        return redirect("/")
    except:
        flash("Error, blog does not exist.")
        return redirect("/")


@app.route("/editpost/<user>/<blog_id>/<post_id>")
def editPost(user, blog_id, post_id):
    if 'user' not in session:
        flash("You need to be logged in to edit.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to edit other user's posts.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        # print(user)
        c.execute("SELECT body FROM post where username='" + str(user) + "' AND blog_id =" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        body = c.fetchall()
        c.execute("SELECT post_title FROM post where username='" + str(user) + "' AND blog_id =" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        title = c.fetchall()
        db.commit()
        db.close()
        title = title[0][0]
        body = body[0][0]
        return render_template("editp.html", title=title, body=body, user=user, blog_id=blog_id, post_id=post_id)
    except:
        flash("Error, post does not exist.")
        return redirect("/")


@app.route("/doeditpost/<user>/<blog_id>/<post_id>", methods=['POST', 'GET'])
def makeEditPost(user, blog_id, post_id):
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
        # print(entry)
        c.execute("UPDATE post SET body='" + str(nbody) + "'  WHERE username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
        c.execute("UPDATE post SET post_title='" + str(ntitle) + "'  WHERE username='" + str(user) + "' AND blog_id=" + str(
            blog_id) + " AND post_id=" + str(post_id) + ";")
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
        flash("You need to be logged in to add blogs.")
        return redirect("/")
    return render_template("add.html")


@app.route("/makeadd")
def addNew():
    if 'user' not in session:
        flash("You need to be logged in to add blogs.")
        return redirect("/")
    user = session['user']
    category = request.args.get("category")
    title = request.args.get("title")
    ndescription = request.args.get("ndescription")
    if category == None or ndescription == None or title == None:
        flash("The blog must not be left blank.")
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    try:
        c.execute("SELECT blog_id FROM blog WHERE username='" + str(user) + "';")
        blog_id = c.fetchall()
        # print(blog_id)
        # print(len(blog_id[0]) - 1)
        blog_id = (blog_id[len(blog_id) - 1][0] + 1)
        # print(blog_id)
    except:
        blog_id = 1
    c.execute("INSERT INTO blog VALUES('" + str(user) + "', '" + str(category) + "', '" + str(title) + "', '" + str(
        ndescription) + "', " + str(blog_id) + ");")
    db.commit()
    db.close()
    flash("Success! New post has been added.")
    return redirect("/user/" + str(user) + "/" + str(blog_id))


@app.route("/addpost/<user>/<blog_id>")
def addStartPost(user, blog_id):
    if 'user' not in session:
        flash("You need to be logged in to add posts.")
        return redirect("/")
    return render_template("addp.html", user=user, blog_id=blog_id)


@app.route("/makeaddpost/<user>/<blog_id>")
def addNewPost(user, blog_id):
    if 'user' not in session:
        flash("You need to be logged in to add posts.")
        return redirect("/")
    user = session['user']
    title = request.args.get("title")
    nbody = request.args.get("nbody")
    if nbody == None or title == None:
        flash("The post must not be left blank.")
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    try:
        c.execute("SELECT post_id FROM post WHERE username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        post_id = c.fetchall()
        post_id = (post_id[len(post_id) - 1][0] + 1)
    except:
        post_id = 1
    c.execute("INSERT INTO post VALUES('" + str(user) + "', '" + str(title) + "', '" + str(
        nbody) + "', " + str(blog_id) + ", " + str(post_id) + ", " + "CURRENT_TIMESTAMP);")
    db.commit()
    db.close()
    flash("Success! New post has been added.")
    return redirect("/user/" + str(user) + "/" + str(blog_id) + "/" + str(post_id))


@app.route("/search")
def findEntry():
    query = request.args.get("query")
    if query == None:
        flash("The user search field must not be left blank.")
        return redirect("/")
    return redirect("/user/" + str(query))


@app.route("/delete/<user>/<blog_id>")
def delBlog(user, blog_id):
    if 'user' not in session:
        flash("You need to be logged in to delete blogs.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to delete other user's blogs.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("DELETE FROM blog where username='" + str(user) + "' AND blog_id=" + str(blog_id) + ";")
        c.execute("DELETE FROM post where username='" + str(user) + "' and blog_id=" + str(blog_id) + ";")
        db.commit()
        db.close()
        flash("Success! Your blog has been deleted.")
        return redirect("/")
    except:
        flash("Error, blog does not exist.")
        return redirect("/")


@app.route("/deletepost/<user>/<blog_id>/<post_id>")
def delPost(user, blog_id, post_id):
    if 'user' not in session:
        flash("You need to be logged in to delete posts.")
        return redirect("/login")
    if session['user'] != user:
        flash("You are not allowed to delete other user's posts.")
        return redirect("/")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute(
            "DELETE FROM post where username='" + str(user) + "' AND blog_id=" + str(blog_id) + " AND post_id=" + str(
                post_id) + ";")
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
