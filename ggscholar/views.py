from entry import app

from flask import request

from service import wechat


@app.route("/", methods = ['GET','POST'])
def index():
    if request.args.get("echostr") is not None:
        return request.args.get("echostr")
    else:
        return wechat.process(request.data)
