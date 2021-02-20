'''
Author: whalefall
Date: 2021-02-20 15:02:27
LastEditTime: 2021-02-20 20:38:32
Description: 一个基于flask的聚合api(能用就行)
'''
import json
from flask import *
import threading
# 禁用警告
import urllib3
urllib3.disable_warnings()
from function import (
    SkyPic, pzez, dy,xiaojiDict
)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 返回中文

# 主页


@app.route("/", methods=["GET", "POST"])
def index():
    return "<h1 style='text-align:center'>鲸落云API 基于Python Flask</h1><p style='text-align:center'>项目地址:<a href='https://github.com/adminwhalefall/PythonAPI'>https://github.com/adminwhalefall/PythonAPI</a></p1>"

# 光遇随机图


@app.route("/sky/<string:ty>/", methods=["GET", "POST"])
def sky(ty):
    if ty == "json":
        # return json.dumps(SkyPic.skyJson(), ensure_ascii=False)
        return jsonify(SkyPic.skyJson())
    elif ty == "pic":
        return redirect(SkyPic.skyPic())
    else:
        return redirect("/sky/json/")

# pzez查人系统


@app.route("/pzez/", methods=["GET", "POST"])
def checkPZEZ():
    if request.method == "GET":

        ty = request.args.get("type")  # 获取type
        pyname_real = request.args.get("pyname")  # 获取指定拼音缩写的值
        name_real = request.args.get("name")  # 获取真实名字
        born_real = request.args.get("born")  # 获取生日
        res = pzez.run(ty, pyname_real, name_real, born_real)
        return jsonify(res)

    elif request.method == "POST":
        ty = request.form["type"]
        pyname_real = request.form["pyname"]
        name_real = request.form["name"]
        born_real = request.form["born"]
        res = pzez.run(ty, pyname_real, name_real, born_real)
        return jsonify(res)
    else:
        return "只接受POST与GET请求"


# 抖音去水印
@app.route("/dy/", methods=["GET", "POST"])
def dyDelWm():
    if request.method == "GET":
        url = request.args.get("url")
        res = dy.run(url)
        return jsonify(res)
    elif request.method == "POST":
        url = request.form["url"]
        res = dy.run(url)
        return jsonify(res)
    else:
        return "只接受POST与GET请求"

# 小鸡词典查词
@app.route("/xiaoji/", methods=["GET", "POST"])
def xiaoji():
    if request.method == "GET":
        kw = request.args.get("kw")
        res = xiaojiDict.checkWord(kw)
        return jsonify(res)
    elif request.method == "POST":
        kw = request.form["kw"]
        res = dy.run(kw)
        return jsonify(res)
    else:
        return "只接受POST与GET请求"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
