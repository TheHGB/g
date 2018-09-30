#Only navigation with no movement and listing, just simple stuff, done in 15 min or so

import os
import re

location = "."

while True:
    try:
        command = raw_input()
        if command == "ls":
             content = os.listdir(location)
             for f in content:
                 print f
        elif re.match(r'^cd ', command):
            if len(command.split(" ")) is not 2:
                print "Usage: cd path/to/where/you/want/to/go"
            else:
                if not os.path.isdir(command.split(" ")[1]):
                    print "Please choose a directory"
                else:
                    location = command.split(" ")[1]
        elif command == "exit":
            break
        else:
            print "Command unknown"
    except:
        print "Something went wrong.\nls to list current location\ncd path to change location\nexit to leave"
