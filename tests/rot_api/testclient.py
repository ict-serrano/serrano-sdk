import unittest
import os.path
from serrano_sdk.rot_api.client import ROT


# example values

execution_id = "eb7d5663-50ca-486f-9802-3cb4f08af40d"
execution_plugin = "SimpleMatch"
engine_id = "6218118f-748d-42ad-b2f2-65e6332435ac"
username = "some_username"
password = "some_password"
client_uuid = "7ebef019-1894-4fb0-8ee6-2dd8a096171e"


class ROTTestCase(unittest.TestCase):

    def setUp(self):
        self.rot_api = ROT(os.path.join(os.path.dirname(__file__), "sdk_config.json"))

    def test_get_engines(self):
        result = self.rot_api.get_engines()
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_engine(self):
        result = self.rot_api.get_engine(engine_id)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_logs(self):
        result = self.rot_api.get_logs(execution_id)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_history(self):
        result = self.rot_api.get_history()
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_executions(self):
        result = self.rot_api.get_executions()
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_execution(self):
        result = self.rot_api.get_execution(execution_id)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_post_execution(self):
        result = self.rot_api.post_execution(execution_plugin, {})
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_delete_execution(self):
        result = self.rot_api.delete_execution(execution_id)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_statistics(self):
        result = self.rot_api.get_statistics()
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_get_users(self):
        result = self.rot_api.get_users()
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_post_user(self):
        result = self.rot_api.post_user(username,password)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

    def test_delete_user(self):
        result = self.rot_api.delete_user(client_uuid)
        self.assertEqual(result['status_code'], 200)
        self.rot_api.close()

if __name__ == '__main__':
    unittest.main()