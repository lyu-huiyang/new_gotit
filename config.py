# coding=utf-8
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.getenv('NEWGOTIT_DATABASE_URI')
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config
}
