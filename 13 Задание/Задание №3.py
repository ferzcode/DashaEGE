from ipaddress import *

for mask in range(0, 33):
    net1 = ip_network(f'216.54.187.235/{mask}', False)
    net2 = ip_network(f'216.54.174.128/{mask}', False)

    if net1 != net2 and str(net1[0]) != '216.54.187.235' and str(net2[0]) != '216.54.174.128':
        print(mask, net1, net2)