import service_factory

class MetricsController:
    def __init__(self, svc_factory):
        self.service_factory = svc_factory

    def route(self, http_response, route):
        if route == "/metircs":
            _get_metircs(self.service_factory.build(service_factory.ServiceType.METIRCS), http_response)
        elif route == "/health":
            _get_health(self.service_factory.build(service_factory.ServiceType.HEALTH), http_response)
        else:
            _404(self.service_factory.build(service_factory.ServiceType.NOT_FOUND), http_response)

def _get_metircs(service, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(service.get_metircs_package())

def _get_health(service, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(service.get_health_package())

def _404(service, http_response):
    http_response.set_status_code(404)
    http_response.set_content_type("text/plain")
    http_response.set_status_content(service.get_404_package())