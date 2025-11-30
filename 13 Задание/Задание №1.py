from ipaddress import *

c = 0
setochka = ip_network('204.16.168.0/255.255.248.0', False)

for ip in setochka:
    b = bin(int(ip))[2:].zfill(32) # Строка

    if b.count('1') % 5 != 0:
        c += 1
print(c)

