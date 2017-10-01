import sys
import os
frameworkPath = os.getcwd()
print frameworkPath

sLibraryPath = frameworkPath + "/Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
##print current_time

## Browser and URL ##
sConfigFilePath = frameworkPath + "/Config.ini"
print "SConfig File Path "
print sConfigFilePath
sURL = "file://" + frameworkPath + "/TestCases/alertexample.html"
GenericLib.openBrowser(sURL)
time.sleep(5)
##print "slept for 10 sec"

## Not a member ##
print "after sleep of alert"
GenericLib.clickObject("css=button")
print("after click object")
time.sleep(5)
print "AFter Click on Try it"
GenericLib.clickAlert()
GenericLib.closeBrowser()
