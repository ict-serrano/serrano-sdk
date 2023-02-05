import unittest, os
from serrano_sdk.secure_storage.client import SecureStorage

GATEWAY_URL = "https://on-premise-storage-gateway.services.cloud.ict-serrano.eu"
SKYFLOK_TOKEN = "PKxZpXhEx5JyT8uRaH6BBtKfkbOY4nfwe3mPqe9lWZi9ufzUfKYNkSr9UPIwslsC"
file_data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sit amet vulputate augue. Phasellus\
 lobortis pharetra dignissim. Quisque feugiat, nulla id rutrum interdum, nunc tellus maximus mauris, at mollis velit\
  velit ac felis. Etiam non risus tempor, ultrices lorem nec, pellentesque quam. Aliquam vel lacus nec magna mattis\
   elementum. Donec ipsum est, lobortis vel ante eu, auctor sagittis tortor. Duis quis ex mi. Proin auctor dui felis,\
    sed eleifend elit venenatis in. Duis feugiat rhoncus sapien et finibus. Donec vitae magna porta, egestas lacus\
     sodales, tincidunt eros.

Mauris ut nunc sed augue sagittis maximus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur\
 ridiculus mus. Morbi accumsan convallis rutrum. Quisque fringilla aliquam libero sed semper. Duis volutpat turpis eu\
  placerat viverra. Mauris vel ullamcorper arcu. Cras ultricies finibus velit a sollicitudin. Donec rhoncus sit amet\
   elit varius ullamcorper. Quisque mattis dignissim ex. Pellentesque in sodales ex. Nunc convallis, urna nec volutpat\
    luctus, massa tellus pellentesque massa, sit amet faucibus turpis leo vitae turpis. Donec non suscipit ex."""

class SecureStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.secureStorage = SecureStorage(GATEWAY_URL, SKYFLOK_TOKEN)
        self.secureStorage.create_bucket("SERRANO_SDK_test_bucket")

    def test_list_buckets(self):
        """Test for list_buckets function"""

        result = self.secureStorage.list_buckets()
        self.assertEqual(result['Buckets'][0]['Name'], "SERRANO_SDK_test_bucket")

    def test_upload_object(self):
        """Test for upload object function"""

        result = self.secureStorage.upload_object("SERRANO_SDK_test_bucket", "test_file00001", file_data)
        self.assertTrue(result)

        self.secureStorage.delete_object("SERRANO_SDK_test_bucket", "test_file00001")

    def test_get_object(self):
        """Test for get object function"""
        result = self.secureStorage.upload_object("SERRANO_SDK_test_bucket", "test_file00001", file_data)
        self.assertTrue(result)

        response = self.secureStorage.get_object("SERRANO_SDK_test_bucket", "test_file00001")
        self.assertEquals(file_data, response['Body'].read().decode('utf-8'))

        self.secureStorage.delete_object("SERRANO_SDK_test_bucket", "test_file00001")

    def test_download_object(self):
        """Test for download object function"""
        result = self.secureStorage.upload_object("SERRANO_SDK_test_bucket", "test_file00001", file_data)
        self.assertTrue(result)

        result = self.secureStorage.download_object("SERRANO_SDK_test_bucket", "test_file00001")
        self.assertTrue(result)
        file = open("test_file00001_downloaded", "r")
        self.assertEquals(file_data, file.read())
        os.remove("test_file00001_downloaded")

        self.secureStorage.delete_object("SERRANO_SDK_test_bucket", "test_file00001")


    def tearDown(self):
        self.secureStorage.delete_bucket("SERRANO_SDK_test_bucket")

if __name__ == '__main__':
    unittest.main()