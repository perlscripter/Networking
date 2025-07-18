# For building the socket
import socket

# For system level commands
import sys

# For doing an array in the TCP checksum
import array

# For establishing the packet structure (Used later on), this will allow direct access to the methods and functions in the struct module
from struct import *

# Create a raw socket.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

packet = ''

src_ip = "10.10.0.40"
dst_ip = "172.16.82.106"

# Lets add the IPv4 header information
ip_ver_ihl = 69                       # This is putting the decimal conversion of 0x45 for Version and Internet Header Length
ip_tos = 0                            # This combines the DSCP and ECN fields
ip_len = 0                            # The kernel will fill in the actually length of the packet
ip_id = 12345                         # This sets the IP Identification for the packet
ip_frag = 0                           # This sets fragmentation to off
ip_ttl = 64                           # This determines the TTL of the packet when leaving the machine
ip_proto = 6                          # This sets the IP protocol to 6 (TCP) or 11 (UDP) (reference IANA)
ip_check = 0                          # The kernel will fill in the checksum for the packet
ip_srcadd = socket.inet_aton(src_ip)  # inet_aton(string) will convert an IP address to a 32 bit binary number
ip_dstadd = socket.inet_aton(dst_ip)  # inet_aton(string) will convert an IP address to a 32 bit binary number

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)
