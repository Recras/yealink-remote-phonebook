import requests
from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route("/<recrasurl>")
def hello(recrasurl):
    if request.authorization is None:
        abort(401)

    try:
        resp = requests.get("https://{0}/api2.php/klanten".format(recrasurl), auth=(request.authorization['username'], request.authorization['password']))
        resp.raise_for_status()

        return render_template('phonebookdirectory.xml', klanten=resp.json())
    except requests.ConnectionError, e:
        abort(404)
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print("%s" % e )
        abort(500)

if __name__ == "__main__":
    app.debug= True
    app.run(host = "0.0.0.0")
