import unittest
from serrano_sdk.secure_storage.client import SecureStorage

GATEWAY_URL = "https://on-premise-storage-gateway.services.cloud.ict-serrano.eu"
SKYFLOK_TOKEN = "PKxZpXhEx5JyT8uRaH6BBtKfkbOY4nfwe3mPqe9lWZi9ufzUfKYNkSr9UPIwslsC"

class SecureStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.secureStorage = SecureStorage(GATEWAY_URL, SKYFLOK_TOKEN)
        self.secureStorage.create_bucket("SERRANO_SDK_test_bucket")

    def test_list_buckets(self):
        """Test for list_buckets function"""

        result = self.secureStorage.list_buckets()
        self.assertEqual(result['Buckets'][0]['Name'], "SERRANO_SDK_test_bucket")

    def tearDown(self):
        self.secureStorage.delete_bucket("SERRANO_SDK_test_bucket")

if __name__ == '__main__':
    unittest.main()