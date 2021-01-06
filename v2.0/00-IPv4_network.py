# This code is not optimal at all. I was testing some things and adapting the code to make it work, its full of workarounds to not have to rethink code

import argparse
import re
import sys

#Definition of the arguments for the script
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP addrss", required=True)
parser.add_argument("-n", "--netmask", help="IP addrss", required=True)
args = parser.parse_args()

#Regex to validate that the netmask and the IP have valid values
extended_netmask_regex = "^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$"
shortened_range_regex = "^[/][1-9]$|^[/][0-2][0-9]$|^[/]3[0-2]$"
ip_address_regex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

# Checking if the IP has a valid value and storing it in a list of 4 binary values
if re.match(ip_address_regex, args.ip):
    ip = list(map(int, args.ip.split('.')))
    bin_ip = ['{0:08b}'.format(int(i)) for i in ip]
else:
    print ('Invalid IP value')
    sys.exit()

# Checking if the netmask has a valid value and storing it a list of 4 binary values
if re.match(extended_netmask_regex, args.netmask):
    netmask = list(map(int, args.netmask.split('.')))
    bin_netmask = ''.join(['{0:08b}'.format(int(i)) for i in netmask])
elif re.match(shortened_range_regex, args.netmask):
    bin_netmask = ''.join(['1' for i in range(int(args.netmask[1:]))])
    bin_netmask = bin_netmask + ''.join(['0' for i in range(32-len(bin_netmask))])
    netmask = [int(bin_netmask[i*8-8:i*8], 2) for i in range(1,5)]
else:
    print ('Invalid netmask value')
    sys.exit()

# Calculating the Network Address using logical AND between IP and Network
print ('The Network address is:')
print (''.join([str(x&y)+'.' for x,y in zip(ip,netmask)])[:-1])

# Separate each value of the binary IP address and substituting the netmask values by to get the broadcast address
bin_ip_list = list(''.join(bin_ip))
for i in range(1,bin_netmask.count('0')):
    bin_ip_list[i*-1] = '1'
bin_ip_list = ''.join(bin_ip_list)
bin_ip_list = [int(bin_ip_list[i*8-8:i*8], 2) for i in range(1,5)]

print ('The broadcast address is:')
print (''.join([str(i)+'.' for i in bin_ip_list])[:-1])

