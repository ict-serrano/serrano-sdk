# Import SecureStorage from your library
from serrano_sdk.secure_storage.client import SecureStorage

# Instantiate a SecureStorage object
GATEWAY_URL = "https://on-premise-storage-gateway.services.cloud.ict-serrano.eu/s3"
SKYFLOK_TOKEN = "PKxZpXhEx5JyT8uRaH6BBtKfkbOY4nfwe3mPqe9lWZi9ufzUfKYNkSr9UPIwslsC"
secureStorage = SecureStorage(GATEWAY_URL, SKYFLOK_TOKEN)

# Get available buckets
secureStorage.delete_bucket("bucket-with-default-policy")
secureStorage.delete_bucket("bucket-with-custom-policy")
print(str(secureStorage.list_buckets()['Buckets']))
