import logging
import warnings

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError


class SecureStorage:

    def create_bucket(self, bucket_name, storage_policy_name="SERRANO-SDK"):
        """Create an S3 bucket

        :param bucket_name: Bucket to create
        :param storage_policy_name: Name of storage policy
        :return: True if bucket created, else False
        """
        try:
            resp = self._client.create_bucket(Bucket=bucket_name,
                                              CreateBucketConfiguration={'LocationConstraint': storage_policy_name})
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def delete_bucket(self, bucket_name):
        """Delete an S3 bucket

        :param bucket_name: Bucket to delete
        :return: True if bucket deleted, else False
        """
        try:
            resp = self._client.delete_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def list_buckets(self):
        """List S3 buckets

        :return: String with information of buckets
        """
        try:
            resp = self._client.list_buckets()
        except ClientError as e:
            resp = ("Unable to list buckets. Client error: {ex}.").format(ex=e.response['Error'])
        except Exception as e:
            resp = ("Unable to list buckets. Exception: {ex}. ").format(ex=e)

        return resp

    def upload_object(self, bucket_name, object_key, file_data):
        """Upload object to bucket

        :param bucket_name: Bucket to upload the object to
        :param object_key: Key of object to be uploaded
        :return: True if object uploaded, else False
        """
        try:
            resp = self._client.put_object(Body=file_data, Bucket=bucket_name, Key=object_key)
            return True
        except ClientError as e:
            resp = ("Unable to upload object (bucket={bucket_name}). Client error: {ex}.").format(
                bucket_name=bucket_name, ex=e.response['Error'])
            logging.error(e)
            return False
        except Exception as e:
            resp = ("Unable to upload object (bucket={bucket_name}). Exception: {ex}. ").format(
                bucket_name=bucket_name, ex=e)
            logging.error(e)
            return False

    def get_object(self, bucket_name, object_key):
        """Get object from bucket

        :param bucket_name: Bucket to get the object from
        :param object_key: Key of requested object
        :return: The requested object, or the exception
        """
        file_name = object_key + "_downloaded"
        try:
            resp = self._client.get_object(Bucket=bucket_name, Key=object_key)
        except ClientError as e:
            resp = ("Unable to download object (bucket={bucket_name}). Client error: {ex}.").format(
                bucket_name=bucket_name, ex=e.response['Error'])
        except Exception as e:
            resp = ("Unable to download object (bucket={bucket_name}). Exception: {ex}. ").format(
                bucket_name=bucket_name, ex=e)
        return resp

    def download_object(self, bucket_name, object_key):
        """Download object from bucket

        :param bucket_name: Bucket to download the object from
        :param object_key: Key of object to be downloaded
        :return: True if object downloaded, else False
        """
        file_name = object_key + "_downloaded"
        try:
            resp = self._client.download_file(bucket_name, object_key, file_name)
            return True
        except ClientError as e:
            message = ("Unable to download object (bucket={bucket_name}). Client error: {ex}.").format(
                bucket_name=bucket_name, ex=e.response['Error'])
            logging.error(e)
            return False
        except Exception as e:
            message = ("Unable to download object (bucket={bucket_name}). Exception: {ex}. ").format(
                bucket_name=bucket_name, ex=e)
            logging.error(e)
            return False

    def delete_object(self, bucket_name, object_key):
        """Delete object from bucket

        :param bucket_name: Name of bucket that contains the object
        :param object_key: Key of object to be deleted
        :return: True if object deleted, else False
        """
        try:
            resp = self._client.delete_object(Bucket=bucket_name, Key=object_key)
            return True
        except ClientError as e:
            message = ("Unable to delete object (bucket={bucket_name}). Client error: {ex}.").format(
                bucket_name=bucket_name, ex=e.response['Error'])
            logging.error(e)
            return False
        except Exception as e:
            message = ("Unable to delete object (bucket={bucket_name}). Exception: {ex}. ").format(
                bucket_name=bucket_name, ex=e)
            return False

    """
    Instantiate a Secure Storage context.
    
    :param gateway_url: URL of on-premise-storage-gateway to use
    :param skyflok_token: skyflok token to be used
    """

    def __init__(self, gateway_url,
                 skyflok_token):
        self._client = boto3.client(
            's3',
            endpoint_url="{gateway}/s3".format(gateway=gateway_url),
            region_name="local",
            config=Config(signature_version='s3v4'),
            aws_access_key_id=skyflok_token,
            aws_secret_access_key="SECRET_KEY"
        )
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")
