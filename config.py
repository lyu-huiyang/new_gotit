# -*- coding: utf-8 -*-

class Config:

    SECRET_KEY = 'lvhuiyang'  # 实现CSRF保护的通用密钥,环境变量中获取
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {
    'default' : Config
}
