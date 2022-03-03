import unittest
from unittest.mock import MagicMock
from src import cpu
from src import system

class TestCpu(unittest.TestCase):

    def test_usage(self):
        sys = system.System()
        sys.cpu_usage = MagicMock(return_value=40)
        usage = cpu.Cpu(sys)

        self.assertEqual(usage.info(), 40, "Should be 40")

if __name__ == '__main__':
    unittest.main()