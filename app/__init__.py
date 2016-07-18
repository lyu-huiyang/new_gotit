from config import config
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    moment.init_app(app)
    db.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .wechat import wechat
    app.register_blueprint(wechat, url_prefix='/wechat')

    return app
