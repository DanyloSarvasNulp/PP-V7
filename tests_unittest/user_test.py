import requests
from tests_unittest.app_test import *


class TestUser(MyTest):

    def setUp(self):
        self.user_username = "default"
        self.user_password = "somepassword"
        self.user_auth = self.user_username, self.user_password
        self.user_firstname = "Example"

        self.user_data = {"username": self.user_username, "password": self.user_password, }
        self.header = {"Content-Type": "application/json", }

    def test1_post_user(self):
        resp = requests.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(200, resp.status_code)
        self.assertGreaterEqual(resp.json().items(), dict(username="default").items())

    def test2_failed_post_user(self):
        resp = self.client.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(400, resp.status_code)

    def test3_get_user(self):
        resp = self.client.get("http://localhost:5000/user", headers=self.header, auth=self.user_auth)
        self.assertEqual(resp.status_code, 200)

    def test4_failed_get_user(self):
        resp = self.client.get("http://localhost:5000/user", headers=self.header,
                               auth=(self.user_username, "wrong_password"))
        self.assertEqual(resp.status_code, 401)

    def test5_put_user(self):
        resp = self.client.put("http://localhost:5000/user", headers=self.header,
                               auth=self.user_auth, data=json.dumps({"first_name": self.user_firstname}))
        self.assertEqual(resp.status_code, 200)

    def test6_failed_put_user(self):
        resp = self.client.put("http://localhost:5000/user", headers=self.header,
                               auth=self.user_auth, data=json.dumps({"not existing field": self.user_firstname}))
        self.assertEqual(resp.status_code, 400)

    def test9_delete_user(self):
        resp = self.client.delete("http://localhost:5000/user", headers=self.header, auth=self.user_auth)
        self.assertEqual(resp.status_code, 200)
        # self.assertIsNone(session.query(user).filter_by(email="someMail@gmail.com").first())