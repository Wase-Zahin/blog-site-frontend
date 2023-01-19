from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

conn = sqlite3.connect("cms.db", check_same_thread=False)

def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn.row_factory = dict_factory
cursor = conn.cursor()

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sql = "select id, title, description from blogs"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
        if res:
            return jsonify(res)
    return jsonify()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        sql = "select * from users where username = ? and password = ?"
        user = (username, password)
        cursor.execute(sql, user)
        res = cursor.fetchone()
        if res:
            userid = res['id']
            return jsonify({'status':'login_yes', 'id':userid})
    return jsonify({'status': 'login_no'})

app.run(debug=True, port=8000)
