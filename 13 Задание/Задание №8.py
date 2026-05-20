from ipaddress import *

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32)
    levie = b[:16]
    pravie = b[16:]
    return levie.count('1') >= pravie.count('1')


mask = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for A in mask:
    net = ip_network(f'127.63.67.1/255.255.{A}.0', False)

    if all(proverka(ip) == 1 for ip in net):
        print(A)
