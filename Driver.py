from openpyxl import load_workbook
import xlrd
import ConfigParser
from ConfigParser import SafeConfigParser
import sys
import os
import time
from datetime import datetime
from selenium import webdriver
global frameworkPath
frameworkPath = os.getcwd()
print (frameworkPath)
sLibraryPath = frameworkPath + "/Libraries"
sys.path.insert(0, sLibraryPath)
import GenericLib
# from GenericLib import driver 

sCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
global intCounter
intCounter = 0
global sReportPath
sReportPath = frameworkPath + "/Reports/Automation_Report_" + str(sCurrentTime) + ".html"

global sIniPath
sIniPath = frameworkPath + "/config.ini"
print "Global ini path:- " + sIniPath

def readTestSuiteXlsxFile():
    # Pre Setting:
    global intCounter
    GenericLib.sIniFilePath = frameworkPath + "/Config.ini"
 
    GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath, "Other", "FrameworkPath", frameworkPath)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #logFile = frameworkPath + "/Logs/GL_" + current_time + ".log"
    GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "SuiteStartTime", current_time)
    #GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "Log File", logFile)
    GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase Status", "")
    GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase_FileName", "")
    GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "Test Case Name", "")
    testSuiteFileName = GenericLib.getValueFromINIFile_Dr(GenericLib.sIniFilePath , "Environment", "testSuiteFile")
    
    testSuitePath = str(frameworkPath) + "/TestSuite/" + str(testSuiteFileName)
    print (testSuitePath)
    oWorkbook = xlrd.open_workbook(testSuitePath)
    
    testSuiteSheetFileName = GenericLib.getValueFromINIFile_Dr(GenericLib.sIniFilePath , "Environment", "testSuiteSheetName")
    oWorksheet = oWorkbook.sheet_by_name(testSuiteSheetFileName)
    rowCount = oWorksheet.nrows
    testSuiteReportCreation()
    try:
        for iRow in range(1, rowCount):
            sTestCaseCell = oWorksheet.cell_value(iRow, 0)
            sTestCaseExecutionCell = oWorksheet.cell_value(iRow, 1)

            sTestCaseName = sTestCaseCell
            sTestCaseExecutionVal = sTestCaseExecutionCell
            print (sTestCaseName, sTestCaseExecutionVal)

            if sTestCaseExecutionVal == "Yes":
                print (sTestCaseName)
                intCounter = intCounter + 1
                sFilePath = frameworkPath + "/TestCases/" + sTestCaseName +".py"
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "Test Case Name", sTestCaseName)
                sTCCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
                sTCFileName = sTestCaseName + "_" + str(sTCCurrentTime) + ".html"
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase_FileName", sTCFileName)
                sTCReportPath = frameworkPath + "/Reports/TestCaseReport/" + sTCFileName
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase_Path", sTCReportPath)
                execfile(sFilePath)
                testSuiteReportAddTestCaseReport(intCounter)
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase Status", "")
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "TestCase_FileName", "")
                GenericLib.setValueIntoINIFile(GenericLib.sIniFilePath , "Other", "Test Case Name", "")
        testSuiteReportClosure()
    except Exception as e:
        print "under exception" + str(e)
        testSuiteReportClosure()
        GenericLib.quitSelenium()

    GenericLib.quitSelenium()


#########################################################################################
def testSuiteReportCreation():
    global sReportPath
    sImagePath = frameworkPath + "/TestArena.jpg"
    sHeaderName = "Environment"
    sEnvName = GenericLib.getValueFromINIFile_Dr(sIniPath , sHeaderName, "Environment")
    sReleaseName = GenericLib.getValueFromINIFile_Dr(sIniPath , sHeaderName, "Release")
    sUserReq = GenericLib.getValueFromINIFile_Dr(sIniPath , sHeaderName, "User Requested")
    sRunStartTime = GenericLib.getValueFromINIFile_Dr(sIniPath , "Other", "SuiteStartTime")

    print (sReportPath)
    if not(os.path.isfile(sReportPath)):
        sFile = open(sReportPath, "w")
        sFile.write('<html><HEAD><TITLE>Automation Report</TITLE></HEAD><body><h4 align="center"><FONT COLOR="660066" FACE="Arial"SIZE=5><b>Automation Test Report</b><img src="' + sImagePath + '" alt="TestArena" align="right"></h4>')
        sFile.write('<table cellspacing=1 cellpadding=1   border=1> <tr>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Test Details :</h4>')
        sFile.write('<td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Run Start Date Time</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sRunStartTime +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>User Requested</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sUserReq +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Environment</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sEnvName +'</b></td></tr>')
        sFile.write('<tr><td  border=1 width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Release</b></td>')
        sFile.write('<td  border=1 width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sReleaseName +'</b></td></tr></table>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Detailed Report :</h4><table  border=1 cellspacing=1    cellpadding=1 ><tr> ')
        sFile.write('<td width=80  align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>S.No</b></td>')
        sFile.write('<td width=75 align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Test Case</b></td>')
        sFile.write('<td width=600 align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Status</b></td>')
    else:
       sFile = open(sReportPath, "a")

#########################################################################################
def testSuiteReportAddTestCaseReport(intCounter):
    global sReportPath
    print "testSuiteReportAddTestCaseReport Report Path:- " + sReportPath
    StatusDetbgcolor=""
    sFile = open(sReportPath, "a")
    print "Start Printing"
    # sIniPath = frameworkPath + "/config.ini"
    sTestCaseName = GenericLib.getValueFromINIFile_Dr(sIniPath , "Other", "Test Case Name")
    print "Test Case Name:- " + sTestCaseName
    sTC_Status = GenericLib.getValueFromINIFile_Dr(sIniPath , "Other", "TestCase Status")
    print "Test Case status:- " + sTC_Status
    sTC_FileName = GenericLib.getValueFromINIFile_Dr(sIniPath , "Other", "TestCase_FileName")
    print "Test file Name:- " + sTC_FileName
    if sTC_Status.lower() == "pass":
        StatusDetbgcolor='"#BCE954"'
    elif sTC_Status.lower() == "fail":
        finalTestCaseStatus="Fail"
        StatusDetbgcolor = '"#F9966B"'
    elif sTC_Status.lower() == "done":
        StatusDetbgcolor = '"#BCE954"'
    else:
        finalTestCaseStatus="Pass"
        StatusDetbgcolor = '"#BCE954"'
    #Append test report after creating
    sFile.write('<tr><td width=80 align="center"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(intCounter) + '</b></td>')
    sFile.write('<td width=600 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b><a href=TestCaseReport/' + str(sTC_FileName) + '>' + str(sTestCaseName) + '</b></td>')
    sFile.write('<td width=75 align="center" bgcolor=' + StatusDetbgcolor + '><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(finalTestCaseStatus) + '</b></td>')
        
#########################################################################################
def testSuiteReportClosure():
   global sReportPath  
   sFile = open(sReportPath, "a")
   sFile.write('</table></html>')

readTestSuiteXlsxFile()

