import json
import os.path
import requests

class ROT:
    """
    Instantiate a ROT operation.

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

                self.__client_uuid = params["rot"]["api_client"]["client_uuid"]
                self.__databroker = params["rot"]["databroker_interface"]

                self.__rest_url = "https://%s:%s" % (params["rot"]["api_client"]["server_address"],
                                                    params["rot"]["api_client"]["server_port"])

                self.__http_auth = (params["rot"]["api_client"]["username"], params["rot"]["api_client"]["password"])

        except FileNotFoundError:
            raise clientEvents.ConfigurationError("Invalid configuration - FileNotFoundError")
        except json.JSONDecodeError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - JSONDecodeError: %s" % s.msg)
        except KeyError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - Missing configuration parameter %s" % s)

    def get_engines(self):
        res = requests.get("%s/api/v1/rot/engines" % self.__rest_url, auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def get_engine(self, engine_uuid):
        res = requests.get("%s/api/v1/rot/engine/%s" % (self.__rest_url, engine_uuid), auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def get_logs(self, execution_uuid):
        res = requests.get("%s/api/v1/rot/logs/%s" % (self.__rest_url, execution_uuid), auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def get_statistics(self, **kwargs):
        start = kwargs.get('start', None)
        end = kwargs.get('end', None)
        return {}

    # TODO def delete_execution(self, execution_uuid):
    #     res = requests.delete("%s/api/v1/rot/execution/%s" % (self.__rest_url, execution_uuid), auth=self.__http_auth)
    #     print(res.text)

    def post_execution(self, execution_plugin, parameters):
        if type(parameters) is not dict:
            parameters = json.loads(parameters)
        res = requests.post("%s/api/v1/rot/execution" % self.__rest_url,
                            auth=self.__http_auth,
                            json={"execution_plugin": execution_plugin, "parameters": parameters})
        data = {'status_code': res.status_code}
        if res.status_code == 200 or res.status_code == 201:
            data = json.loads(res.text)
            data['status_code'] = res.status_code
        return data

    def get_execution(self, execution_uuid):
        data = {}
        res = requests.get("%s/api/v1/rot/execution/%s" % (self.__rest_url, execution_uuid), auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def get_executions(self):
        res = requests.get("%s/api/v1/rot/executions" % self.__rest_url, auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def close(self):
        self.session.close()

