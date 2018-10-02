#Therapy Session -- Max Millar and Joshua Weiner
#SoftDev1 pd06
#k#14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/', methods=["POST", "GET"])
def render_test():
    if request.form.get("Log Out") != None:
        session.pop("john")
    if session.get("john") != None:
        return render_template("logged.html")
    else:
        return render_template("home.html")

@app.route('/user', methods=["POST", "GET"])
def show_user():
    errors = []
    u_pass = request.form.get("password")
    u_name = request.form.get("username")
    print(u_name + ":" + u_pass)
    if u_name != "john":
        errors.append("Wrong username!")
    if u_pass != "doe":
        errors.append("Wrong password!")
    if errors != []:
        return render_template("home.html", errors=errors)
    else:
        session[u_name] = u_pass
        return redirect(url_for("render_test"))

if __name__ == '__main__':
    app.debug = True
    app.run()
