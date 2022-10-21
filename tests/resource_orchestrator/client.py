import unittest

from serrano_sdk.resource_orchestrator.client import ResourceOrchestrator


class ResourceOrchestratorTestCase(unittest.TestCase):

    def setUp(self):
        self.resource_orchestrator = ResourceOrchestrator(2)

    def test_employ(self):
        """Test employ"""

        result = self.resource_orchestrator.employ()
        self.assertEqual(result.status_code, 200)
        self.resource_orchestrator.close()

if __name__ == '__main__':
    unittest.main()