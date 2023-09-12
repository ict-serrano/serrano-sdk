import unittest
import os.path
from serrano_sdk.resource_orchestrator.client import ResourceOrchestrator

bundles_url = "api/v1/orchestrator/bundles"
deployments_url= "/api/v1/orchestrator/deployments"
storage_policy_url="/api/v1/orchestrator/storage_policies"
assignments_url="/api/v1/orchestrator/assignments"
class ResourceOrchestratorTestCase(unittest.TestCase):

    def setUp(self):
        self.rot_api = ResourceOrchestrator(os.path.join(os.path.dirname(__file__), "sdk_config.json"))
    def test_get_deployments(self):
        result = self.rot_api.get_deployments(deployments_url)
        self.assertEqual(result["status_code"], 200)
        self.rot_api.close()
    def test_get_deployment_info(self):
        result = self.rot_api.get_deployment_info(deployments_url, uuid="649decae-63ec-40cb-9c5f-eb16f5b93590")
        print(result)
        self.assertEqual(result["status_code"], 200)
        self.rot_api.close()
    def test_get_storage_policies(self):
        result = self.rot_api.get_storage_policies(storage_policy_url)
        self.assertEqual(result["status_code"], 200)
        self.rot_api.close()
    # Receive 404 from endpoints
    # def test_get_assignments(self):
    #     result = self.rot_api.get_assignments(assignments_url)
    #     print(result)
    #     self.assertEqual(result["status_code"], 400) # update this when is ready
    #     self.rot_api.close()
    # def test_get_bundles(self):
    #     result = self.rot_api.get_bundles(bundles_url)
    #     self.assertEqual(result.status_code, 400)  # update this when server is fixed
    #     self.rot_api.close()


if __name__ == '__main__':
    unittest.main()