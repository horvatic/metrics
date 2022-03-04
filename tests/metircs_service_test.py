import unittest
import json
from src import metircs_service

class TestMetircsService(unittest.TestCase):

    def test_get_metircs_package(self):
        service = metircs_service.MetircsService(MockSystem())
        self.assertEqual(service.get_metircs_package(), _response())

class MockSystem:
    def cpu_usage(self):
        return 50
    def ram_usage(self):
        return 40


def _response() -> str:
    return json.dumps({ 
        "cpu" : { 
            "usage" : 50
        }, "ram" : {
            "usage" : 40
        }
    })

if __name__ == '__main__':
    unittest.main()