import response
import cpu
import system

_res = response.Response(cpu.Cpu(system.System))

def build():
    return _res