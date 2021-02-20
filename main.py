'''
Author: your name
Date: 2021-02-20 15:02:27
LastEditTime: 2021-02-20 16:51:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonAPI\main.py
'''
import json
from flask import *
import threading
from function import (
    SkyPic
)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 返回中文


@app.route("/", methods=["GET", "POST"])
def index():
    return "<h1 style='text-align:center'>鲸落云API 基于Python Flask</h1><p style='text-align:center'>项目地址:<a href='https://github.com/adminwhalefall/PythonAPI'>https://github.com/adminwhalefall/PythonAPI</a></p1>"


@app.route("/sky/<string:ty>/", methods=["GET", "POST"])
def sky(ty):
    print(ty)
    if ty == "json":
        # return json.dumps(SkyPic.skyJson(), ensure_ascii=False)
        return jsonify(SkyPic.skyJson())
    elif ty == "pic":
        return redirect(SkyPic.skyPic())
    else:
        return redirect("/sky/json/")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
