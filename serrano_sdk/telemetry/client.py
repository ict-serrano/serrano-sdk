import json
import requests

CTH_SERVICE = "http://central-telemetry.services.cloud.ict-serrano.eu"


class Telemetry:
    """
    Instantiate a Telemetry operation.

    :param parameter: parameter.
    :type parameter: int
    """

    def __init__(self, parameter):
        self.parameter = parameter
        self.session = requests.Session()

    def employ(self):
        """
        Employ telemetry using a given parameter.

        :param parameter: The parameter to use.
        :type parameter: int

        :return: The result of calling telemetry.
        :rtype: object
        """
        response = self.session.get("http://api.open-notify.org/astros.json")
        return response
    

    def telemetry_probe_monitor(self, **kwargs):
        valid_query_params = ["target"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/telemetry/probe/monitor" % (CTH_SERVICE), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    

    def telemetry_probe_inventory(self):
        res = requests.get("%s/api/v1/telemetry/probe/inventory" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data


    def telemetry_probe_collection(self):
        res = requests.post("%s/api/v1/telemetry/probe/collection" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    

    def telemetry_probe_streaming(self, sessionId):
        res = requests.delete("%s/api/v1/telemetry/probe/streaming/%s" % (CTH_SERVICE,sessionId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_query_clusters(self):
        res = requests.get("%s/api/v1/telemetry/central/clusters" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_query_cluster(self, clusterId):
        res = requests.get("%s/api/v1/telemetry/central/clusters/%s" % (CTH_SERVICE,clusterId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data


    def telemetry_cluster_monitor(self, clusterId, **kwargs):
        valid_query_params = ["target"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/telemetry/central/clusters/monitor/%s" % (CTH_SERVICE,clusterId), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data


    def telemetry_cluster_inventory(self, clusterId):
        res = requests.get("%s/api/v1/telemetry/central/clusters/inventory/%s" % (CTH_SERVICE,clusterId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_cluster_metrics(self, clusterId, **kwargs):
        valid_query_params = ["target"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/telemetry/central/clusters/metrics/%s" % (CTH_SERVICE,clusterId), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_get_central(self):
        res = requests.get("%s/api/v1/telemetry/central" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_update_central(self):
        res = requests.put("%s/api/v1/telemetry/central" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def telemetry_register_agent(self):
        res = requests.post("%s/api/v1/telemetry/agent/register" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    

    def telemetry_delete_agent(self, agentId):
        res = requests.delete("%s/api/v1/telemetry/agent/register/%s" % (CTH_SERVICE,agentId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    

    def telemetry_get_agent(self, agentId):
        res = requests.get("%s/api/v1/telemetry/agent/register/%s" % (CTH_SERVICE,agentId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def telemetry_update_agent(self, agentId):
        res = requests.put("%s/api/v1/telemetry/agent/register/%s" % (CTH_SERVICE,agentId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def telemetry_agent_streaming(self):
        res = requests.post("%s/api/v1/telemetry/agent/streaming" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_agent_monitor(self, agentId, **kwargs):
        valid_query_params = ["target"]
        query_params = {k: v for (k, v) in kwargs.items() if k in valid_query_params}
        res = requests.get("%s/api/v1/telemetry/agent/monitor/%s" % (CTH_SERVICE,agentId), params=query_params)
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data

    def telemetry_agent_inventory(self, agentId):
        res = requests.get("%s/api/v1/telemetry/agent/inventory/%s" % (CTH_SERVICE,agentId))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def telemetry_agent_entities(self):
        res = requests.get("%s/api/v1/telemetry/agent/entities" % (CTH_SERVICE))
        data = {'status_code': res.status_code}
        if res.status_code == 200:
            data = json.loads(res.text)
            data['status_code'] = 200
        return data
    
    def close(self):
        self.session.close()

