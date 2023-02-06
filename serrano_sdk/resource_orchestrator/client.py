import json
import os.path
import requests

class ResourceOrchestrator:
    """
    Instantiate a ResourceOrchestrator operation.

    :param parameter: parameter.
    :type parameter: int
    """

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
    def get_clusters(self):
        data = {}
        res = requests.get("%s/api/v1/orchestrator/clusters" % self.__rest_url, auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)["clusters"]
        return data

    def get_cluster(self, cluster_uuid):
        data = {}
        res = requests.get("%s/api/v1/orchestrator/clusters/%s" % (self.__rest_url, cluster_uuid), auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)
        return data

    def get_cluster_heartbeat(self, cluster_uuid):
        data = {}
        res = requests.get("%s/api/orchestrator/clusters/health/%s" % (self.__rest_url, cluster_uuid), auth=self.__http_auth)
        if res.status_code == 200:
            data = json.loads(res.text)["cluster_heartbeat"]
        return data

    def delete_cluster(self, cluster_uuid):
        res = requests.delete("%s/api/orchestrator/clusters/%s" % (self.__rest_url, cluster_uuid), auth=self.__http_auth)
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

    def close(self):
        self.session.close()

