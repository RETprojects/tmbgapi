import flask    # do `pip3 install flask` if it gives you trouble
from ShowsData import Shows

app = flask.Flask(__name__)     # define the flask app like this
app.config["DEBUG"] = True      # debug will print useful stuff out

@app.route('/Shows/<year>', methods=['GET']) # this is called a decorator. it has info on the name of the endpoint and supported http method.
def ShowsWrapper(year):                         # this will be your wrapper function. each path var (thing in square brackets) is an input to this.
    return str(Shows(year))

app.run()   # actually starts the flask server

# to make requests, try `curl 127.0.0.1:5000/endpoint1/2022/Remi` (replace it with the IP address and port that it gives you when you start it up)