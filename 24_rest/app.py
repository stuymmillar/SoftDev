from flask import Flask, render_template
import json
import urllib2.request

app = Flask(__name__)

@app.route('/')
def render_test():
    data = json.loads((urllib2.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=h9chfP0S0Fxq5oKty7ve1o08M6EhA6dVRtkvroWK")).read().decode())
    return render_template("index.html", url=data["url"])

if __name__ == '__main__':
    app.debug = True
    app.run()
