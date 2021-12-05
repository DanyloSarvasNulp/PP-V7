from flask_testing import TestCase
from flask import Flask
from DataBase.config_app import db, app


class MyTest(TestCase):
    def create_app(self):
        return app


