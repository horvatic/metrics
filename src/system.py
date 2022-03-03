import psutil

class System:
    def cpu_usage() -> int:
        return psutil.cpu_percent(1)
