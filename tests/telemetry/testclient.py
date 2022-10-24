import unittest

from serrano_sdk.telemetry.client import Telemetry


class TelemetryTestCase(unittest.TestCase):

    def setUp(self):
        self.telemetry = Telemetry(2)

    def test_employ(self):
        """Test employ"""

        result = self.telemetry.employ()
        self.assertEqual(result.status_code, 200)
        self.telemetry.close()

if __name__ == '__main__':
    unittest.main()