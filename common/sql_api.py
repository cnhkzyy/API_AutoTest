from flask import Flask, request, jsonify
from common.read_mysql import ReadMysql
import json
import decimal, datetime
import sys
import os

app = Flask(__name__)



@app.route("/query/one", methods=["post"])
def query_one():
    read_mysql = ReadMysql()
    query_sql = request.form.get("query_sql")
    one_data = read_mysql.select_one_data(query_sql)
    if one_data:
        return json.dumps({"code": "200", "result": str(one_data)})
    else:
        return json.dumps({"code": "404"})


app.run()
