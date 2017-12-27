import datetime 
import time
import os,json, sys
import string
import glob
sys.stdout=stdoutHandler

import clr, os, sys, System
clr.AddReference("Geomagic.Api.V2")
clr.AddReference('3DSPRINT')
from System.Diagnostics import Process
from System import Environment
from Watson.Automation import *
from Geomagic.Api.V2 import *

sys.path.insert(0, r'AutomationScripts\Modules')
import WatsonAutomation, AquaAutomation, geoTools, PrinterSetup
wc = WatsonAutomation.WatsonCommands()
wp = WatsonAutomation.WatsonPrinters()
scriptUtil = ScriptSys()

def XMLCheckpoint(checkpoint):
	docHelper = WatsonAutomation.DocumentHelper()
	#Use to deliver complete XML dump of Data values 
	docHelper.AddPath("//") 
	docHelper.WalkDocument()
	testrunner.doXMLCheckpoint(checkpoint, docHelper.GetXMLString(), checkpoint+".xml")
		
def main():							
	global testrunner
	resourceData = []
		
	#####################################################################DO NOT MODIFY############################################################
	#Following WorkspaceDirectory is AQUA 6 place holder
	WorkspaceDirectory="$INPUT$"
	#####################################################################\DO NOT MODIFY############################################################
	
	#####################################################################LOCAL USAGE ONLY##########################################################
	#Use Following "WorkspaceDirectory" For Local Testing (Before adding on AQuA 6 Server) & comment [WorkspaceDirectory="$INPUT$"]
	# WorkspaceDirectory="AutomationScripts/aAQuA06/Local"
	#####################################################################\LOCAL USAGE ONLY##########################################################
	
	#Creation of INIML Path for test script
	resourceFile = glob.glob(WorkspaceDirectory+"/"+"*.aqua")
	WorkspaceDirectory=WorkspaceDirectory+"/"+os.path.basename(resourceFile[0])

	#Use resourceData to retrieve iniml attributes
	resourceData = wc.readResourceFile(WorkspaceDirectory)

	#####################################################################LOCAL USAGE ONLY##########################################################
	#Use following to display iniml data LOCALLY , add more below if read more from iniml file (LOCALLY)
	# print "Input Directory " + resourceData[0]
	# print "Output Directory " + resourceData[1]
	# print "Model file " + resourceData[2]
	# print "Model file Multi " + resourceData[3]
	# resourceData[3] = resourceData[3].split(".")[0]
	# print "Model file Multi " + resourceData[3]
	#####################################################################\LOCAL USAGE ONLY##########################################################
	
	#Create mode property fields from resource data of iniml file
	input = resourceData[0]
	output = resourceData[1]
	model = resourceData[2]
	printerInput = resourceData[3]
	modelFile = input+"/"+model
	
	print printerInput
	testrunner = WatsonAutomation.WatsonTestRunner(rootScriptFile, True) # for login
	testrunner.startTest(output)
	setupList = PrinterSetup.printerSetups()
		
	#UNCOMMENT/ADD NEW FOLLOWING PRINTER NAME AS PER PRINTER REQUIREMENT OF PRINTER
	setupList.add(printerInput)
	printerSetups = setupList.getList()
	
	for setup in printerSetups:
		wc.cmdShowPrintTab()
		wc.cmdNewDocument()

		wc.cmdSelectVirtualPrinter(virtualPrinterName=setup[0], material=setup[1], printmode= setup[2], mdm=setup[3], buildstyle=setup[4]) 
		scriptUtil.Wait("2")
		printerPD()
		
		### Start Test Here
		wc.cmdShowPrintTab()
		print "Importing File"
		wc.cmdFileImport(modelFile)
		checkpoint = "Import_" + setup[0] + "_" + setup[1] + "_" + setup[2] + "_" + setup[4]
		testrunner.appendCheckpoint(checkpoint)
		XMLCheckpoint(checkpoint)
		scriptUtil.Wait("2")
		
		#Following will be used when iniml file is updated with model name and etc
		# print "Select Object"
		# SetOnlyActiveObject(modelName)
		# print "End of Select"
		
		print "Auto Place Model"
		wc.cmdAutoPlace()
		scriptUtil.Wait("2")
		checkpoint = "AutoPlace_" + setup[0] + "_" + setup[1] + "_" + setup[2] + "_" + setup[4]
		testrunner.appendCheckpoint(checkpoint)
		XMLCheckpoint(checkpoint)
		print "Auto Place Model end"
					
		print "Estimate Command start"
		wc.cmdEstimate()
		checkpoint = "Estimate_" + setup[0] + "_" + setup[1] + "_" + setup[2] + "_" + setup[4]
		testrunner.appendCheckpoint(checkpoint)
		XMLCheckpoint(checkpoint)
		print "Estimate Command end"

		print "Saving Print File"
		filename = "Output" +  "_" + setup[0] + "_" + setup[1] + "_" + setup[2] + "_" + setup[4]
		# BuildFileDir = output +""+"\OutputBuildFiles"
		BuildFileDir = os.path.join(output, "..") +""+"\Temp\OutputBuildFiles"
		if not os.path.exists(BuildFileDir):
			os.makedirs(BuildFileDir)
		wc.cmdPrint2File(BuildFileDir + "\\" + filename + ".vbf")
		checkpoint = "PrintToFile_" + setup[0] + "_" + setup[1] + "_" + setup[2] + "_" + setup[4]
		testrunner.appendCheckpoint(checkpoint)
		XMLCheckpoint(checkpoint)
		scriptUtil.Wait("2")
		print "Print To File command end"
		wc.cmdNewDocument()
		### End Test here
		testrunner.endTest()
		
		
def printerPD():
	#need a string to concatenates : material,mode,style and MDM : checkpoint = xmlfilename+printer+material+mode+style+MDM
	global testrunner
	checkpointName = ""
	#pdFile = AAD.outputData + "\\printerSettingsUsed.xml"
	printerData = wp.getSelectedPrinter()

	if printerData != None:
		printerName   = printerData.Name
		curMaterials  = printerData.GetCurrentMaterials()
		curPrintMode  = printerData.GetCurrentPrintMode()
		curBuildStyle = printerData.GetCurrentBuildStyle()
		curMDM			  = printerData.GetCurrentMDM()
	
		
		pd = geoTools.customXMLReport('printers')
	
			
		printerNode=pd.add("printer",{"name":printerName})
		if curMaterials != None: 
			pd.add("material", {"diff":curMaterials[0].Name},printerNode)
		if curPrintMode != None: 
			pd.add("mode"    , {"diff":curPrintMode.NameForUI},printerNode)
			printMode = curPrintMode.NameForUI
		else:
			printMode = "None"
		if curBuildStyle!= None: 
			pd.add("style"   , {"diff":curBuildStyle.Name},printerNode)
		if curMDM       != None: 
			pd.add("MDM"     , {"diff":curMDM.Name},printerNode)
			MDMName = curMDM.Name
		else:
			MDMName = "None"
		
		xmlString = pd.getXMLString()
		checkpointName = printerName + "_" + curMaterials[0].Name + "_" + printMode + "_" + MDMName +"_" + curBuildStyle.Name
		
		testrunner.doXMLCheckpoint(checkpointName, xmlString, checkpointName + ".xml")

main()	

