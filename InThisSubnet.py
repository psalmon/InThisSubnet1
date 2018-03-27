import socket
import struct
import sys

if len(sys.argv) != 3: #accounting for the one default arg
    sys.exit("invalid args")

ipAddr = struct.unpack('L', socket.inet_aton(sys.argv[1]))[0]
subnet = sys.argv[2]
networkAddr,bits = subnet.split('/')
mask = struct.unpack('L', socket.inet_aton(networkAddr))[0] & ((1 << int(bits)) - 1) #explanation for this bit shift: https://stackoverflow.com/a/1392065

# Article explaining the ANDing process to determine if the ip resides within the subnet mask.
# https://www.hackthissite.org/articles/read/902
if ipAddr & mask == mask:
    print('YES, ' + sys.argv[1] + ' is within subnet: ' + subnet)
else:
    print('NO, ' + sys.argv[1] + ' is NOT within subnet: ' + subnet)

