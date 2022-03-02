import unittest
from src import cpu

class TestCpu(unittest.TestCase):

    def test_usage(self):
        self.assertEqual(cpu.cpu_usage(), 50, "Should be 50")

if __name__ == '__main__':
    unittest.main()