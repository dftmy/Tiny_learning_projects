import re
open_file = open("2.txt", 'r')
read_file = open_file.read()
ips = re.findall(r'\d\d[.]\d\d\d[.]\d\d\d[.]\d\d\d' , read_file)
unique_ips = (set(ips))
print(unique_ips)