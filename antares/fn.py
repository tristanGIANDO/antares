import os, shutil, socket, time, six, sys
import env
# import maya.standalone
# import maya.cmds as cmds

def newCharFN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.TYPE_CHAR_PATH))
    if assetName in check :
	    print ("Sorry, can't do this ! " + assetName + " already exists !")
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]

        path = os.path.join(env.SERVER , prod, env.TYPE_CHAR_PATH , assetName)
        source = os.path.join(env.SERVER, prod , env.SRC)
        destination = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH, env.TMP_ASSET)
        #   Copy template
        shutil.copytree(source, destination)
        os.rename(destination, path)
        #Rename Scenes
        for dpt in departments:
            editToRename = os.path.join(path , env.E_DIR , dpt , env.TMP_SCN_E + ".ma")
            publishToRename = os.path.join(path , env.P_DIR , dpt , env.TMP_SCN_P + ".ma")
            editRenamed = os.path.join(path , env.E_DIR , dpt , assetName + "_E_" + dpt + "_001.ma")
            publishRenamed = os.path.join(path , env.P_DIR , dpt , assetName + "_P_" + dpt + ".ma")
            os.rename(editToRename, editRenamed )
            os.rename(publishToRename, publishRenamed)
        #Rename E_DIR data
        for n in [".jpg", ".png", ".txt"]:
            for dpt in departments:
                editToRename = os.path.join(path , env.E_DIR , dpt , "_data" , env.TMP_SCN_E + n)
                editRenamed = os.path.join(path , env.E_DIR , dpt , "_data" , assetName + "_E_" + dpt + "_001" + n)
                publishToRename = os.path.join(path , env.P_DIR , dpt , env.TMP_SCN_P + n)
                publishRenamed = os.path.join(path , env.P_DIR , dpt , assetName + "_P_" + dpt + n)
                os.rename(editToRename, editRenamed)
                os.rename(publishToRename, publishRenamed)
        # PROFILE PICTURE
        # S:\packages\antares\dev\antares\resources\icons\_library\Images\character
        picSrc = os.path.join(env.SERVER , env.LIB, "template.png")
        picDst = os.path.join(env.SERVER , env.LIB, env.TYPE_CHAR,"template.png")
        picRenamed = os.path.join(env.SERVER, env.LIB, env.TYPE_CHAR , assetName + ".png")
        shutil.copyfile( picSrc, picDst)
        os.rename(picDst, picRenamed)
        print ("New Character created with success")

def newPropFN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.TYPE_PROP_PATH))
    if assetName in check :
	    print ("Sorry, can't do this ! " + assetName + " already exists !")
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]

        path = os.path.join(env.SERVER , prod, env.TYPE_PROP_PATH , assetName)
        source = os.path.join(env.SERVER, prod , env.SRC)
        destination = os.path.join(env.SERVER , prod , env.TYPE_PROP_PATH, env.TMP_ASSET)
        #   Copy template
        shutil.copytree(source, destination)
        os.rename(destination, path)
        #Rename Scenes
        for dpt in departments:
            editToRename = os.path.join(path , env.E_DIR , dpt , env.TMP_SCN_E + ".ma")
            publishToRename = os.path.join(path , env.P_DIR , dpt , env.TMP_SCN_P + ".ma")
            editRenamed = os.path.join(path , env.E_DIR , dpt , assetName + "_E_" + dpt + "_001.ma")
            publishRenamed = os.path.join(path , env.P_DIR , dpt , assetName + "_P_" + dpt + ".ma")
            os.rename(editToRename, editRenamed )
            os.rename(publishToRename, publishRenamed)
        #Rename E_DIR data
        for n in [".jpg", ".png", ".txt"]:
            for dpt in departments:
                editToRename = os.path.join(path , env.E_DIR , dpt , "data" , env.TMP_SCN_E + n)
                editRenamed = os.path.join(path , env.E_DIR , dpt , "data" , assetName + "_E_" + dpt + "_001" + n)
                publishToRename = os.path.join(path , env.P_DIR , dpt , env.TMP_SCN_P + n)
                publishRenamed = os.path.join(path , env.P_DIR , dpt , assetName + "_P_" + dpt + n)
                os.rename(editToRename, editRenamed)
                os.rename(publishToRename, publishRenamed)
        # PROFILE PICTURE
        picSrc = os.path.join(env.SERVER , prod, env.LIB, "template.png")
        picDst = os.path.join(env.SERVER , prod, env.LIB, env.TYPE_PROP,"template.png")
        picRenamed = os.path.join(env.SERVER, prod, env.LIB, env.TYPE_PROP , assetName + ".png")
        shutil.copyfile( picSrc, picDst)
        os.rename(picDst, picRenamed)
        print ("New Prop created with success")

def openPublish_FN(name, dep, prod):
     project = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.P_DIR , dep , name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastEdit_FN(name, dep, prod):
    path = os.path.join(env.SERVER  , prod, env.TYPE_CHAR_PATH , name , env.E_DIR , dep)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-2])
    print ( destination )
    print (project)
    print ("Edit Path")
    os.startfile(project)

def openAllEdits_FN(name, dep, prod):
    print ("Edit Path")

def deleteAsset_FN ( name, assetcharacter, prod ):
    shutil.rmtree(os.path.join(env.SERVER  , prod, env.TYPE_CHAR_PATH , name))
    os.remove(os.path.join(env.SERVER, prod, "11_library","Images", "Character", name + ".png"))
    print ("before", assetcharacter)
    assetcharacter = []
    print ("after", assetcharacter)
    characterPath = os.path.join(env.SERVER, prod, env.ASSET_DIR, env.TYPE_CHAR)
    assetcharacter = os.listdir( characterPath )
    print ("now", assetcharacter)
    #print ( name + " deleted.")
    
def renameAsset_FN(prod, oldName, newName):
    oldPath = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , oldName)
    newPath = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , newName)
    libPath = os.path.join(env.SERVER , prod, env.LIB_IMG, env.TYPE_CHAR)
      
    os.rename(oldPath, newPath)

    departmentList = os.listdir( os.path.join(newPath , env.E_DIR))
    for dpt in departmentList:
        editPath = os.path.join(newPath , env.E_DIR , dpt )
        publishPath = os.path.join(newPath , env.P_DIR , dpt)

        editToRename = os.path.join(editPath , oldName + "_E_" + dpt + "_001.ma")
        editRenamed = os.path.join(editPath , newName + "_E_" + dpt + "_001.ma")
        publishToRename = os.path.join(publishPath , oldName + "_P_" + dpt + ".ma")
        publishRenamed = os.path.join(publishPath, newName + "_P_" + dpt + ".ma")
        os.rename(editToRename, editRenamed )
        os.rename(publishToRename, publishRenamed)
    
    for n in [".jpg", ".png", ".txt"]:
        for dpt in departmentList:
            editPath = os.path.join(newPath , env.E_DIR , dpt, "_data" )
            publishPath = os.path.join(newPath , env.P_DIR , dpt)

            editToRename = os.path.join(editPath , oldName + "_E_" + dpt + "_001" + n)
            editRenamed = os.path.join(editPath , newName + "_E_" + dpt + "_001" + n)
            publishToRename = os.path.join(publishPath, oldName + "_P_" + dpt + n)
            publishRenamed = os.path.join(publishPath, newName + "_P_" + dpt + n)
            os.rename(editToRename, editRenamed)
            os.rename(publishToRename, publishRenamed)

    picDst = os.path.join(libPath, oldName + ".png")
    picRenamed = os.path.join(libPath, newName + ".png")
    os.rename(picDst, picRenamed)
    
    print ( "'", oldName , "' renamed '", newName, "' with success")

# FONCTIONS SOCKETS

def refPublishFN(name, dep, prod):
    print ( name, dep, prod )
    ref = os.path.join(env.SERVER,
                        prod,
                        env.TYPE_CHAR_PATH,
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
                        env.TYPE_CHAR_PATH,
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