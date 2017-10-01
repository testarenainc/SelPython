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

####
# GenericLib.inputText("id=signin-email", "sgshwetagoyal7@gmail.com")
# GenericLib.inputText("id=signin-password", "8791640735")
# GenericLib.clickObject("xpath=//button[@class='submit btn primary-btn flex-table-btn js-submit']")
# GenericLib.clickObject("css=div[id='tweet-box-mini-home-profile']")
# GenericLib.inputText("css=div[id='tweet-box-mini-home-profile']", sTweet)
# GenericLib.clickObject("xpath=//button[@class='btn primary-btn tweet-action tweet-btn js-tweet-btn']")
# GenericLib.clickObject("id=search-query")
# GenericLib.inputText("id=search-query","khushboo220691")
# GenericLib.clickObject("xpath=//button[@class='Icon Icon--search nav-search']")
GenericLib.closeBrowser()
