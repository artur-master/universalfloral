import os

class Development(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = ''

class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://password:user_name@host_name/db_name'
    # JWT_SECRET_KEY = ''

app_config = {
    'development': Development,
    'production': Production,
}