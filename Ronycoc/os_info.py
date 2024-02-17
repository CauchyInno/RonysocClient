import psutil
from socket import gethostname
from getpass import getuser

def os_info_message() -> str:
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    return (f"host_name : {gethostname()}\n"
    f"user: {getuser()}\n"
    f"cpu_usage: {round(os_cpu_avg_pct(), 2)}\n"
    f"memory_usage: {round(memory_info.used / 1024 ** 2, 1)} MB / {round(memory_info.total / 1024 ** 2, 1)} MB {round(memory_info.percent, 1)} %\n"
    f"disk_usage: {round(disk_info.used / 1024 ** 3, 1)} GB / {round(disk_info.total / 1024 ** 3, 1)} GB {round(disk_info.percent, 1)} %\n")

def os_cpu_avg_pct():
    cpu_pct = psutil.cpu_percent(percpu=True)
    cpu_avg_pct = sum(cpu_pct) / len(cpu_pct)
    return cpu_avg_pct