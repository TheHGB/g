import os
import binascii
import string

with open('./names.txt') as names:
    names_list = [name.strip() for name in names]    
    
    full_name = [names_list[(int.from_bytes(os.urandom(2),'big'))%len(names_list)] for i in range(3)]

print ("Your new name:")
for i in range(3):
    print(full_name[i] + " ", end = '')

print ("\n\nYour username could be:")
for i in range(3):
    print(full_name[i][:2], end='')

print ("\n\nYour password could be:")
chars = string.ascii_letters+string.digits+string.punctuation 

for i in range(20):
    print(chars[int.from_bytes(os.urandom(1),'big')%len(chars)], end='')

print("\n")


