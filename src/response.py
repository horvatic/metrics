class Response:
    def __init__(self, cpu):
        self.cpu = cpu

    def get_cpu_package(self) -> str:
        return str({ 
        "cpu" : { 
            "usage" : self.cpu.info()
        } 
    })

    def get_health_package(self) -> str:
        return str({"status" : "OK"})

    def get_404_package(self) -> str:
        return "NOT FOUND"