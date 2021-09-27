import os, shutil, socket, json
import env


# CHARACTER

def newCharFN(server, prod, assetName):
    check = os.listdir(os.path.join(server , prod, env.CHAR_PATH))
    if assetName in check :
        # raise RuntimeError("Sorry, can't do this ! " + assetName + " already exists !")
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(server,
                            prod ,
                            env.TMP_ASSET_PATH)

        destination = os.path.join(server ,
                            prod ,
                            env.CHAR_PATH,
                            env.TMP_ASSET)

        path = os.path.join(server ,
                            prod,
                            env.CHAR_PATH ,
                            assetName)

        #   Copy template
        if os.path.isdir(destination):
            print ("_Template_asset is already there")
        else:
            shutil.copytree(source, destination)
            print ( "Template copied")
            
        try:
            os.rename(destination, path)
            print (" Template renamed, it works well")
        except:
            print ( "I couldn't rename " + assetName + " correctly ! Please do it by hand !")

        #Rename Scenes
        for dpt in departments:
            editToRename = os.path.join(path ,
                                        env.E_PATH ,
                                        dpt ,
                                        env.TMP_SCN_TYPE_E + ".ma")

            publishToRename = os.path.join(path ,
                                        env.P_PATH ,
                                        dpt ,
                                        env.TMP_SCN_TYPE_P + ".ma")

            editRenamed = os.path.join(path ,
                                        env.E_PATH ,
                                        dpt ,
                                        assetName + "_E_" + dpt + "_001.ma")

            publishRenamed = os.path.join(path ,
                                        env.P_PATH ,
                                        dpt ,
                                        assetName + "_P_" + dpt + ".ma")

            try:
                os.rename(editToRename, editRenamed )
                os.rename(publishToRename, publishRenamed)
                print ( dpt + " renamed correctly (scenes)")
            except:
                print ( dpt + " isn't renamed correctly (scenes)... ...")

        #Rename EDIT_TYPE data
        for n in [".jpg", ".png", ".txt"]:
            for dpt in departments:
                editToRename = os.path.join(path ,
                                        env.E_PATH ,
                                        dpt ,
                                        "_data" , env.TMP_SCN_TYPE_E + n)

                editRenamed = os.path.join(path ,
                                        env.E_PATH ,
                                        dpt ,
                                        "_data" ,
                                        assetName + "_E_" + dpt + "_001" + n)

                publishToRename = os.path.join(path ,
                                        env.P_PATH ,
                                        dpt ,
                                        env.TMP_SCN_TYPE_P + n)

                publishRenamed = os.path.join(path ,
                                        env.P_PATH ,
                                        dpt ,
                                        assetName + "_P_" + dpt + n)

                try :
                    os.rename(editToRename, editRenamed)
                    os.rename(publishToRename, publishRenamed)
                    print ( dpt + " renamed correctly (data)")
                except:
                    print ( dpt + " isn't renamed correctly (data)... ...")

        #Rename Sculpt
        mudbox_to_rename = os.path.join(server,
                                        prod,
                                        env.CHAR_PATH,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".mud")

        mudbox_renamed = os.path.join(server,
                                        prod,
                                        env.CHAR_PATH,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        assetName + "_E_sculpt_001.mud")

        zbrush_to_rename = os.path.join(server,
                                        prod,
                                        env.CHAR_PATH,
                                        assetName,
                                        env.ZBRUSH_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".ZPR")

        zbrush_renamed = os.path.join(server,
                                        prod,
                                        env.CHAR_PATH,
                                        assetName,
                                        env.ZBRUSH_PATH,
                                        assetName + "_E_sculpt_001.ZPR")

        try:
            os.rename(mudbox_to_rename, mudbox_renamed)
            print ( "mudbox file renamed correctly")
        except:
            print ( "mudbox file isn't renamed correctly")

        try:
            os.rename(zbrush_to_rename, zbrush_renamed)
            print ( "zbrush file renamed correctly")
        except:
            print ( "zbrush file isn't renamed correctly")

        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(server ,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.TMP_IMAGE)

        picDst = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.CHAR_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.CHAR_TYPE ,
                                        assetName + ".png")
        try:
            shutil.copyfile( picTMP_ASSET_PATH, picDst)
            os.rename(picDst, picRenamed)
            print ( "Image renamed correctly")
            print ("New Character created with success")
        except:
            print ( "There is no profile picture, sorry... ...")
            print ( "Try again, it will work better")

def openInFolder_Char_FN(name, server,prod):
    path = os.path.join( server,
                        prod,
                        env.CHAR_PATH,
                        name)
                        # env.MAYA_TYPE,
                        # env.SCN_TYPE )
    os.startfile(path)

def openPublish_FN(server, name, dep, prod):
     project = os.path.join(server ,
                            prod ,
                            env.CHAR_PATH ,
                            name ,
                            env.P_PATH ,
                            dep ,
                            name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastEdit_FN(name, dep, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.CHAR_PATH ,
                            name ,
                            env.E_PATH ,
                            dep)
    print ( path )
    destination = os.listdir( path )
    print ( destination )
    try:
        destination.remove("_data")
    except:
        print ( "No data")
    project = os.path.join(path,  destination[-1])
    print ( project )
    print ("Edit Path is a file")
    os.startfile(project)

def openAllEdits_FN(name, dep, prod):
    print ("Edit Path")

def openLastSculpt_FN(name, soft, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.CHAR_PATH ,
                            name ,
                            env.SCULPT_TYPE,
                            soft)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-1])
    print ( project )
    os.startfile(project)

def open_in_folder_sculpt_FN(name, soft, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.CHAR_PATH ,
                            name ,
                            env.SCULPT_TYPE,
                            soft)
    os.startfile(path)

def deleteAsset_FN (name, server, prod ):
    try :
        shutil.rmtree(os.path.join(server,
                                    prod,
                                    env.CHAR_PATH ,
                                    name))
    except:
        print ("You already removed the folder.")
    try:
        os.remove(os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.CHAR_TYPE,
                                    name + ".png"))
    except:
        print ("You already removed the asset picture.")
    
    print ( name + " deleted with success.")
    
def renameAsset_FN(server, prod, oldName, newName):
    oldPath = os.path.join(server , prod , env.CHAR_PATH , oldName)
    newPath = os.path.join(server , prod , env.CHAR_PATH , newName)
    IMAGES_PATHPath = os.path.join(server , prod, env.IMAGES_PATH_IMG, env.CHAR_TYPE)
      
    os.rename(oldPath, newPath)

    departmentList = os.listdir( os.path.join(newPath , env.EDIT_TYPE))
    for dpt in departmentList:
        editPath = os.path.join(newPath , env.EDIT_TYPE , dpt )
        publishPath = os.path.join(newPath , env.PUBLISH_TYPE , dpt)

        editToRename = os.path.join(editPath , oldName + "_E_" + dpt + "_001.ma")
        editRenamed = os.path.join(editPath , newName + "_E_" + dpt + "_001.ma")
        publishToRename = os.path.join(publishPath , oldName + "_P_" + dpt + ".ma")
        publishRenamed = os.path.join(publishPath, newName + "_P_" + dpt + ".ma")
        os.rename(editToRename, editRenamed )
        os.rename(publishToRename, publishRenamed)
    
    for n in [".jpg", ".png", ".txt"]:
        for dpt in departmentList:
            editPath = os.path.join(newPath , env.EDIT_TYPE , dpt, "_data" )
            publishPath = os.path.join(newPath , env.PUBLISH_TYPE , dpt)

            editToRename = os.path.join(editPath , oldName + "_E_" + dpt + "_001" + n)
            editRenamed = os.path.join(editPath , newName + "_E_" + dpt + "_001" + n)
            publishToRename = os.path.join(publishPath, oldName + "_P_" + dpt + n)
            publishRenamed = os.path.join(publishPath, newName + "_P_" + dpt + n)
            os.rename(editToRename, editRenamed)
            os.rename(publishToRename, publishRenamed)

    picDst = os.path.join(IMAGES_PATHPath, oldName + ".png")
    picRenamed = os.path.join(IMAGES_PATHPath, newName + ".png")
    os.rename(picDst, picRenamed)
    
    print ( "'", oldName , "' renamed '", newName, "' with success")


# FUNCTIONS SOCKETS

def refPublishFN( server, name, dep, prod):
    print ( name, dep, prod )
    ref = os.path.join(server,
                        prod,
                        env.CHAR_PATH,
                        name,
                        env.P_PATH,
                        dep,
                        name + "_P_" + dep + ".ma")
    
    if not os.path.isfile(ref):
        raise RuntimeError("where is %s")%ref

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', env.PORT)) #same port as in Maya
        myCommand = 'result = cmds.file( r"%s", r=True, namespace = "CHAR_1")'%ref
        s.send(bytes(myCommand, 'utf-8'))
        s.recv(2048)
        print ( "File referenced with success")

def importPublish_Char_FN(server, name, dep, prod):
    print ( name, dep, prod )
    importFile = os.path.join(server,
                        prod,
                        env.CHAR_PATH,
                        name,
                        env.P_PATH,
                        dep,
                        name + "_P_" + dep + ".ma")
    
    if not os.path.isfile(importFile):
        raise RuntimeError("where is %s")%importFile

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', env.PORT)) #same port as in Maya
        myCommand = 'cmds.file( r"%s", i=True, typ="mayaAscii")'%importFile
        s.send(bytes(myCommand, 'utf-8'))
        s.recv(2048)
        print ( "File imported with success")

def testFN():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1789)) #same port as in Maya
        myCommand = 'cmds.joint()\ncmds.polyCube()'
        s.send(bytes(myCommand, 'utf-8'))
        s.recv(2048)
        print ( "done")

    
    '''
    # Write this in Maya

    import maya.cmds as cmds
    # Open new ports
    cmds.commandPort(name=":1789", sourceType="python", echoOutput=True)
    print('Antares connected to maya')

    # je stocke des trucs
    project = osDir  + "04_asset/character/" + perso + pDir + department + "/" + perso + "_P_" + department + ".ma"
        cmds.file( project, r=True, namespace = "CHAR_1")
    '''

###### UI CUSTOMIZE


def open_library_FN(server,prod):
    path = os.path.join( server,
                        prod,
                        env.LIBRARY )
    os.startfile(path)

def open_resources_FN(server,prod):
    path = os.path.join( server,
                        prod,
                        "02_ressource")
    os.startfile(path)

def open_user_picture_FN():
    path = os.path.join( "C:\\",
                        "antares_user")
    os.startfile(path)

def open_prefs_FN():
    path = os.path.join( "C:\\",
                        "antares_user")
    os.startfile(path)