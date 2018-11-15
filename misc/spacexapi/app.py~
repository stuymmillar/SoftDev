from flask import Flask, render_template
import json
from urllib import request

app = Flask(__name__)

@app.route('/')
def render_test():
    data = json.loads((request.urlopen("https://catfact.ninja/fact")).read())
    return render_template("index.html", url=data["fact"])

if __name__ == '__main__':
    app.debug = True
    app.run()
