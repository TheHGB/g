#It will be like an indian talking 'cause I aint conjugating shit
#All is loaded into memory at once because this is for Chad-tier PCs
import random


adj = open("adj.txt")
subject = open("noun.txt")
verb = open("verb.txt")

adjs = adj.read().splitlines()
names = subject.read().splitlines()
verbs = verb.read().splitlines()

print "The " + adjs[random.randrange(0,len(adjs))] + " " +adjs[random.randrange(0,len(adjs))] + " " + names[random.randrange(0,len(names))] + " " + verbs[random.randrange(0,len(verbs))]+"s" 

adj.close()
subject.close()
verb.close()
