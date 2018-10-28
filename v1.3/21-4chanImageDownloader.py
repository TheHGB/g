#Shit is slow as fuck, but I did not want to spend more time learning the API nor the wrap, so there you go

import basc_py4chan
import urllib

board = basc_py4chan.Board(raw_input("Which board do you want to explore? "))
print "Thread Id - Subject"
for thread_id in board.get_all_thread_ids():
    try: #To lazy to check for Unicode
        print str(thread_id) + " - " + str(board.get_thread(thread_id).topic.subject)
    except:
        pass
thread = board.get_thread(raw_input("Input the thread id you want the images from "))
files= a.files()
for f in files:
    print f

urllib.urlretrieve("http://i.4cdn.org/b/1540734957527.jpg", ""+f[-4::])

