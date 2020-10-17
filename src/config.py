import os

class Development(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://password:user_name@host_name/db_name'
    SECRET_KEY = "_5#y2LF4Q8zgg5345tg3gwff3^$34t3f34f4f34fxec]"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_RECIPIENTS = []

class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://password:user_name@host_name/db_name'
    SECRET_KEY = "_5#y2LF4Q8zgg5345tg3gwff3^$34t3f34f4f34fxec]"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_RECIPIENTS = []

app_config = {
    'development': Development,
    'production': Production,
}