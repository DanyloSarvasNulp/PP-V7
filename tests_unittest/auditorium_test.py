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
        resp = self.client.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(200, resp.status_code)
        self.assertGreaterEqual(resp. json().items(), dict(username="default").items())
