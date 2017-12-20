#!/usr/bin/python
import os, re, urllib2, time
from multiprocessing import Process

# Author: Azeem Ilyas
# Title: MultiProcessing Wikipedia Dictionary Generator
# Desc: Queries a random page on Wikipedia with a 0.1 seconds delay to avoid
# 	spamming the web server. Grabs the page title in order to generate a
#	good dictionary of names, places, items etc...
#
#	In Order to speed things up... a lot... I split the function into 
#	smaller processes to run in a multi process environment.


# NOTE: No Longer being developed as Wikipedia will block the IP address of anyone querying
# 	more than once per second to their web server and not obeying the robots.txt file.
#	Alternatively, download the XML wikipedia and mine that to construct a dictionary?

wikiurl = "https://en.wikipedia.org/wiki/Special:Random"
incLen = 10

def urlquery():
	for num in range(1, incLen):
		wReq = urllib2.Request(wikiurl)
		wRec = urllib2.urlopen(wReq)
		wPage = wRec.read()

		randomword = re.findall("<title>(.*) - Wikipedia, the free encyclopedia</title>", wPage)
		print randomword[0]

for num in range(1, 5):

	p1 = Process(target=urlquery)
	p1.start()
	p2 = Process(target=urlquery)
	p2.start()
	p3 = Process(target=urlquery)
	p3.start()
	p4 = Process(target=urlquery)
	p4.start()

	p1.join()
	p2.join()
	p3.join()
	p4.join()
