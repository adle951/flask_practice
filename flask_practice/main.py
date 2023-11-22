from flask import Flask, request, redirect, render_template
import json

app = Flask(
    __name__,
    static_folder="static/picture",
    static_url_path="/www"
)
 
@app.route('/')
def hello_world():
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")

    else:
        return  redirect("/cn/")

@app.route("/en/")
def index_english():
    return json.dumps({
        "status" : "ok",
        "text" : "hello Leo"
        })

@app.route("/cn/")
def index_chinese():
    return json.dumps({
        "status" : "ok",
        "text" : "你好, Leo"
    })

@app.route("/tem")
def tem():
    return render_template("index", name="小明")

@app.route("/getsum")
def getsum():
    maxNumber = request.args.get("max", 100)
    maxNumber = int(maxNumber)
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    result = 0
    for i in range(minNumber, maxNumber + 1):
        result += i
    return f"total:{result}"

@app.route('/data')
def handleData():
    return 'My_data!'

@app.route('/user/<name>')
def handleName(name):
    return "Hi:" + name

app.run()