from ipaddress import *

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32)

    pravie = b[16:].count('1')

    return pravie > 3


for A in range(0, 256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', False)

    if all(proverka(ip) for ip in net):
        print(A)