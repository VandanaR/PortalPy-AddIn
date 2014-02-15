#-------------------------------------------------------------------------------
# Name:        signIn.py
# Purpose:      Sign into ArcGIS Online through Portal Py
#
# Author:      alex7370
#
# Created:     13/02/2014
# Copyright:   (c) alex7370 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import arcpy
sys.path.append(r".\Tools")
import portalpy

def main():
    # Get the parameters for the tool
    URL = arcpy.GetParameterAsText(0)
    user = arcpy.GetParameterAsText(1)
    password = arcpy.GetParameterAsText(2)

    # Instantiate the portal object
    try:
        portalObject = portalpy.Portal(URL, user, password)
    except:
        print "Login is not valid"

    if portalObject.is_logged_in == "True":
        return "Successful login"
    else:
        return "No Sucecss"