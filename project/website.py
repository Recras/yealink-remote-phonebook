import requests
import sys
from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route("/<recrasurl>")
def hello(recrasurl):
    if request.authorization:
        credentials = (request.authorization['username'], request.authorization['password'])
    elif request.args.get('username') and request.args.get('password'):
        credentials = (request.args.get('username'), request.args.get('password'))
    else:
        abort(401)

    try:
        resp = requests.get("https://{0}/api2.php/contacten?page_size=1000&sort_by=id&sort_order=desc".format(recrasurl), auth=credentials)
        resp.raise_for_status()

        return render_template('phonebookdirectory.xml', klanten=resp.json())
    except (requests.ConnectionError, e):
        print("%s" % e )
        abort(404)
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print("%s" % e )
        abort(500)

if __name__ == "__main__":
    app.debug= True
    app.run(host = "0.0.0.0")
