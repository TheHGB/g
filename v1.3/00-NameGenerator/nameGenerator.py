import random


f = open("names.txt")
names = f.read().splitlines()

print names[random.randrange(0,len(names))] + " " + names[random.randrange(0,len(names))]
