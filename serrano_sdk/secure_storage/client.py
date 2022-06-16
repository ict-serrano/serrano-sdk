import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

class SecureStorage:
    """
    Instantiate a Secure Storage context.

    :param multiplier: The multiplier.
    :type multiplier: int
    """

    def create_bucket(self, bucket_name="S3_test_bucket", storage_policy_name="S3_test_storage_policy"):
        """Create an S3 bucket

        :param bucket_name: Bucket to create
        :param storage_policy_name: Name of storage policy
        :return: True if bucket created, else False
        """
        try:
            resp = self._client.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def __init__(self, gateway_url="http://localhost:2525",
                 skyflok_token="QNF7qlO6zydbDIbloiyex5CsGziubSznZpVgXqrCxQ4MlSkSwN5OYr4SYfuAh3mD"):
        self._client = boto3.client(
            's3',
            endpoint_url="{gateway_url}/s3".format(gateway_url),
            region_name="",
            config=Config(signature_version='s3v4'),
            aws_access_key_id=skyflok_token,
            aws_secret_access_key="SECRET_KEY"
        )

