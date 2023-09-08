import json
import os.path
import requests

from serrano_sdk.resource_orchestrator.assignments import get_assignments, create_assignments, update_assignments, \
    terminate_assignments, get_assignments_info, watch_assignments
from serrano_sdk.resource_orchestrator.bundles import watch_bundle, get_bundle_info, delete_bundle, update_bundle, \
    create_bundle, get_bundles
from serrano_sdk.resource_orchestrator.deployments import get_deployments, get_deployment_info, create_deployment, \
    update_deployment, terminate_deployment, watch_deployments
from serrano_sdk.resource_orchestrator.kernels import create_faas_kernel_execution, get_faas_kernel_execution, \
    create_kernel_execution, get_kernel_execution
from serrano_sdk.resource_orchestrator.storage_policies import get_storage_policy_info, create_storage_policy, \
    update_storage_policy, delete_storage_policy, get_storage_policies


class ResourceOrchestrator:
    """
    Instantiate a ResourceOrchestrator operation.

    :param config_path: Filesystem path where the configuration file is located (default: "~/.serrano/sdk_config.json")
    :type config_path: string
    """
    deployments_url = "/api/v1/orchestrator/deployments"
    storage_policy_url = "/api/v1/orchestrator/storage_policies"
    assignments_url = "/api/v1/orchestrator/assignments"
    bundles_url = "api/v1/orchestrator/bundles"
    def __init__(self, config_path):
        self.session = requests.Session()

        if config_path:
            self.__load_configuration(config_path)
        else:
            self.__load_configuration("%s/.serrano/sdk_config.json" % (os.path.expanduser("~")))

    def __load_configuration(self, config_file):

        try:
            with open(config_file) as f:
                params = json.load(f)

                self.__client_uuid = params["resource_orchestrator"]["api_client"]["client_uuid"]

                self.__rest_url = "http://%s:%s" % (params["resource_orchestrator"]["api_client"]["server_address"],
                                                     params["resource_orchestrator"]["api_client"]["server_port"])
                self.__base_url = "http://%s" % (params["resource_orchestrator"]["api_client"]["server_address"])
                self.__http_auth = (params["resource_orchestrator"]["api_client"]["username"],
                                    params["resource_orchestrator"]["api_client"]["password"])

        except FileNotFoundError:
            raise clientEvents.ConfigurationError("Invalid configuration - FileNotFoundError")
        except json.JSONDecodeError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - JSONDecodeError: %s" % s.msg)
        except KeyError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - Missing configuration parameter %s" % s)

    def is_ready(self):
        response =self.session.get(self.__rest_url, verify=False)
        return response

    #Kernels
    def create_faas_kernel(self, name, params):
        try:
            result = create_faas_kernel_execution("%s/v1/orchestrator/faas" % self.__rest_url, name, params)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_faas_kernel(self, uuid):
        try:
            result = get_faas_kernel_execution("%s/v1/orchestrator/faas" % self.__rest_url, uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def create_kernel(self, name, params):
        try:
            result = create_kernel_execution("%s/v1/orchestrator/faas" % self.__rest_url, name, params)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_kernel(self, uuid):
        try:
            result = get_kernel_execution("%s/v1/orchestrator/faas" % self.__rest_url, uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")

    # --- Deployments --- #
    def get_deployments(self, deployments_url):
        try:
            result = get_deployments("%s%s" % (self.__base_url, deployments_url))
            return result
        except Exception as e:
            print(f"Error: {e}")
    def create_deployments(self, deployments_url, deployment_data):
        try:
            result = create_deployment("%s%s" % (self.__base_url, deployments_url), deployment_data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def update_deployment(self, deployments_url, deployment_data):
        try:
            result = update_deployment("%s%s" % (self.__base_url, deployments_url), deployment_data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def terminate_deployment(self, deployments_url, uuid):
        try:
            result = terminate_deployment("%s%s" % (self.__base_url, deployments_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_deployment_info(self, deployments_url, uuid):
        try:
            result = get_deployment_info("%s%s" % (self.__base_url, deployments_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def watch_deployments(self, deployments_url):
        try:
            result = watch_deployments("%s%s" % (self.__base_url, deployments_url))
            return result
        except Exception as e:
            print(f"Error: {e}")

    # --- Storage Policies --- #
    def get_storage_policies(self, storage_policy_url):
        try:
            result = get_storage_policies("%s%s" % (self.__base_url, storage_policy_url))
            return result
        except Exception as e:
            print(f"Error: {e}")
    def create_storage_policy(self, storage_policy_url, data):
        try:
            result = create_storage_policy("%s%s" % (self.__base_url, storage_policy_url), data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def update_storage_policy(self, storage_policy_url, data):
        try:
            result = update_storage_policy("%s%s" % (self.__base_url, storage_policy_url), data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def delete_storage_policy(self, storage_policy_url, uuid):
        try:
            result = delete_storage_policy("%s%s" % (self.__base_url, storage_policy_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_storage_policy_info(self, storage_policy_url, uuid):
        try:
            result = get_storage_policy_info("%s%s" % (self.__base_url, storage_policy_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")

    # --- Clusters --- #
    def get_clusters(self):
        data = {}
        res = requests.get("%s/api/v1/orchestrator/clusters" % self.__rest_url, auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)["clusters"]
        return data
    def get_cluster(self, cluster_uuid):
        data = {}
        res = requests.get("%s/api/v1/orchestrator/clusters/%s" % (self.__rest_url, cluster_uuid),
                           auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)
        return data
    def get_cluster_heartbeat(self, cluster_uuid):
        data = {}
        res = requests.get("%s/api/orchestrator/clusters/health/%s" % (self.__rest_url, cluster_uuid),
                           auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)["cluster_heartbeat"]
        return data
    def delete_cluster(self, cluster_uuid):
        res = requests.delete("%s/api/orchestrator/clusters/%s" % (self.__rest_url, cluster_uuid),
                              auth=self.__http_auth)
        print(res.text)
    def post_cluster(self, cluster_uuid, type, nodes):
        data = None
        res = requests.post("%s/api/v1/orchestrator/clusters" % self.__rest_url,
                            auth=self.__http_auth,
                            json={"cluster_uuid": cluster_uuid, "type": type, "nodes": nodes})
        if res.status_code == 201:
            data = json.loads(res.text)
        return data
    def put_cluster(self, cluster_uuid, type, nodes):
        data = None
        res = requests.put("%s/api/v1/orchestrator/clusters" % self.__rest_url,
                           auth=self.__http_auth,
                           json={"cluster_uuid": cluster_uuid, "type": type, "nodes": nodes})
        if res.status_code == 200:
            data = json.loads(res.text)
        return data
    def watch_cluster(self):
        data = {}
        res = requests.get("%s/api/v1/orchestrator/clusters" % self.__rest_url, auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)
        return data

    # --- Assignments--- #
    def get_assignments(self, assignments_url):
        try:
            result = get_assignments("%s%s" % (self.__base_url, assignments_url))
            return result
        except Exception as e:
            print(f"Error: {e}")
    def create_assignments(self, assignments_url, assignments_data):
        try:
            result = create_assignments("%s%s" % (self.__base_url, assignments_url), assignments_data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def update_assignments(self, assignments_url, assignments_data):
        try:
            result = update_assignments("%s%s" % (self.__base_url, assignments_url), assignments_data)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def terminate_assignments(self, assignments_url, uuid):
        try:
            result = terminate_assignments("%s%s" % (self.__base_url, assignments_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_assignments_info(self, assignments_url, uuid):
        try:
            result = get_assignments_info("%s%s" % (self.__base_url, assignments_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def watch_assignments(self, assignments_url, uuid):
        try:
            result = watch_assignments("%s%s" % (self.__base_url, assignments_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")

    # --- Bundles--- #
    def get_bundles(self,bundles_url):
        try:
            result = get_bundles("%s/%s" % (self.__rest_url, bundles_url))
            print("results:", result)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def create_bundle(self,bundles_url):
        try:
            result = create_bundle("%s/%s" % (self.__rest_url, bundles_url))
            return result
        except Exception as e:
            print(f"Error: {e}")
    def update_bundle(self,bundles_url, uuid):
        try:
            result = update_bundle("%s/%s" % (self.__rest_url, bundles_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def delete_bundle(self,bundles_url, uuid):
        try:
            result = delete_bundle("%s/%s" % (self.__rest_url, bundles_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def get_bundle_info(self,bundles_url, uuid):
        try:
            result = get_bundle_info("%s/%s" % (self.__rest_url, bundles_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")
    def watch_bundle(self, bundles_url, uuid):
        try:
            result = watch_bundle("%s/%s" % (self.__rest_url, bundles_url), uuid)
            return result
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        self.session.close()

