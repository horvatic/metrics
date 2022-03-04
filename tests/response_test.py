import unittest
from src import response

class TestResponse(unittest.TestCase):

    def test_get_cpu_package(self):
        res = response.Response(MockCpu())
        self.assertEqual(res.get_cpu_package(), _response())

    def test_health_package(self):
        res = response.Response(MockCpu())
        self.assertEqual(res.get_health_package(), str({"status" : "OK"}))

    def test_404_package(self):
        res = response.Response(MockCpu())
        self.assertEqual(res.get_404_package(), str("NOT FOUND"))

class MockCpu:
    def info(self):
        return 50


def _response() -> str:
    return str({ 
        "cpu" : { 
            "usage" : 50
        } 
    })

if __name__ == '__main__':
    unittest.main()