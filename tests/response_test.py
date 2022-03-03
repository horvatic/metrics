import unittest
from src import response

class TestResponse(unittest.TestCase):

    def test_build(self):
        self.assertEqual(response.build(), "Hello World", "Should be Hello World")

if __name__ == '__main__':
    unittest.main()