import health_service
import not_found_service
from enum import Enum

class ServiceType(Enum):
    HEALTH = 1
    NOT_FOUND = 2

class ServiceFactory:
    def __init__(self):
        self.health_service = health_service.HealthService()
        self.not_found_service = not_found_service.NotFoundService()

    def build(self, service_type):
        if service_type == ServiceType.HEALTH:
            return self.health_service
        elif service_type == ServiceType.NOT_FOUND:
            return self.not_found_service
        else:
            None