import os, shutil
import env

#GLOBAL

def create_new_set_FN(name, server,prod):
    directory = os.path.join(server,
                                    prod,
                                    env.SET_PATH ,
                                    name)
    
    os.makedirs(directory)

def create_new_module_FN(server, set, module, prod):
    directory = os.path.join(server,
                                    prod,
                                    env.SET_PATH ,
                                    set,
                                    module)
    
    os.makedirs(directory)

def create_new_item_FN(self):
    print ( "to do")

#ITEMS

def openPublish_FN(name, dep, server, setName, modName, prod):
     project = os.path.join(server ,
                            prod ,
                            env.SET_PATH ,
                            setName,
                            modName,
                            name,
                            env.P_PATH ,
                            dep ,
                            name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastEdit_FN(name, dep, server, setName, modName, prod):
    path = os.path.join(server  ,
                            prod ,
                            env.SET_PATH ,
                            setName,
                            modName,
                            name,
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

def openLastSculpt_FN(name, soft, server, setName, modName, prod):
    path = os.path.join(server  ,
                            prod ,
                            env.SET_PATH ,
                            setName,
                            modName,
                            name,
                            env.SCULPT_TYPE,
                            soft)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-1])
    print ( project )
    os.startfile(project)

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
