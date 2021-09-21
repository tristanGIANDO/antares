import maya.cmds as cmds
import shutil
import os

'''
INCREMENT AND SAVE
By Tristan GIANDORIGGIO and Alwin DUREZ
'''

VERSION = 0.1
print ( VERSION )

def increment (*args):

    PATH = os.path.join("S:\\",
                        "packages",
                        "antares",
                        "dev",
                        "antares",
                        "resources",
                        "icons",
                        "_user",
                        "User.png")
    boucle = 1
    nombreDeRep = 0
    while boucle == 1: 
        fullName = cmds.file( q =1, sn = 1, shn =1)
        print ( fullName )
        fullNamePath = cmds.file( q =1, sn = 1)
        absName = os.path.dirname(fullNamePath)
        noExtName = fullName.split('.')[0]
        ext = fullName.split('.')[1]
        splitName = noExtName.split('_')
        splitName.reverse()
        intVersion = int(splitName[0]) + nombreDeRep +1
        print ( intVersion )
        strVersion = str(intVersion)
        padding = strVersion.__len__()
        if padding == 1:
            newVersion = '00' + strVersion
        elif padding == 2:
            newVersion = '0' + strVersion
        else:
            newVersion = strVersion
        splitName.reverse()
        listSize = len(splitName)
        resolvedName = ''
        for i in range(0, listSize-1):
            resolvedName += splitName[i] + '_'
        finalNamePath = absName + '/'+ resolvedName +  newVersion + '.' + ext
        print ( finalNamePath )
        #check if the file exist
        if cmds.file(finalNamePath, q=1, exists = 1) == 1:
            boucle = 1
            nombreDeRep += 1
        else:
            boucle = 0 
            cmds.file(rename=finalNamePath)
            cmds.file( save=True)
            print ( "File saved to a new version" )
        #PROFILE PICTURE 
        print ( absName + "/" + resolvedName +  newVersion + ".png" )   
        shutil.copyfile( PATH, absName + "/_data/" + resolvedName +  newVersion + ".png" )





increment()