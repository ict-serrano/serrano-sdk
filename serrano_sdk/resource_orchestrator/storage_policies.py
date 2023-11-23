import json
import requests

def get_storage_policies(base_url):
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e
def create_storage_policy(base_url, storage_data):
    try:
        response = requests.post(base_url, json=storage_data)
        if response.status_code == 201:
            data = json.loads(response.text)
            data['status_code'] = 201
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e
def update_storage_policy(base_url, storage_data):
    try:
        response = requests.put(base_url, json=storage_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e
def delete_storage_policy(base_url, uuid):
    try:
        response = requests.delete(base_url+"/"+uuid)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e
def get_storage_policy_info(base_url, uuid):
    try:
        response = requests.get(base_url+"/"+uuid)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e