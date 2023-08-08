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

if __name__ == '__main__':
    unittest.main()