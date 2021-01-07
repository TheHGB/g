import argparse

#Definition of the arguments for the script
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--units", help="Units of the value", required=True)
parser.add_argument("-v", "--value", help="Value you want to transform", required=True)
args = parser.parse_args()

unit = args.units
val = float(args.value)

if unit == 'miles' or unit == 'mi':
    print ("{} miles are {} kilometers".format(val, val*1.609344))
elif unit == 'kilometers' or unit == 'km':
    print ("{} kilometers are {} miles".format(val, val/1.609344))
elif unit == 'yards' or unit == 'yd':
    print ("{} yards are {} meters".format(val, val*0.9144))
elif unit == 'meters' or unit == 'm':
    print ("{} meters are {} yards".format(val, val/0.9144))
elif unit == 'inches' or unit == 'in':
    print ("{} inches are {} centimiters".format(val, val*2.54))
    print ("{} inches are {} feet and {}".format(val, val/12))
elif unit == 'feet' or unit == 'ft':
    print ("{} feet are {} centimiters".format(val, val*30.48))
    print ("{} feet are {} inches".format(val, val*12))
elif unit == 'centimiters' or unit == 'cm':
    print ("{} centimiters are {} feet and {} inches".format(val, int(val/30.48), ((val/30.48)%1)*12))
    print ("{} centimiters are {} inches".format(val, val/2.54))
elif unit == 'pound' or unit == 'lb':
    print ('{} pounds are {} kilograms'.format(val, val*0.454))
    print ('{} pounds are {} ounces'.format(val, val*16))
elif unit == 'ounces' or unit == 'oz':
    print ('{} ounces are {} grams'.format(val, val*28.35))
    print ('{} ounces are {} pounds'.format(val, val/16))
elif unit == 'grams' or unit == 'g':
    print ('{} grams are {} ounces'.format(val, val/28.35))
elif unit == 'kilograms' or unit == 'kg':
    print ('{} kilograms are {} punds and {} ounces'.format(val, int(val/0.454), ((val/0.454)%1)*16))
