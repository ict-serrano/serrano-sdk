import unittest

from serrano_sdk.telemetry.client import Telemetry

uuid = "cb8cce21-d0d1-4638-beee-081dafe63621"

class TelemetryTestCase(unittest.TestCase):

    def setUp(self):
        self.telemetry = Telemetry(2)

    def test_employ(self):
        """Test employ"""

        result = self.telemetry.employ()
        self.assertEqual(result.status_code, 200)
        self.telemetry.close()

    
    def test_telemetry_probe_monitor(self):
        result = self.telemetry.telemetry_probe_monitor()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_probe_inventory(self):
        result = self.telemetry.telemetry_probe_inventory()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_probe_collection(self):
        result = self.telemetry.telemetry_probe_collection()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_probe_streaming(self):
        result = self.telemetry.telemetry_probe_streaming(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_query_clusters(self):
        result = self.telemetry.telemetry_query_clusters()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_query_cluster(self):
        result = self.telemetry.telemetry_query_cluster(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    
    def test_telemetry_cluster_monitor(self):
        result = self.telemetry.telemetry_cluster_monitor(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_cluster_inventory(self):
        result = self.telemetry.telemetry_cluster_inventory(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()
    
    def test_telemetry_cluster_metrics(self):
        result = self.telemetry.telemetry_cluster_metrics(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    
    def test_telemetry_get_central(self):
        result = self.telemetry.telemetry_get_central()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_update_central(self):
        result = self.telemetry.telemetry_update_central()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    def test_telemetry_register_agent(self):
        result = self.telemetry.telemetry_register_agent()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_delete_agent(self):
        result = self.telemetry.telemetry_delete_agent(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    def test_telemetry_get_agent(self):
        result = self.telemetry.telemetry_get_agent(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_update_agent(self):
        result = self.telemetry.telemetry_update_agent(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_agent_streaming(self):
        result = self.telemetry.telemetry_agent_streaming()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    def test_telemetry_agent_monitor(self):
        result = self.telemetry.telemetry_agent_monitor(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_agent_inventory(self):
        result = self.telemetry.telemetry_agent_inventory(uuid)
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_agent_entities(self):
        result = self.telemetry.telemetry_agent_entities()
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    #################
    #   EXAMPLES    #
    #################


    def test_telemetry_cluster_metrics_example_1(self):
        # Get from the Operational Database all the available monitoring samples for the "UVT Production" cluster
        result = self.telemetry.telemetry_cluster_metrics("7628b895-3a91-4f0c-b0b7-033eab309891", target="all")
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    def test_telemetry_cluster_metrics_example_2(self):
        # Get from the Operational Database the latest monitoring sample for the "NBFC" cluster
        result = self.telemetry.telemetry_cluster_metrics("5a075716-7d7d-4b40-9566-bc1a33ee70c2")
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()


    def test_telemetry_cluster_monitor_example_1(self):
        # Query directly the "UVT Production" cluster to retrieve all the latest monitoring information
        result = self.telemetry.telemetry_cluster_monitor("7628b895-3a91-4f0c-b0b7-033eab309891")
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

    def test_telemetry_cluster_monitor_example_2(self):
        # Query directly the "NBFC" cluster to retrieve only the latest monitoring information for the worker nodes
        result = self.telemetry.telemetry_cluster_monitor("5a075716-7d7d-4b40-9566-bc1a33ee70c2", target="resources")
        self.assertEqual(result['status_code'], 200)
        self.telemetry.close()

if __name__ == '__main__':
    unittest.main()