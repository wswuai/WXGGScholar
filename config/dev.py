class Config(object):
    DEBUG = False

class ReleaseConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True

class DockerConfig(Config):
    DEBUG = False
