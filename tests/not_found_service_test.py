import unittest
from src import not_found_service

class TestNotFoundService(unittest.TestCase):

    def test_404_package(self):
        service = not_found_service.NotFoundService()
        self.assertEqual(service.get_404_package(), str("NOT FOUND"))

if __name__ == '__main__':
    unittest.main()