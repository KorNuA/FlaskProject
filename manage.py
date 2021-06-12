from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import pymysql
# Python2&Python3数据库相互转换
pymysql.install_as_MySQLdb()


class Config:
    """自定义配置类"""
    DEBUG = True

    # MySQL配置
    SQLALCHEMY_DATABASE_URI = "mysql://root@127.0.0.1:3306/information23"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SECRET_KEY = "NGRIOIJWESKJNLZV;LBT"

    # 将flask.session的存储调整到redis数据库
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=1)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400


# app对象
app = Flask(__name__)
app.config.from_object(Config)

# MySQL数据库对象
db = SQLAlchemy(app)
# Redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

# CSRF保护机制
CSRFProtect(app)

# Session工具类
Session(app)


@app.route("/index")
def index():
    return "Index"


if __name__ == '__main__':
    app.run()
