import sys
import os
frameworkPath = os.getcwd()
print frameworkPath

sLibraryPath = frameworkPath + "\\Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
##print current_time

## Browser and URL ##
sConfigFilePath = frameworkPath + "\\Config.ini"
print "SConfig File Path "
print sConfigFilePath
GenericLib.openBrowser("https://twitter.com/?lang=en")
time.sleep(5)
GenericLib.closeBrowser()
