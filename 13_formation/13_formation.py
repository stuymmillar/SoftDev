#Max Millar
#SoftDev1 pd06
#k#13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_test():
    return render_template("temp.html")

@app.route('/user', methods=["POST", "GET"])
def show_user():
    return request.form["username"] + ", " + request.method + ". Hello!"

if __name__ == '__main__':
    app.debug = True
    app.run()
