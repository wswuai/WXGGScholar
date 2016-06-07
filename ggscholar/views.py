from entry import app

from flask import request

from service import wechat


@app.route("/wx", methods = ['GET','POST'])
def wx():
    if request.args.get("echostr") is not None:
        return request.args.get("echostr")
    else:
        return wechat.process(request.data)

@app.route("/")
def index():
    return "hello."
