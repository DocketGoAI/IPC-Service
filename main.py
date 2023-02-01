from flask import Flask
from src.res import Fetcher

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "We're Building an API for IPC"


@app.route(rule='/ipc', methods=['GET'])
def ipc_Fetch():
    f = Fetcher()
    return f.ret_all()



@app.route('/ipc/<section>', methods=['GET','POST'])
def section_Fetch(section):
    f = Fetcher()
    return f.ret_id(section)


app.run(debug=True, port=5000)
