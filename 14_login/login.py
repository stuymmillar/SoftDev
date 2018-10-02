#Therapy Session - Max Millar and Joshua Weiner
#SoftDev1 pd6
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

user = {"john" : "doe"}
errors = []

@app.route('/')
def render_test():
    if 'user' in session:
        return render_template("index.html", username="john")
    else:
        return render_template("login.html")

@app.route('/auth')
def authenticate():
    errors = []
    # print(request.form)
    # print(request.args)
    u_name = request.args["username"]
    u_pass = request.args["password"]
    #print(u_name + ":username")
    #print(u_pass + ":password")
    if u_name not in user.keys():
        errors.append("Incorrect username")
    if u_pass != user["john"]:
        errors.append("Incorrect password")
    if errors == []:
        session['user'] = user
        return redirect(url_for('render_test'))
    else:
        return render_template("login.html", errors=errors)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('render_test'))

if __name__ == '__main__':
    app.debug = True
    app.run()
