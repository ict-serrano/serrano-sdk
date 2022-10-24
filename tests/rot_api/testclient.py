import unittest

from serrano_sdk.rot_api.client import ROT


class ROTTestCase(unittest.TestCase):

    def setUp(self):
        self.rot_api = ROT(2)

    def test_employ(self):
        """Test employ"""

        result = self.rot_api.employ()
        self.assertEqual(result.status_code, 200)
        self.rot_api.close()

if __name__ == '__main__':
    unittest.main()