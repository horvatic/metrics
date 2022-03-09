import service_factory

class Controller:
    def __init__(self, svc_factory, config):
        self.service_factory = svc_factory
        self.config = config

    def route(self, http_response, route):
        if route == buildRoute("health", self.config):
            _get_health(self.service_factory.build(service_factory.ServiceType.HEALTH), http_response)
        else:
            _404(self.service_factory.build(service_factory.ServiceType.NOT_FOUND), http_response)

def _get_health(service, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(service.get_health_package())

def _404(service, http_response):
    http_response.set_status_code(404)
    http_response.set_content_type("text/plain")
    http_response.set_status_content(service.get_404_package())

def buildRoute(route, config): # For K8's routing and local routing
    namespace = config.get_namespace()
    service = config.get_service()
    if namespace == None or namespace == "" or service == None or service == "":
        return f"/{route}"
    return f"/{namespace}/{service}/{route}"