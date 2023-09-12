import unittest
import os.path
from serrano_sdk.enhanced_service_orchestrator.client import AIEnhancedServiceOrchestrator

appId = "testID1"
params = "test"
params_object = {"user_id": "1",}
class AIEnhancedServiceOrchestratorTestCase(unittest.TestCase):

    def setUp(self):
        self.enhanced_service_orchestrator_api = AIEnhancedServiceOrchestrator(os.path.join(os.path.dirname(__file__), "sdk_config.json"))
    # Need to check the endpoints
    # def test_create_deployment_scenarios(self):
    #     result = self.enhanced_service_orchestrator_api.create_deployment_scenarios(params_object)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()
    # def test_application_deployment_through_ro(self):
    #     result = self.enhanced_service_orchestrator_api.application_deployment_through_ro(params_object)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()
    # def test_application_management(self):
    #     result = self.enhanced_service_orchestrator_api.application_management(appid, "START", params)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()def test_create_deployment_scenarios(self):
    #     result = self.enhanced_service_orchestrator_api.create_deployment_scenarios(params_object)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()
    # def test_application_deployment_through_ro(self):
    #     result = self.enhanced_service_orchestrator_api.application_deployment_through_ro(params_object)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()
    # def test_application_management(self):
    #     result = self.enhanced_service_orchestrator_api.application_management(appid, "START", params)
    #     self.assertEqual(201, result["status_code"])
    #     self.enhanced_service_orchestrator_api.close()

    # def test_testing_central_telemetry_handler(self):
    #     result = self.enhanced_service_orchestrator_api.testing_central_telemetry_handler()
    #     self.assertEqual(result["status_code"], 200)
    #     self.enhanced_service_orchestrator_api.close()

if __name__ == '__main__':
    unittest.main()