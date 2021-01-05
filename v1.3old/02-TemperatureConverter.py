units = raw_input("Which scale is your imput using? (C,F,K)\n")

while units.upper() not in ("F","C","K"):
    print "Sorry, I don't know scale "+ units.upper() +"\n"
    units = raw_input("Which scale is your input using? (C,F,K)\n")


while True:
    try:
        temp = float(input("Which temperature do you wish to convert?"))
        break
    except :
        print "Please, enter a valid value"


if units.upper() == "C":
    print str(temp) + "C is " + str(temp*1.8+32) + "F and " + str(temp + 273.15) + "K" 
elif units.upper() == "K":
    print str(temp) + "K is " + str((temp-273.15)*1.8+32) + "F and " + str(temp - 273.15) + "C" 
else:
    print str(temp) + "F is " + str((temp-32)/1.8) + "C and " + str((temp-32)/1.8 + 273.15) + "K" 
