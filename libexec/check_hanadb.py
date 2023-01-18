#!/usr/bin/python

import os,sys

processValidation=sys.argv[1]+","

processName=os.popen("/usr/sap/hostctrl/exe/sapcontrol -nr 10 -function GetProcessList | grep "+sys.argv[1]+" | awk '{print $1}'").readline().strip()

processInfo=os.popen("/usr/sap/hostctrl/exe/sapcontrol -nr 10 -function GetProcessList | grep "+sys.argv[1]+" | awk '{print $4}'").readline().strip()

processId=os.popen("/usr/sap/hostctrl/exe/sapcontrol -nr 10 -function GetProcessList | grep "+sys.argv[1]+" | awk '{print $11}'").readline().strip()


if (processInfo == "GREEN," and processName == processValidation):
        print "OK - Process %s it's running in process ID : %s - process status : %s." % (processName, processId, processInfo)
        sys.exit(0)

if (processInfo == "YELLOW," and processName == processValidation):
        print "WARNING - Process %s is %s it's going up" % (processName, processInfo)
        sys.exit(1)

elif (processInfo == "GRAY" and processName == processValidation):
        print "CRITICAL - Process %s is %s it's not going to go up" % (processName, processInfo)
        sys.exit(2)
else:
        print "UNKNOWN - %s is %s .We can not identify process status" % (processName, processInfo)
        sys.exit(3)
