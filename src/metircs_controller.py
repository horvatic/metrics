class MetricsController:
    def __init__(self, res_factory):
        self.res_factory = res_factory

    def route(self, http_response, route):
        res = self.res_factory.build()
        if route == "/metircs":
            _get_metircs(res, http_response)
        elif route == "/health":
            _get_health(res, http_response)
        else:
            _404(res, http_response)

def _get_metircs(res, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(res.get_cpu_package())

def _get_health(res, http_response):
    http_response.set_status_code(200)
    http_response.set_content_type("application/json")
    http_response.set_status_content(res.get_health_package())

def _404(res, http_response):
    http_response.set_status_code(404)
    http_response.set_content_type("text/plain")
    http_response.set_status_content(res.get_404_package())