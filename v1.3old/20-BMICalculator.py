height = float(raw_input("What is your height (in meters)? "))
weight = float(raw_input("What is your weight (in kilograms)? "))

print "Your BMI is " + str(weight/pow(height,2)) + " kilos per sqared meter"
