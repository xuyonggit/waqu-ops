import os
import redis
from flask import Flask
from App.user_views import user_blueprint
from App.models import db
from flask import url_for, redirect, session
from App.views import main
from App.tools_views import tools


def create_app():
    # 定义系统路径的变量
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # 定义静态文件的路径
    static_dir = os.path.join(BASE_DIR, 'static')
    # 定义模板文件的路径
    templates_dir = os.path.join(BASE_DIR, 'templates')
    # 初始化app 和manage.py文件关联
    app = Flask(__name__,
        static_folder=static_dir,
        template_folder=templates_dir
                )
    # 注册蓝图
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=main, url_prefix='/')
    app.register_blueprint(blueprint=tools, url_prefix='/tools')
    # 配置mysql数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ksrong-ops:Sklc123456-@mysql.ksrong-ops.com:3306/ksrong-ops?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 设置session密钥
    app.config['SECRET_KEY'] = 'sdertyuhgfd23456q'
    # 设置连接的redis数据库 默认连接到本地6379
    app.config['SESSION_TYPE'] = 'redis'
    # 设置远程
    app.config['SESSION_REDIS'] = redis.Redis(host='redis.ksrong-ops.com', port=6379, password='J]5#Umg_th3mYq6')
    # 初始化db

    db.init_app(app=app)

    return app


