class Config(object):
    WXTOKEN = None
    WXAPPID = None
    WXSECRET= None
    AESKEY = None
    DEBUG = False

class ReleaseConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True

class DockerConfig(Config):
    DEBUG = False
