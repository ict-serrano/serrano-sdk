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

    def close(self):
        self.session.close()