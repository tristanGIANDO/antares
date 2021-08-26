import os, shutil, socket
import env



def newCharFN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.CHAR_PATH))
    if assetName in check :
        raise RuntimeError("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]

        path = os.path.join(env.SERVER , prod, env.CHAR_PATH , assetName)
        source = os.path.join(env.SERVER, prod , env.TMP_ASSET_PATH)
        destination = os.path.join(env.SERVER , prod , env.CHAR_PATH, env.TMP_ASSET)
        #   Copy template
        if not os.path.isfile(destination):
            shutil.copytree(source, destination)
        else:
            pass
        try:
            os.rename(destination, path)
        except:
            pass
        #Rename Scenes
        for dpt in departments:
            editToRename = os.path.join(path , env.EDIT_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_E + ".ma")
            publishToRename = os.path.join(path , env.PUBLISH_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_P + ".ma")
            editRenamed = os.path.join(path , env.EDIT_TYPE , dpt , assetName + "_E_" + dpt + "_001.ma")
            publishRenamed = os.path.join(path , env.PUBLISH_TYPE , dpt , assetName + "_P_" + dpt + ".ma")
            os.rename(editToRename, editRenamed )
            os.rename(publishToRename, publishRenamed)
        #Rename EDIT_TYPE data
        for n in [".jpg", ".png", ".txt"]:
            for dpt in departments:
                editToRename = os.path.join(path , env.EDIT_TYPE , dpt , "_data" , env.TMP_SCN_TYPE_TYPE_TYPE_E + n)
                editRenamed = os.path.join(path , env.EDIT_TYPE , dpt , "_data" , assetName + "_E_" + dpt + "_001" + n)
                publishToRename = os.path.join(path , env.PUBLISH_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_P + n)
                publishRenamed = os.path.join(path , env.PUBLISH_TYPE , dpt , assetName + "_P_" + dpt + n)
                os.rename(editToRename, editRenamed)
                os.rename(publishToRename, publishRenamed)
        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(env.RESOURCES , env.IMAGES_PATH, env.TMP_IMAGE)
        picDst = os.path.join(env.RESOURCES, env.IMAGES_PATH, env.CHAR_TYPE, env.TMP_IMAGE)
        picRenamed = os.path.join(env.SERVER, env.IMAGES_PATH, env.CHAR_TYPE , assetName + ".png")
        shutil.copyfile( picTMP_ASSET_PATH, picDst)
        os.rename(picDst, picRenamed)
        print ("New Character created with success")

def newPropFN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.PROP_PATH))
    if assetName in check :
	    print ("Sorry, can't do this ! " + assetName + " already exists !")
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]

        path = os.path.join(env.SERVER , prod, env.PROP_PATH , assetName)
        source = os.path.join(env.SERVER, prod , env.TMP_ASSET_PATH)
        destination = os.path.join(env.SERVER , prod , env.PROP_PATH, env.TMP_ASSET)
        #   Copy template
        shutil.copytree(source, destination)
        os.rename(destination, path)
        #Rename Scenes
        for dpt in departments:
            editToRename = os.path.join(path , env.EDIT_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_E + ".ma")
            publishToRename = os.path.join(path , env.PUBLISH_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_P + ".ma")
            editRenamed = os.path.join(path , env.EDIT_TYPE , dpt , assetName + "_E_" + dpt + "_001.ma")
            publishRenamed = os.path.join(path , env.PUBLISH_TYPE , dpt , assetName + "_P_" + dpt + ".ma")
            os.rename(editToRename, editRenamed )
            os.rename(publishToRename, publishRenamed)
        #Rename EDIT_TYPE data
        for n in [".jpg", ".png", ".txt"]:
            for dpt in departments:
                editToRename = os.path.join(path , env.EDIT_TYPE , dpt , "data" , env.TMP_SCN_TYPE_TYPE_TYPE_E + n)
                editRenamed = os.path.join(path , env.EDIT_TYPE , dpt , "data" , assetName + "_E_" + dpt + "_001" + n)
                publishToRename = os.path.join(path , env.PUBLISH_TYPE , dpt , env.TMP_SCN_TYPE_TYPE_TYPE_P + n)
                publishRenamed = os.path.join(path , env.PUBLISH_TYPE , dpt , assetName + "_P_" + dpt + n)
                os.rename(editToRename, editRenamed)
                os.rename(publishToRename, publishRenamed)
        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(env.SERVER , prod, env.IMAGES_PATH, "template.png")
        picDst = os.path.join(env.SERVER , prod, env.IMAGES_PATH, env.PROP_TYPE,"template.png")
        picRenamed = os.path.join(env.SERVER, prod, env.IMAGES_PATH, env.PROP_TYPE , assetName + ".png")
        shutil.copyfile( picTMP_ASSET_PATH, picDst)
        os.rename(picDst, picRenamed)
        print ("New Prop created with success")

def openPublish_FN(name, dep, prod):
     project = os.path.join(env.SERVER , prod , env.CHAR_PATH , name , env.PUBLISH_TYPE , dep , name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastEdit_FN(name, dep, prod):
    path = os.path.join(env.SERVER  , prod, env.CHAR_PATH , name , env.EDIT_TYPE , dep)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-2])
    print ( destination )
    print (project)
    print ("Edit Path")
    os.startfile(project)

def openAllEdits_FN(name, dep, prod):
    print ("Edit Path")

def deleteAsset_FN ( name, assetcharacter, prod ):
    shutil.rmtree(os.path.join(env.SERVER  , prod, env.CHAR_PATH , name))
    os.remove(os.path.join(env.RESOURCES, env.IMAGES_PATH, env.CHAR_TYPE, name + ".png"))
    characterPath = os.path.join(env.SERVER, prod, env.ASSET_TYPE, env.CHAR_TYPE)
    assetcharacter = os.listdir( characterPath )
    print ("now", assetcharacter)
    print ( name + " deleted.")
    
def renameAsset_FN(prod, oldName, newName):
    oldPath = os.path.join(env.SERVER , prod , env.CHAR_PATH , oldName)
    newPath = os.path.join(env.SERVER , prod , env.CHAR_PATH , newName)
    IMAGES_PATHPath = os.path.join(env.SERVER , prod, env.IMAGES_PATH_IMG, env.CHAR_TYPE)
      
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

def refPublishFN(name, dep, prod):
    print ( name, dep, prod )
    ref = os.path.join(env.SERVER,
                        prod,
                        env.CHAR_PATH,
                        name,
                        env.P_PATH,
                        dep,
                        name + "_P_" + dep + ".ma")
    
    if not os.path.isfile(ref):
        raise RuntimeError("where is %s")%ref

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1789)) #same port as in Maya
        myCommand = 'result = cmds.file( r"%s", r=True, namespace = "CHAR_1")'%ref
        s.send(bytes(myCommand, 'utf-8'))
        s.recv(2048)
        print ( "done")

def importPublish_Char_FN(name, dep, prod):
    print ( name, dep, prod )
    ref = os.path.join(env.SERVER,
                        prod,
                        env.CHAR_PATH,
                        name,
                        env.P_PATH,
                        dep,
                        name + "_P_" + dep + ".ma")
    
    if not os.path.isfile(ref):
        raise RuntimeError("where is %s")%ref

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1789)) #same port as in Maya
        myCommand = 'cmds.file( r"%s", i=True, typ="mayaAscii")'%ref
        s.send(bytes(myCommand, 'utf-8'))
        s.recv(2048)
        print ( "done")

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