import psutil

class System:
    def cpu_usage() -> float:
        return psutil.cpu_percent(1)
    def ram_usage() -> float:
        return psutil.virtual_memory().percent
