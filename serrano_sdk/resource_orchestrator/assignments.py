import json
import requests

def get_assignments(base_url):
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

def create_assignments(base_url, assignments_data):
    try:
        response = requests.post(base_url, json=assignments_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def update_assignments(base_url, assignments_data):
    try:
        response = requests.put(base_url, json=assignments_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def terminate_assignments(base_url, uuid):
    try:
        response = requests.delete(base_url, uuid)
        if response.status_code == 200:
            data = json.loads(response.text)
            data['status_code'] = 200
            return data
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def get_assignments_info(base_url, uuid):
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

def watch_assignments(base_url, uuid):
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