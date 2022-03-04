class MetircsService:
    def __init__(self, system):
        self.system = system

    def get_metircs_package(self) -> str:
        return str({ 
        "cpu" : { 
            "usage" : self.system.cpu_usage()
        } 
    })