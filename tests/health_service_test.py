import unittest
import json
from src import health_service

class TestHealthService(unittest.TestCase):


    def test_health_package(self):
        service = health_service.HealthService()
        self.assertEqual(service.get_health_package(), json.dumps({"status" : "OK"}))

    def test_health_package(self):
        service = health_service.HealthService()
        self.assertEqual(service.get_health_package(), json.dumps({"status" : "Failed"}))

if __name__ == '__main__':
    unittest.main()