import unittest
import os.path
from serrano_sdk.pmds.client import PMDS

UVT_CLUSTER = "7628b895-3a91-4f0c-b0b7-033eab309891"
NBFC_CLUSTER = "5a075716-7d7d-4b40-9566-bc1a33ee70c2"

class PMDSTestCase(unittest.TestCase):

    def setUp(self):
        self.pmds = PMDS(os.path.join(os.path.dirname(__file__), "sdk_config.json"))

    def test_query_nodes_no_params(self):
        """Test query_nodes with no parameters"""

        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER)
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

        
    def test_query_deployments_no_params(self):
        """Test query_deployments with no parameters"""

        result = self.pmds.pmds_service_query_deployments(UVT_CLUSTER, "integration")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_pods_no_params(self):
        """Test query_pods with no parameters"""

        result = self.pmds.pmds_service_query_pods(UVT_CLUSTER, "integration")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_pvs_no_params(self):
        """Test query_pvs with no parameters"""

        result = self.pmds.pmds_service_query_pvs(UVT_CLUSTER)
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    #################
    #   EXAMPLES    #   note: param format = raw causing two tests to fail
    #################

    # query_nodes_examples

    def test_query_nodes_example_1(self):
        # Get collected data in "general" group for all nodes in the k8s cluster, for the last 24hours
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, start="-24h")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_nodes_example_2(self):
        # Get collected data in "memory" group for all nodes in the k8s cluster, for a specific timeframe
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, group="memory", start="-4h", stop="-1h")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_nodes_example_3(self):
        # Get collected data in "storage" group for all nodes in the k8s cluster, for the last 1 hour, using the raw format
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, group="storage", start="-1h", format="raw")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_nodes_example_4(self):
        # Get collected data in "cpu" group for worker node "serrano-k8s-worker-03" the last 6 hours
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, group="cpu", node_name="serrano-k8s-worker-03", start="-6h")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_nodes_example_5(self):
        # Get collected data in "cpu" group  using a specific timeframe
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, group="cpu",  start="1676293139", stop="1676390944")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_nodes_example_6(self):
        # Get collected data for specific metric in group 'memory' in all nodes and for specific timeframe
        result = self.pmds.pmds_service_query_nodes(UVT_CLUSTER, group="memory", field_measurement="node_memory_MemUsed_bytes", start="-6h", stop="-30m")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()


    # query_deployments_examples

    def test_query_deployments_example_1(self):
        # Get collected data for all deployments in "integration" namespace the last 8 hours
        result = self.pmds.pmds_service_query_deployments(UVT_CLUSTER, "integration", start="-8h")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_deployments_example_2(self):
        # Get collected data for all deployments in "integration" namespace the last 1 hour, using the raw format
        result = self.pmds.pmds_service_query_deployments(UVT_CLUSTER, "integration", start="-1h", format="raw")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    # query_pods_examples


    def test_query_pods_example_1(self):
        # Get collected data for all pods in "integration" namespace the last 12 hours
        result = self.pmds.pmds_service_query_pods(UVT_CLUSTER, "integration", start="-12h")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_pods_example_2(self):
        # Get collected data for all pods in "integration" namespace that run on node "serrano-k8s-worker-01"
        # for Monday 13/03 (start="1676239200" , stop="1676325599")
        result = self.pmds.pmds_service_query_pods(UVT_CLUSTER, "integration", node_name="serrano-k8s-worker-02", start="1676239200", stop="1676325599")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()

    def test_query_pods_example_3(self):
        # Get all collected data for a specifc pod "serrano-k8s-probe-6dfc6bcd49-98kp4" in "integration" namespace for the last two days
        result = self.pmds.pmds_service_query_pods(UVT_CLUSTER, "integration", name="serrano-k8s-probe-6dfc6bcd49-98kp4", start="-2d")
        self.assertEqual(result['status_code'], 200)
        self.pmds.close()


if __name__ == '__main__':
    unittest.main()