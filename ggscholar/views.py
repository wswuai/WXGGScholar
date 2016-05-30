from entry import app


@app.route("/")
def index():
    return "hello,world!"
