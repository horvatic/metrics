import health_service
from enum import Enum

class ServiceType(Enum):
    HEALTH = 1

class ServiceFactory:
    def __init__(self):
        self.health_service = health_service.HealthService()

    def build(self, service_type):
        if service_type == ServiceType.HEALTH:
            return self.health_service
        else:
            None