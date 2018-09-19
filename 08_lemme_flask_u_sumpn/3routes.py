from flask import Flask
app= Flask(__name__) #create isntanc of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    return '<h1><i><center><a href="/page2"> welcome to page 1! </a></center></i></h1>'

@app.route("/page2")
def also_hello_world():
	return '<a href="/page3">i like to call this one, page 2!</a>'

@app.route("/page3")
def another_hello_world():
	print(__name__)
	return '<a href="/">and this one? page 3!</a>'

if __name__ == "__main__":
    app.debug = True
    app.run()


