import unittest
import os
from unittest.mock import MagicMock
from src import metircs_controller
from src import config

class TestMetricsController(unittest.TestCase):

    def test_route_metircs(self):
        route = "/metircs"
        mock_http_response = MockHttpResponse()
        mock_service_factory = MockServiceFactory()
        mock_config = config.Config()
        mock_config.get_namespace = MagicMock(return_value=None)
        mock_config.get_service = MagicMock(return_value=None)
        controller = metircs_controller.MetricsController(mock_service_factory, mock_config)

        controller.route(mock_http_response, route)

        self.assertEqual(200, mock_http_response.status_code)
        self.assertEqual(_response(), mock_http_response.content)
        self.assertEqual("application/json", mock_http_response.content_type)

    def test_route_metircs_with_env_set(self):
        route = "/dev/metric/metircs"
        mock_http_response = MockHttpResponse()
        mock_service_factory = MockServiceFactory()
        mock_config = config.Config()
        mock_config.get_namespace = MagicMock(return_value="dev")
        mock_config.get_service = MagicMock(return_value="metric")
        controller = metircs_controller.MetricsController(mock_service_factory, mock_config)

        controller.route(mock_http_response, route)

        self.assertEqual(200, mock_http_response.status_code)
        self.assertEqual(_response(), mock_http_response.content)
        self.assertEqual("application/json", mock_http_response.content_type)
    
    def test_route_404(self):
        route = "/willneverfind"
        mock_http_response = MockHttpResponse()
        mock_service_factory = MockServiceFactory()
        mock_config = config.Config()
        mock_config.get_namespace = MagicMock(return_value=None)
        mock_config.get_service = MagicMock(return_value=None)
        controller = metircs_controller.MetricsController(mock_service_factory, mock_config)

        controller.route(mock_http_response, route)

        self.assertEqual(404, mock_http_response.status_code)
        self.assertEqual("NOT FOUND", mock_http_response.content)
        self.assertEqual("text/plain", mock_http_response.content_type)

    def test_route_health(self):
        route = "/health"
        mock_http_response = MockHttpResponse()
        mock_service_factory = MockServiceFactory()
        mock_config = config.Config()
        mock_config.get_namespace = MagicMock(return_value=None)
        mock_config.get_service = MagicMock(return_value=None)
        controller = metircs_controller.MetricsController(mock_service_factory, mock_config)

        controller.route(mock_http_response, route)

        self.assertEqual(200, mock_http_response.status_code)
        self.assertEqual(str({"status" : "OK"}), mock_http_response.content)
        self.assertEqual("application/json", mock_http_response.content_type)

    def test_route_health_with_env(self):
        route = "/dev/metric/health"
        mock_http_response = MockHttpResponse()
        mock_service_factory = MockServiceFactory()
        mock_config = config.Config()
        mock_config.get_namespace = MagicMock(return_value="dev")
        mock_config.get_service = MagicMock(return_value="metric")
        controller = metircs_controller.MetricsController(mock_service_factory, mock_config)

        controller.route(mock_http_response, route)

        self.assertEqual(200, mock_http_response.status_code)
        self.assertEqual(str({"status" : "OK"}), mock_http_response.content)
        self.assertEqual("application/json", mock_http_response.content_type)

def _response() -> str:
    return str({ 
        "cpu" : { 
            "usage" : 50
        }, "ram" : {
            "usage" : 40
        }
    })

class MockService:
    def get_metircs_package(self):
        return _response()
    def get_health_package(self):
        return str({"status" : "OK"})
    def get_404_package(self):
        return str("NOT FOUND")

class MockServiceFactory:
    def build(self, option):
        return MockService()

class MockHttpResponse:
    status_code = 0
    content_type = ""
    content = ""

    def set_status_code(self, new_status_code):
        self.status_code = new_status_code
    def set_content_type(self, new_content_type):
        self.content_type = new_content_type
    def set_status_content(self, new_content):
        self.content = new_content

if __name__ == '__main__':
    unittest.main()