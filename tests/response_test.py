import unittest
from unittest.mock import MagicMock
from src import response
from src import cpu
from src import system

class TestResponse(unittest.TestCase):

    def test_build(self):
        c = cpu.Cpu(system.System)
        c.info = MagicMock(return_value=50)
        res = response.Response(c)
        self.assertEqual(res.build(), _response())

if __name__ == '__main__':
    unittest.main()

def _response() -> str:
    return str({ 
        "cpu" : { 
            "usage" : 50
        } 
    })