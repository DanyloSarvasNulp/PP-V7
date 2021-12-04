from unittest import TestCase
from unittest.mock import patch, Mock
import urllib
from urllib import request

import requests
from flask import json

# from database.app import app
# from database.middlewares.middlewares_user import UserSchema, login
# from database.models import user
# from database.authorization import *
import bcrypt
from urllib3 import response


class TestUser(TestCase):

    def setUp(self):
        self.user_id = "1"
        self.user_username = "default"
        self.user_password = "somepassword"
        self.user_auth = "default:somepassword"
        self.user_password_hashed = bcrypt.hashpw(self.user_password.encode("utf-8"), bcrypt.gensalt())

        self.user_data = {"username": "default", "password": "somepassword", }
        self.header = {"Content-Type": "application/json", }

    def test1_post_user(self):
        resp = requests.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))

        self.assertEqual(200, resp.status_code)

        self.assertGreaterEqual(resp.json().items(), dict(username="default").items())

    # def test2_failed_post_user(self):
    #     resp = requests.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
    #     self.assertEquals(400, resp.status_code)

    # def test3_authenticate_user(self):
    #     resp = verify_password(self.user_email, self.user_password)
    #     self.assertIsInstance(resp, user)
    #
    # def test4_failed_authenticate_user(self):
    #     resp = verify_password("wrong_email", "wrong_password")
    #     self.assertIsNot(resp, user)
    #
    # def test5_get_user(self):
    #     resp = requests.get("http://localhost:5000/user/" + self.user_id, headers=self.header, auth=(self.user_email, self.user_password))
    #     self.assertEquals(resp.status_code, 200)
    #     # self.assertEquals(resp.json, )
    #
    # def test6_failed_get_user(self):
    #     resp = requests.get("http://localhost:5000/user/" + self.user_id, headers=self.header, auth=(self.user_email, "wrong_password"))
    #     self.assertEquals(resp.status_code, 401)

    def test20_delete_user(self):
        resp = requests.delete("http://localhost:5000/user", headers=self.header,
                               auth=(self.user_username, self.user_password))
        self.assertEqual(resp.status_code, 200)
        # self.assertIsNone(session.query(user).filter_by(email="someMail@gmail.com").first())

# class TestBank(TestCase):
#
#     def setUp(self):
#         self.user_id = "2"
#         self.account_id = "2"
#         self.user_email = "someMail@gmail.com"
#         self.user_password = "somepassword"
#         self.user_auth = "someMail@gmail.com:somepassword"
#         self.user_password_hashed = bcrypt.hashpw(self.user_password.encode("utf-8"), bcrypt.gensalt())
#
#         self.account_data = {"user_id": self.user_id, "name": "someName", }
#         self.header = {"Content-Type": "application/json", }
#
#     def test1_post_user(self):
#         resp = requests.post("http://localhost:5000/account", headers=self.header, data=json.dumps(self.user_data))
#
#         self.assertEqual(200, resp.status_code)
#         # self.assertEquals(resp.json, {
#         #     "email": "someEmail@gmail.com",
#         #     "password": "somepassword",
#         # })
#         # self.assertTrue(session.query(user).filter_by(email=self.user_email).one)
#
#     def test20_delete_user(self):
#         resp = requests.delete("http://localhost:5000/account/" + self.account_id, headers=self.header, auth=(self.user_email, self.user_password))
#         self.assertEquals(resp.status_code, 200)
#         # self.assertIsNone(session.query(user).filter_by(email="someMail@gmail.com").first())
