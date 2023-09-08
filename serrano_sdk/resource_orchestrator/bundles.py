import requests

def get_bundles(base_url):
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def create_bundle(base_url):
    try:
        response = requests.post(base_url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def update_bundle(base_url, uuid):
    try:
        url = f"{base_url}/{uuid}"
        response = requests.put(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def delete_bundle(base_url, uuid):
    try:
        url = f"{base_url}/{uuid}"
        response = requests.delete(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def get_bundle_info(base_url, uuid):
    try:
        url = f"{base_url}/{uuid}"
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e

def watch_bundle(base_url, uuid):
    try:
        url = f"{base_url}/watch/{uuid}"
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Failed. Error code: {response.status_code}")
    except Exception as e:
        raise e
