from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

conn = sqlite3.connect('cms.db', check_same_thread=False)

def dict_factory(cursos, row):
    d = {}
    for idx, col in enumerate(cursos.description):
        d[col[0]] = row[idx]
    return d

conn.row_factory = dict_factory

cur = conn.cursor()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')                   

if __name__ == '__main__':
    app.run()