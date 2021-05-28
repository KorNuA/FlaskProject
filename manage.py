from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
# Python2&Python3数据库相互转换
pymysql.install_as_MySQLdb()


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@127.0.0.1:3306/information23"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


@app.route("/index")
def index():
    return "Index"


if __name__ == '__main__':
    app.run()
