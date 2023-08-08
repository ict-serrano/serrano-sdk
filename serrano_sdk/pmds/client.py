import json
import os.path
import requests

class PMDS:
    """
    Instantiate a PMDS operation.

    :param config_path: Filesystem path where the configuration file is located (default: "~/.serrano/sdk_config.json")
    :type config_path: string
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

                self.__client_uuid = params["pmds"]["api_client"]["client_uuid"]

                self.__rest_url = "http://%s:%s" % (params["pmds"]["api_client"]["server_address"],
                                                    params["pmds"]["api_client"]["server_port"])

                self.__http_auth = (params["pmds"]["api_client"]["username"],
                                    params["pmds"]["api_client"]["password"])

        except FileNotFoundError:
            raise clientEvents.ConfigurationError("Invalid configuration - FileNotFoundError")
        except json.JSONDecodeError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - JSONDecodeError: %s" % s.msg)
        except KeyError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - Missing configuration parameter %s" % s)

    def pmds_service_query_nodes(self, cluster_uuid, **kwargs):
        """
        Retrieve historical telemetry data for the worker nodes within a K8s cluster.

        Required parameters:
          - cluster_uuid (path parameter) => Determines the K8s cluster.

        The telemetry data for the available worker nodes within a K8s cluster are organized into five categories:
        (1) general, (2) cpu, (3) memory, (4) storage and (5) network. The query parameter "group" can be used to
        determine the group of metrics that the service will return. Supported values: "general", "cpu", "memory",
        "storage", "network". If not specified the "general" metrics will be returned.

        Timeframe options:
         - start (query parameter) => Earliest time to include in results, by default is the last 24 hours (-1d).
            Accepted formats are relative duration (e.g., -30m, -1h, -1d) or unix timestamp in seconds (e.g., 1644838147).
            Durations are relative to now().
         - stop (query parameter) => Latest time to include in results. Default is now(). Accepted formats are relative
            duration (e.g., -30m, -1h, -1d) or unix timestamp in seconds (e.g., 1644838147).Durations are relative to now().

        Filtering options:
          - node_name (query parameter) => Limits the results only for the pods that are running in the specified node name.
          - field_measurement (query parameter) => Limits the results only for the selected parameter.

        Formatting options:
          - format (query parameter) => Determines the format of the response. Supported values "raw" and "compact".
            The "raw" format provides the return data in a time series way. The "compact" format organizes the data at a
            per persistent volume basis. If not specified the "compact" format will be used.
    """
        valid_query_params = ["group", "start", "stop", "node_name", "field_measurement", "format"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/pmds/nodes/%s" % (self.__rest_url, cluster_uuid), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data



    def pmds_service_query_deployments(self, cluster_uuid, namespace, **kwargs):
        """
            Provide historical telemetry data for the available Deployments within a K8s cluster.
            
            Required parameters:
            - cluster_uuid (path parameter) => Determines the K8s cluster.
            - namespace (query parameter) =>  Determines the target namespace

            Parameters for requesting data for a specific timeframe, the same with the pmds_service_query_nodes()
            
            Filtering parameters:
            - name (path parameter) => Limits the results only for the deployment with the provided name.
            
            Response format parameter, the same with the pmds_service_query_nodes()
        """
        valid_query_params = ["start", "stop", "name", "format"]

        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        query_params["namespace"] = namespace

        res = requests.get("%s/api/v1/pmds/deployments/%s" % (self.__rest_url, cluster_uuid), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data


    def pmds_service_query_pods(self, cluster_uuid, namespace, **kwargs):
        """
            Provide historical telemetry data for the available Pods within a K8s cluster.
            
            Required parameters:
            - cluster_uuid (path parameter) => Determines the K8s cluster.
            - namespace (query parameter) =>  Determines the target namespace

            Parameters for requesting data for a specific timeframe, the same with the pmds_service_query_nodes()
            
            Filtering parameters:
            - name (path parameter) => Limits the results only for the pod with the provided name.
            - node_name (path parameter) => Limits the results only for the pods that are running in the specified node name.  
            
            Response format parameter, the same with the pmds_service_query_nodes()
        """
        valid_query_params = ["start", "stop", "name", "node_name", "format"]

        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        query_params["namespace"] = namespace

        res = requests.get("%s/api/v1/pmds/pods/%s" % (self.__rest_url, cluster_uuid), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def pmds_service_query_pvs(self, cluster_uuid, **kwargs):
        valid_query_params = ["start", "stop", "name", "format"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/pmds/pvs/%s" % (self.__rest_url, cluster_uuid), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def close(self):
        self.session.close()