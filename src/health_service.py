import json

class HealthService:
    def get_health_package(self) -> str:
        return json.dumps({"status" : "OK"})
