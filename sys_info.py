#https://www.thepythoncode.com/article/get-hardware-system-information-python

import psutil
import platform

sys_file = open("sys_info.html", 'w')

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#получать информацию о процессоре, памяти, диске, сети, датчиках и запущенных процессах в системе
# let's print CPU information
sys_file.write("<h1>CPU Info</h1>")
# number of cores
sys_file.write(f"Physical cores: {psutil.cpu_count(logical=False)}<br>")
sys_file.write(f"Total cores: {psutil.cpu_count(logical=True)}<br>")
# CPU frequencies
cpufreq = psutil.cpu_freq()
sys_file.write(f"Max Frequency: {cpufreq.max:.2f}Mhz<br>")
sys_file.write(f"Min Frequency: {cpufreq.min:.2f}Mhz<br>")
sys_file.write(f"Current Frequency: {cpufreq.current:.2f}Mhz<br>")

sys_file.write("<h1>Memory Information</h1>")
# get the memory details
svmem = psutil.virtual_memory()
sys_file.write(f"Total: {get_size(svmem.total)}<br>")
sys_file.write(f"Available: {get_size(svmem.available)}<br>")

# Disk Information
sys_file.write("<h1>Disk Information</h1>")
sys_file.write("<h2>Partitions and Usage:</h2>")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    sys_file.write(f"=== Device: {partition.device} ===<br>")
    sys_file.write(f"  Mountpoint: {partition.mountpoint}<br>")
    sys_file.write(f"  File system type: {partition.fstype}<br>")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    sys_file.write(f"  Total Size: {get_size(partition_usage.total)}<br>")
    sys_file.write(f"  Used: {get_size(partition_usage.used)}<br>")
    sys_file.write(f"  Free: {get_size(partition_usage.free)}<br>")
    sys_file.write(f"  Percentage: {partition_usage.percent}%<br>")
    # Network information
sys_file.write("<h1>Network Information</h1>")
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        sys_file.write(f"=== Interface: {interface_name} ===<br>")
        if str(address.family) == 'AddressFamily.AF_INET':
            sys_file.write(f"  IP Address: {address.address}<br>")
            sys_file.write(f"  Netmask: {address.netmask}<br>")
            sys_file.write(f"  Broadcast IP: {address.broadcast}<br>")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            sys_file.write(f"  MAC Address: {address.address}<br>")
            sys_file.write(f"  Netmask: {address.netmask}<br>")
            sys_file.write(f"  Broadcast MAC: {address.broadcast}<br>")
# get IO statistics since boot
net_io = psutil.net_io_counters()
sys_file.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}<br>")
sys_file.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}<br>")

sys_file.write("<h2>Battery Information</h2>")
bat_inf = psutil.sensors_battery()
sys_file.write(f'{bat_inf}')
