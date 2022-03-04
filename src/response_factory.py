import response
import cpu
import system

class ResponseFactory:
    def __init__(self):
        self.res = response.Response(cpu.Cpu(system.System))

    def build(self):
        return self.res