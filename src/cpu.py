class Cpu:
    def __init__(self, system):
        self.system = system

    def info(self) -> int:
        return self.system.cpu_usage()