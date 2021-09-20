import maya.cmds as cmds
import shutil
import os

'''
PUBLISH ASSET
By Tristan GIANDORIGGIO
'''

VERSION = 0.1
print ( VERSION )


def publish ( self, perso, department, *args ):
    sel = cmds.ls(sl=True)
    filePath = osDir  + "04_asset/character/" + perso + pDir + department + "/" + perso + "_P_" + department
    if sel:
        cmds.file(filePath + ".ma", force = True, options = "v = 0", type = "mayaAscii", exportSelected = True) 
        cmds.file(filePath + ".obj", pr=1,typ="OBJexport",es=1, op="groups=0; ptgroups=0; materials=0; smoothing=0; normals=0", exportSelected = True)
        shutil.copyfile( "C:/sharky/user.png", osDir  + "04_asset/character/" + perso + pDir + department + "/" + perso + "_P_" + department + ".png" )
        print "wow"
    return

publish()