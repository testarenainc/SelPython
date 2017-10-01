# SelPython
Keyword Driven Selenium Automation Framework Using Python.

# Requirement
Python: 2.7.x
Selenium (Any Version)
xlrd (To Access Xls file)
Note: This was created on MacOS

# Add new Test Case
1. Create new file with .py extension under TestCases Directory
2. Import Generib Lib by adding following line :
    rameworkPath = os.getcwd()
    sLibraryPath = frameworkPath + "/Libraries"
    sys.path.insert(0, sLibraryPath)
    import GenericLib
3. Start your steps like GenericLib.openBrowser(url), etc
4. After completion of test case add the test case in test suite. For that Go to Director TestSuite and open TestSuite.Xls
5. Now add the exact name of test case file and mark execute Yes.
