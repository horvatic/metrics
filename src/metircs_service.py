import json

class MetircsService:
    def __init__(self, system):
        self.system = system

    def get_metircs_package(self) -> str:
        return json.dumps({ 
        "cpu" : { 
            "usage" : self.system.cpu_usage()
        }, 
        "ram" : {
            "usage" : self.system.ram_usage()
        }
    })