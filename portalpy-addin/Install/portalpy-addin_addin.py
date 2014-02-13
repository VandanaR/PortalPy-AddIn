import arcpy
import pythonaddins
import sys
sys.path.append(r"portalpy") #This will allow this module to be read straight from the Install module
import portalpy

class listFolders2(object):
    """Implementation for portalpy-addin_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onClick(self):
        x = portalpy.Portal("ess.maps.arcgis.com", "anohe_ess5","GeogWorks3!")
        for i in x.folders("anohe_ess5"): print i['title']

class listFoldersExt(object):
    """Implementation for portalpy-addin_addin.extension10 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
    def onStartOperation(self):
        pass
