from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def search():
    return render_template("index.html")

@app.route('/book/<bookid>')
def displayBook(bookid):
    return render_template("reader.html", bookid=str(bookid))

if __name__ == '__main__':
    app.debug = True
    app.run()
