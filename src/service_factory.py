import metircs_service
import health_service
import not_found_service
import system
from enum import Enum

class ServiceType(Enum):
    METIRCS = 1
    HEALTH = 2
    NOT_FOUND = 3

class ServiceFactory:
    def __init__(self):
        self.metircs_service = metircs_service.MetircsService(system.System)
        self.health_service = health_service.HealthService()
        self.not_found_service = not_found_service.NotFoundService()

    def build(self, service_type):
        if service_type == ServiceType.METIRCS:
            return self.metircs_service
        elif service_type == ServiceType.HEALTH:
            return self.health_service
        elif service_type == ServiceType.NOT_FOUND:
            return self.not_found_service
        else:
            None