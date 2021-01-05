number = input("Enter an integer:")
org = number
steps = 0


while number is not 1:
    if (int(number) % 2):
        number = number*3+1    
    else:
        number = number/2
    print number
    steps = steps + 1
print "The number " + str(org) + " arrives at 1 with " + str(steps) + " steps"  
