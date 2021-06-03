from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
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


# app对象
app = Flask(__name__)
app.config.from_object(Config)

# MySQL数据库对象
db = SQLAlchemy(app)
# Redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)


@app.route("/index")
def index():
    return "Index"


if __name__ == '__main__':
    app.run()
