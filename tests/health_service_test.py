import unittest # Unit testing framework
import json
from src import health_service 

class TestHealthService(unittest.TestCase): # Test class
    def test_health_package(self): # Test function
        service = health_service.HealthService() # Create the service
        
        self.assertEqual(service.get_health_package(), json.dumps({"status" : "OK"})) # Test the service

if __name__ == '__main__': # Unit testing boilerplate code
    unittest.main()