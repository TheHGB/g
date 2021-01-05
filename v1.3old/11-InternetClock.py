from bs4 import BeautifulSoup
import datetime
import urllib2
response = urllib2.urlopen('https://www.timeanddate.com/')
html = response.read()
soup = BeautifulSoup(html,"html.parser")
minutes = soup.find(attrs={'id' : 'clk_hm'})
seconds = soup.find(attrs={'id' : 'ij0'})
print "Internet Clock: " + minutes.contents[0] + ":" + seconds.contents[0]
print "Internal Clock: " + str(datetime.datetime.now().time())

