#!/usr/bin/env python
# encoding: UTF-8
#Checks txt files in a folder from joomscan.
import os
import datetime
import sys
import colors
urlsDir = os.path.join(os.getcwd(), "urls")
resultsDir = os.path.join(os.getcwd(), "reports")
print "The directory with the urls is " + urlsDir
for i in os.listdir(urlsDir):
    print i
    url = i[::-14]
    if  i.endswith(".txt"):
        scanfile = open(os.path.join(urlsDir, i), "r")
        f = open(os.path.join(resultsDir, "report"+datetime.datetime.now().strftime("%m%d-%H%M")+".txt", "a"))
        scandate = datetime.date.today
        scantime = datetime.datetime.now().time
        sqli = 0
        xss = 0
        csrf = 0
        afu	= 0
        dos	= 0
        lfi	= 0
        rfi	= 0
        indis= 0
        htaccess = 0
        info = ""
        check = ""
        found = ""

        f.write("#******************************************************************************************#\n")
        for line in scanfile.readlines():
            flag = 0
            line = line.rstrip()
            if "Target :" in line:
                f.write(line+"\n")
                url = line[9:]
            if "[x]" in line:
                error = line[4:]
                sys.stdout.write(colors.color.RED+" [x] Error: "+error+"\n"+colors.color.RESET)
            else:
                if "Info" in line:
                    info = line[8:]
                if "Check" in line:
                    check = line[8:]
                if "Exploit" in line:
                    found = line[9:]
                if "Vulnerable? Yes" in line:
                    flag = 1
                    sys.stdout.write(colors.color.GREEN+" VULNERABLE\n"+colors.color.RESET)
		  # Add more criteria if needed !! :)
		  # Don't forget to update "jm_vuln_table" Table's columns!!
                if "SQL Injection" in info:
                    sqli = 1
                elif "XSS" or "Cross Site Scripting" in info:
                    xss = 1
                elif  "CSRF" or "Cross Site Request Forgery" in info:
                    csrf = 1
                elif  "File Upload" in info:
                    afu = 1
                elif  "DoS" or "Dos" or "DOS" in info:
                    dos = 1
                elif "Remote File" or "Remote File Inclusion" in line:
                    rfi = 1
                elif "Local File" or "Local File Inclusion" in line:
                    lfi = 1
                elif  "Disclosure" in info:
                    indis = 1
                elif  "htaccess.txt" in info:
                    htaccess = 1
                else:
                    pass

            if flag == 1:
                sys.stdout.write(colors.color.RED+" [!] Vulnerability - "+info+"\n"+colors.color.RESET)
                sys.stdout.flush()
                f.write ("\t"+ "Vulnerability  - " +info+"\n")
                sys.stdout.write(colors.color.RED+" [!] Vulnerability URL: "+url+"/"+check+"\n"+colors.color.RESET)
                sys.stdout.flush()
                f.write ("\t"+"Vulnerability URL 	: "+url+"/"+check+"\n")
                sys.stdout.write(colors.color.YELLOW+" [+] Vulnerability Details: "+found+"\n"+colors.color.RESET+"\n")
                sys.stdout.flush()
                f.write ("\t"+"Vulnerability Details 	: "+found+"\n")
                f.write ("\n#-------------------------------------------------------------------------------------------#\n\n")
        f.close()
print "The results are in " + resultsDir
