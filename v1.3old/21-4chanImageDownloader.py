#Shit is slow as fuck, but I did not want to spend more time learning the API nor the wrap, so there you go

import basc_py4chan
import urllib
import os

board = basc_py4chan.Board(raw_input("Which board do you want to explore? "))

print "Thread Id - Subject"
for thread_id in board.get_all_thread_ids():
    try: #To lazy to check for Unicode
        print str(thread_id) + " - " + str(board.get_thread(thread_id).topic.subject)
    except:
        pass

thread = board.get_thread(raw_input("Input the thread id you want the images from: "))
files = thread.files()

folder = raw_input("Name the directory where the images will be stored: ")
os.mkdir(folder)
counter = 1
for f in files:
    #I know this fails with webm, but they still werks with the name fucked up, so roll with it
    urllib.urlretrieve(f, folder+"/"+str(counter)+f[-4::]) 
    counter += 1


