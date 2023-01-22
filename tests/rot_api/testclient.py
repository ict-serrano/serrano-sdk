import unittest
import os.path
from serrano_sdk.rot_api.client import ROT


class ROTTestCase(unittest.TestCase):

    def setUp(self):
        self.rot_api = ROT(os.path.join(os.path.dirname(__file__), "sdk_config.json"))

    def test_employ(self):
        """Test employ"""

        result = self.rot_api.is_ready()
        self.assertEqual(result.status_code, 200)
        self.rot_api.close()

if __name__ == '__main__':
    unittest.main()