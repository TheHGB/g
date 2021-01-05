import os

with open('./names.txt') as names:
    names_list = [name.strip() for name in names]    
    
for i in range(3):
    print (names_list[(int.from_bytes(os.urandom(2),'big'))%len(names_list)]+ " ", end='')




