import unittest
import os.path
from serrano_sdk.resource_orchestrator.client import ResourceOrchestrator


class ResourceOrchestratorTestCase(unittest.TestCase):

    def setUp(self):
        self.rot_api = ResourceOrchestrator(os.path.join(os.path.dirname(__file__), "sdk_config.json"))

    def test_is_ready(self):
        """Test is_ready"""

        result = self.rot_api.is_ready()
        self.assertEqual(result.status_code, 404) #update this when server is fixed
        self.rot_api.close()

if __name__ == '__main__':
    unittest.main()