import json
import os.path
import requests

class AIEnhancedServiceOrchestrator:
    """
     Instantiate a ResourceOrchestrator operation.

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

                # self.__client_uuid = params["service_orchestrator"]["api_client"]
                self.__rest_url = "http://%s:%s" % (params["service_orchestrator"]["api_client"]["server_address"],
                                            params["service_orchestrator"]["api_client"]["server_port"])

                self.__http_auth = (params["service_orchestrator"]["api_client"]["username"],
                                             params["service_orchestrator"]["api_client"]["password"])

        except FileNotFoundError:
            raise clientEvents.ConfigurationError("Invalid configuration - FileNotFoundError")
        except json.JSONDecodeError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - JSONDecodeError: %s" %s.msg)
        except KeyError as s:
            raise clientEvents.ConfigurationError("Invalid configuration - Missing configuration parameter %s" %s)


    def is_ready(self):
        response = self.session.get(self.__rest_url, verify=False)
        return response

    def create_deployment_scenarios(self, object_params):
        # Change path
        res = requests.post("%s/CreateDeploymentScenarios" % self.__rest_url,
                            auth=self.__http_auth,
                            json=object_params
                            )
        data = {'status_code': res.status_code}
        if res.status_code == 200 or res.status_code == 201:
            data = json.loads(res.text)
            data['status_code'] = res.status_code
        return data

    def application_deployment_through_ro(self, object_params):
        # Change path
        res = requests.post("%s/ApplicationDeploymentThroughRO" % self.__rest_url,
                            auth=self.__http_auth,
                            json= object_params
                            )
        data = {'status_code': res.status_code}
        if res.status_code == 200 or res.status_code == 201:
            data = json.loads(res.text)
            data['status_code'] = res.status_code
        return data

    def application_management(self, appid, action, params):
        res = requests.post("%s/ApplicationManagement" % self.__rest_url,
                            auth=self.__http_auth,
                            json={"appid": appid, "action": action, "params": params}
                            )
        data = {'status_code': res.status_code}
        if res.status_code == 200 or res.status_code == 201:
            data = json.loads(res.text)
            data['status_code'] = res.status_code
        return data

    def testing_central_telemetry_handler(self):
        res = requests.get("%s/TestingCentralTelemetryHanlder" % self.__rest_url, auth=self.__http_auth)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = res.status_code
        return data
    def close(self):
        self.session.close()