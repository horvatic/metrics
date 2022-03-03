
class Response:
    def __init__(self, cpu):
        self.cpu = cpu

    def build(self) -> str:
        return str({ 
        "cpu" : { 
            "usage" : self.cpu.info()
        } 
    })
