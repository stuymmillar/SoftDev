#Max Millar
#SoftDev1 pd06
#k25 -- Getting More REST
#2018-11-14

from flask import Flask, render_template
import json
from urllib import request

app = Flask(__name__)

@app.route('/')
def render_test():
    data = json.loads((request.urlopen("https://en.wikipedia.org/w/api.php?action=parse&page=Barack_Obama&format=json")).read())
    print(data)
    print("==================================================================")
    print(data["parse"]["text"]["*"])
    return render_template("index.html", text=data["parse"]["text"]["*"], title=data["parse"]["title"])

if __name__ == '__main__':
    app.debug = True
    app.run()
