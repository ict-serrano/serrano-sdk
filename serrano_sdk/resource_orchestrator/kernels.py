import requests

def create_faas_kernel_execution(url, name, params):
    response = requests.post(url, json={"name": name, "params": params})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed. Error code: {response.status_code}")

def get_faas_kernel_execution(url, uuid):
    response = requests.get(url + uuid)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get the UUID {uuid}. Error code: {response.status_code}")

def create_kernel_execution(url, name, params):
    response = requests.post(url, json={"name": name, "params": params})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed. Error code: {response.status_code}")

def get_kernel_execution(url, uuid):
    response = requests.get(url + uuid)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get the UUID {uuid}. Error code: {response.status_code}")
