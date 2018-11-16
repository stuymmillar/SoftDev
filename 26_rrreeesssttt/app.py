from flask import Flask, render_template
import json
from urllib import request

app = Flask(__name__)

@app.route('/')
def render_test():
    data = json.loads((request.urlopen("https://catfact.ninja/fact")).read())
    data2 = json.loads((request.urlopen("https://api.spacexdata.com/v3/launches/latest")).read())
    data3 = json.loads((request.urlopen("https://dog.ceo/api/breeds/image/random")).read())
    return render_template("index.html", fact=data["fact"], number=data2["flight_number"], picture=data3["message"])

if __name__ == '__main__':
    app.debug = True
    app.run()
