import service_factory

class MetricsController:
    def __init__(self, svc_factory, config):
        self.service_factory = svc_factory
        self.config = config

    def route(self, http_response, route):
        if route == buildRoute("health", self.config):
            _get_health(self.service_factory.build(service_factory.ServiceType.HEALTH), http_response)

def _get_health(service, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(service.get_health_package())

def buildRoute(route, config): # For K8's routing and local routing
    namespace = config.get_namespace()
    service = config.get_service()
    if namespace == None or namespace == "" or service == None or service == "":
        return f"/{route}"
    return f"/{namespace}/{service}/{route}"