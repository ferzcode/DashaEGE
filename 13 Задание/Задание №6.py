# 00000000 = 0
# 10000000 = 128
# 11000000 = 192
# 11100000 = 224
# 11110000 = 240
# 11111000 = 248
# 11111100 = 252
# 11111110 = 254
# 11111111 = 255
from ipaddress import ip_network

def proverka(ip):
    b = bin(int(ip))[2:].zfill(32) # Двоичная запись ip
    levie = b[:16]
    pravie = b[16:]

    if levie.count('1') >= pravie.count('1'):
        return True
    else:
        return False


params = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for A in params:
    net = ip_network(f'252.63.194.3/255.255.{A}.0', False)

    if all(proverka(ip) == True for ip in net):
        print(A)