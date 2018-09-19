from flask import Flask, url_for
app= Flask(__name__) #create isntanc of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    return '<h1><i><center><a href="127.0.0.1:5000' + url_for('also_hello_world') + '"> welcome to page 1! </a></center></i></h1>'

@app.route("/page2")
def also_hello_world():
	return '<a href="127.0.0.1:5000' + url_for('another_hello_world') + '">i like to call this one, page 2!</a>'

@app.route("/page3")
def another_hello_world():
	print(__name__)
	return '<a href="127.0.0.1:5000">and this one? page 3!</a>'

if __name__ == "__main__":
    app.debug = True
    app.run()


