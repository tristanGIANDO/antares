import os, shutil

try:
    import maya.standalone
    maya.standalone.initialize("Python")
    
except:
    import traceback
    traceback.print_exc() 
    
# import maya.cmds as cmds
from maya import cmds
import sys



###### REFERENCE PUBLISH ########################################################
if __name__=='__main__':
    args=eval(sys.argv[1])
    kwargs=eval(sys.argv[2]) 
    project = kwargs["project_path"]
    print ( project )
    cmds.file( new = True, force = True)
    #cmds.joint(n = "IN_def")