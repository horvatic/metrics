import unittest
from src import metircs_service

class TestMetircsService(unittest.TestCase):

    def test_get_metircs_package(self):
        service = metircs_service.MetircsService(MockSystem())
        self.assertEqual(service.get_metircs_package(), _response())

class MockSystem:
    def cpu_usage(self):
        return 50


def _response() -> str:
    return str({ 
        "cpu" : { 
            "usage" : 50
        }
    })

if __name__ == '__main__':
    unittest.main()