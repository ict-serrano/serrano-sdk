import unittest
import os.path
from serrano_sdk.enhanced_service_orchestrator.client import AIEnhancedServiceOrchestrator

class AIEnhancedServiceOrchestratorTestCase(unittest.TestCase):

    def setUp(self):
        self.enhanced_service_orchestrator_api = AIEnhancedServiceOrchestrator(os.path.join(os.path.dirname(__file__), "sdk_config.json"))


    def test_is_ready(self):
        """Test is ready"""

        result = self.enhanced_service_orchestrator_api.is_ready()
        self.assertEqual(result.status_code, 400)
        self.enhanced_service_orchestrator_api.close()

if __name__ == '__main__':
    unittest.main()