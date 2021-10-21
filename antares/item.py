import os, shutil
import env

#GLOBAL

def create_new_module_FN(server, prod, assetName):
    check = os.listdir(os.path.join(server , prod, env.SET_PATH))
    if assetName in check :
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(server,
                            prod ,
                            env.TMP_ASSET_PATH)

        destination = os.path.join(server ,
                            prod ,
                            env.SET_PATH,
                            env.TMP_ASSET)

        path = os.path.join(server ,
                            prod,
                            env.SET_PATH ,
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


            try:
                os.remove(editToRename )
                os.remove(publishToRename)
                print ( dpt + " removed correctly (scenes)")
            except:
                print ( dpt + " isn't removed correctly (scenes)... ...")

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


                try :
                    os.remove(editToRename)
                    os.remove(publishToRename)
                    print ( dpt + " removed correctly (data)")
                except:
                    print ( dpt + " isn't removed correctly (data)... ...")

        #Rename Sculpt
        mudbox_to_rename = os.path.join(server,
                                        prod,
                                        env.SET_PATH,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".mud")


        zbrush_to_rename = os.path.join(server,
                                        prod,
                                        env.SET_PATH,
                                        assetName,
                                        env.ZBRUSH_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".ZPR")


        try:
            os.remove(mudbox_to_rename)
            print ( "mudbox file removed correctly")
        except:
            print ( "mudbox file isn't removed correctly")

        try:
            os.remove(zbrush_to_rename)
            print ( "zbrush file removed correctly")
        except:
            print ( "zbrush file isn't removed correctly")

        directory = os.makedirs(os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    assetName,
                                    env.E_PATH,
                                    env.GEO_LO,
                                    "temp to delete"))

        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(server ,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.TMP_IMAGE)

        picDst = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.SET_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.SET_TYPE ,
                                        assetName + ".png")
        try:
            shutil.copyfile( picTMP_ASSET_PATH, picDst)
            os.rename(picDst, picRenamed)
            print ( "Image renamed correctly")
            print ("New module created with success")
        except:
            print ( "There is no profile picture, sorry... ...")
            print ( "Try again, it will work better")

def create_new_item_FN(server, dep, module, assetName, prod):
    directory = os.makedirs(os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    module,
                                    env.E_PATH,
                                    assetName))
    
    check = os.listdir(os.path.join(server ,
                                    prod,
                                    env.SET_PATH,
                                    module,
                                    env.E_PATH,
                                    assetName))
    if assetName in check :
        # raise RuntimeError("Sorry, can't do this ! " + items + " already exists !")
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(server,
                            prod ,
                            env.TMP_ASSET_PATH,
                            env.E_PATH,
                            dep,
                            env.TMP_SCN_TYPE_E)

        destination = os.path.join(server ,
                            prod ,
                            env.SET_PATH ,
                            module,
                            env.E_PATH,
                            dep,
                            directory,
                            env.TMP_SCN_TYPE_E)

        path = os.path.join(server ,
                            prod,
                            env.SET_PATH,
                            module,
                            env.E_PATH,
                            dep,
                            directory,
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
                                        env.SET_PATH ,
                                        set,
                                        module,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".mud")

        mudbox_renamed = os.path.join(server,
                                        prod,
                                        env.SET_PATH ,
                                        set,
                                        module,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        assetName + "_E_sculpt_001.mud")

        zbrush_to_rename = os.path.join(server,
                                        prod,
                                        env.SET_PATH ,
                                        set,
                                        module,
                                        assetName,
                                        env.ZBRUSH_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".ZPR")

        zbrush_renamed = os.path.join(server,
                                        prod,
                                        env.SET_PATH ,
                                        set,
                                        module,
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
                                        env.ITEM_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.ITEM_TYPE ,
                                        assetName + ".png")
        try:
            shutil.copyfile( picTMP_ASSET_PATH, picDst)
            os.rename(picDst, picRenamed)
            print ( "Image renamed correctly")
            print ("New Character created with success")
        except:
            print ( "There is no profile picture, sorry... ...")
            print ( "Try again, it will work better")

#ITEMS

def openPublish_FN(item_name, name, dep, server, prod):
     project = os.path.join(server ,
                            prod ,
                            env.SET_PATH ,
                            name,
                            env.P_PATH ,
                            dep ,
                            item_name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastEdit_FN(item_name, name, dep, server, prod):
    path = os.path.join(server  ,
                            prod ,
                            env.SET_PATH ,
                            name,
                            env.E_PATH ,
                            dep,
                            item_name)
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

def open_in_folder_edits_FN(name, dep, server, setName, modName, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            setName,
                            modName,
                            name,
                            env.E_PATH ,
                            dep)
    os.startfile(path)

def deleteAsset_FN (name, server, setName, modName, prod ):
    try :
        shutil.rmtree(os.path.join(server,
                                    prod,
                                    env.SET_PATH ,
                                    setName,
                                    modName,
                                    name,))
    except:
        print ("You already removed the folder.")
    try:
        os.remove(os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.ITEM_TYPE,
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

def open_in_folder_sculpt_FN(name, soft, server, setName, modName, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            setName,
                            modName,
                            name,
                            env.SCULPT_TYPE,
                            soft)
    os.startfile(path)