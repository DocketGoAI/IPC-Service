import pytest
import json
from flask import Flask
from src.res import Fetcher

@pytest.fixture
def client():
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
    
    return app.test_client()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"We're Building an API for IPC"

def test_ipc_fetch(client):
    response = client.get('/ipc')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), dict)

def test_section_fetch(client):
    for i in range(1, 512):
        response = client.get(f'/ipc/{i}')
        assert response.status_code == 200
        assert isinstance(json.loads(response.data), dict)
