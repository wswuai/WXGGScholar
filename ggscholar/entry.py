from flask import Flask
from flask.ext.cache import Cache
from gevent import monkey


monkey.patch_all()
print "monkey_patch applied"

app = Flask(__name__)
app.config.from_object('config.dev.TestingConfig')
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

import views
