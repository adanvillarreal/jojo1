#!/usr/bin/env python
# encoding: UTF-8
import subprocess
import sys
jm = open("JOMurls.txt", "r")
x = 0
#CHANGE THIS VALUE TO THE NUMBER OF TERMINAL WINDOWS TO BE OPENED AT ONCE.
MAX_TERMINALS = 5
for url in jm.readlines():
    cmd = "joomscan -u " + url + " -ot"
    cmdd = 'gnome-terminal -e ' + '"' + cmd + '"'
    joomscan = subprocess.Popen(cmdd, shell=True, stderr=subprocess.PIPE)
    while True:
        out = joomscan.stderr.read(1)
        if out == '' and joomscan.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
        #if(x++>MAX_TERMINALS):
            #swhile out !=''
