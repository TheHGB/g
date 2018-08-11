for number in range(0,1000000):
    if number % 3 is 0:
        if number % 5 is 0:
            print "FizzBuzz"
        else:
            print "Fizz"
    elif number % 5 is 0:
        print "Buzz"
    else:
        print number
