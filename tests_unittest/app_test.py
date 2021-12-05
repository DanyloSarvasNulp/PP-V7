from flask_testing import TestCase
from DataBase.config_app import db
from app import app
from flask import json


class MyTest(TestCase):
    def create_app(self):
        return app

    # def setUp(self):
    #     db.create_all()
    #
    # def tearDown(self):
    #     db.session.remove()
