from tests_unittest.app_test import *


class TestUser(MyTest):

    def setUp(self):
        self.user_username = "default"
        self.user_password = "somepassword"
        self.user_auth = self.user_username, self.user_password
        self.user_data = {"username": self.user_username, "password": self.user_password, }

        self.auditorium_num = "10"
        self.max_people_count = "48"
        self.auditorium_data = {"auditorium_num": self.auditorium_num, "max_people_count": self.max_people_count, }

        self.start = "2021-01-01 1:00:00"
        self.end = "2021-01-01 3:00:00"

        self.data = {"auditorium_num": self.auditorium_num, "username": self.user_username, "start": self.start,
                     "end": self.end}
        self.header = {"Content-Type": "application/json", }

    def test11_post_user(self):
        resp = self.client.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(200, resp.status_code)

    def test12_post_auditorium(self):
        resp = self.client.post("http://localhost:5000/auditorium", headers=self.header,
                                data=json.dumps(self.auditorium_data))
        self.assertEqual(200, resp.status_code)

    def test19_post_access(self):
        resp = self.client.post("http://localhost:5000/access", headers=self.header, data=json.dumps(self.data),
                                auth=self.user_auth)
        self.assertEqual(200, resp.status_code)

    def test20_get_accesses(self):
        resp = self.client.get("http://localhost:5000/access",
                               auth=self.user_auth)
        self.assertEqual(200, resp.status_code)



    def test50_delete_access(self):
        resp = self.client.delete("http://localhost:5000/access", headers=self.header,
                                  data=json.dumps({"auditorium_num": self.auditorium_num}),
                                  auth=self.user_auth)
        self.assertEqual(200, resp.status_code)

    def test88_delete_auditorium(self):
        resp = self.client.delete("http://localhost:5000/auditorium/" + self.auditorium_num)
        self.assertEqual(200, resp.status_code)

    def test99_delete_user(self):
        resp = self.client.delete("http://localhost:5000/user", headers=self.header, auth=self.user_auth)
        self.assertEqual(resp.status_code, 200)
