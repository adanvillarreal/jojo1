#!/usr/bin/env python
# encoding: UTF-8
import subprocess
import os
import datetime
while True:
    print "1) Detect CMS (Joomla, WordPress or other)"
    print "2) Scan Joomla list with joomscan"
    print "3) Filter joomscan results"
    cmd = ""
    a = int(input('4) Exit'))

    if(a==1):
        cmd = "python " + os.path.join(os.getcwd(), "detect/Detect.py")
    elif(a==2):
        cmd = "./" + os.path.join(os.getcwd(), "scan/Scan.sh")
    elif(a==3):
        cmd = "python " + os.path.join(os.getcwd(), "filter/Filter.py")
    elif(a==4):
        break
    else:
        continue
    print cmd
    p = subprocess.Popen(cmd, shell=True)
