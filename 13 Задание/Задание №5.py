from ipaddress import *

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32) # Двоичная запись ip
    levie = b[:16]
    pravie = b[16:]

    if levie.count('1') <= pravie.count('1'):
        return True
    else:
        return False



for A in range(0, 256):
    net = ip_network(f'32.0.{A}.5/255.255.240.0', False)

    if all(proverka(ip) == True for ip in net):
        print(A)