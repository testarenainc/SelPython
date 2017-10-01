import sys
import os
import logging
frameworkPath = os.getcwd()
print frameworkPath

sLibraryPath = frameworkPath + "/Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
print "aaaaaa"

log = logging.getLogger('GmailTest')
##print current_time

## Browser and URL ##
GenericLib.openBrowser("http://gmail.com")
time.sleep(5)

# Example of Using Generib Defined functions with selenium commands
GenericLib.findElement("//input[@type='email']").send_keys("abc")

# Example of Using Generib Defined functions
GenericLib.inputText("//input[@type='email']","abc")

#Example of Using Seleium Web Driver in other python file
GenericLib.driver.find_element_by_xpath("//input[@type='email']").send_keys("def")
time.sleep(2)

# Example of using logs
log.info("........Logs under Gmail test ...........")
GenericLib.closeBrowser()

print "close gmail test"