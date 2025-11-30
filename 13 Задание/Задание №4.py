from ipaddress import *

for mask in range(0, 33):
    net1 = ip_network(f'157.127.172.56/{mask}', False)
    net2 = ip_network(f'157.127.191.78/{mask}', False)

    if net1 != net2 and str(net1[0]) != '157.127.172.56' and str(net2[0]) != '157.127.191.78':
        print(mask)