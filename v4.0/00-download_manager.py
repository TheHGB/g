import requests
import argparse
import threading
from pathlib import Path


class download (threading.Thread):
   def __init__(self, url, name):
      threading.Thread.__init__(self)
      self.url = url
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      downloading(self.name, self.url)
      print ("Exiting " + self.name)

def downloading(file_url, file_name):

    # Download the file
    try:
        file_content = requests.get(file_url)
    except requests.exceptions.RequestException as e:
        raise SysteExit(e)

    # Check if the user provided a name. If not, use the name of the file in the URL
    if not file_name:
        file_name = file_url.split('/')[-1].split('?')[0]

    # Check if a file with the same name already exists in the system. If it does, add Copy before the file extension
    while Path(file_name).is_file():
        file_name = str(Path(file_name).parent)+'/'+Path(file_name).stem+'-COPY'+Path(file_name).suffix

    # Write the file
    with open(file_name, 'wb') as f:
        f.write(file_content.content)

    print ('Download of {} completed'.format(file_name))


i = 0
threads = []
while True:
    option = input("Wanna download something? ")

    if option.lower() == 'yes' or option.lower() == 'y':
        url = input("Enter the URL of the file: ")
        name = input("Enter the name  of the file: ")
        i = download(name, url)
        i.start()
        threads.append(i)

    elif option.lower()== 'no' or option.lower() == 'n':
        print ('Waiting for all downloads to finish')
        for t in threads:
            t.join()
        break
    else:
        print("I don't understand")
