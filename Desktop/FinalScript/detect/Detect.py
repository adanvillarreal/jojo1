#!/usr/bin/env python
# encoding: UTF-8
from urllib2 import Request, urlopen, URLError, HTTPError
from colorama import init, Fore
import os
import sys
import urllib2
import re
import datetime
init()
urlsDir = os.path.join(os.getcwd(), "detect/urls")
resultsDir = os.path.join(os.getcwd(), "detect/results")
print urlsDir
print resultsDir
jomtag = '<meta name="generator" content="Joomla! - Open Source Content Management" />'
wp = open(os.path.join(resultsDir, "WPurls"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt"),"w")
jm = open(os.path.join(resultsDir,"JOMurls"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt"),"w")
other = open(os.path.join(resultsDir,"Other"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt"), "w")
error4xx = open(os.path.join(resultsDir,"Error4xx"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt"), "w")
error5xx = open(os.path.join(resultsDir,"Error5xx"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt"), "w")
print "The directory with the urls is " + urlsDir
print "If a scan gets stuck, it can be interrupted with ^C"
for i in os.listdir(urlsDir):
    print "I " + i
    if i.endswith(".txt"):
        scanfile = open(os.path.join(urlsDir, i), "r")
        for url in scanfile.readlines():
            try:
                req = Request(url)
                try:
                    response = urlopen(req)
                except HTTPError as e:
                    print Fore.RED + url + 'Failed to fulfill the request.'
                    print Fore.RED + 'Error code: ' + str(e.code) + "\n"
                    error4xx.write(url)
                    continue
                except URLError as e:
                    print Fore.RED + url + 'Failed to reach a server.'
                    print Fore.RED + 'Reason: ' + str(e.reason) + "\n"
                    error5xx.write(url)
                    continue
                else:
                    html = response.read()
                    if re.search('joomla', html, re.IGNORECASE):
                        if re.search(jomtag, html):
                            print Fore.GREEN + url + ' 100%% Joomla\n'
                        else:
                            print Fore.GREEN + url + 'Surely Joomla\n'
                        jm.write(url)
                    elif re.search('wordpress', html, re.IGNORECASE):
                        print Fore.GREEN + url + ' WordPress\n'
                        wp.write(url)
                    else:
                        print Fore.YELLOW + url + ' other\n'
                        other.write(url)
            except KeyboardInterrupt:
                print "Interrupted"
            scanfile.close()
print "The results are in " + resultsDir
