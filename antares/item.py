import os, shutil, json
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


        #DRESSING
        source_dress = os.path.join(server,
                                    prod,
                                    env.TMP_ASSET_PATH,
                                    env.E_PATH,
                                    env.GEO_LO,
                                    env.TMP_SCN_TYPE_E + env.ASCII)

        dest_dress_edit = os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    assetName,
                                    env.E_PATH,
                                    env.DRESSING,
                                    env.TMP_SCN_TYPE_E + env.ASCII)

        dest_dress_publish = os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    assetName,
                                    env.P_PATH,
                                    env.DRESSING,
                                    env.TMP_SCN_TYPE_E + env.ASCII)

        new_dress_edit = os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    assetName,
                                    env.E_PATH,
                                    env.DRESSING,
                                    assetName + env.E_TXT + env.DRESSING + "_001" + env.ASCII)

        new_dress_publish = os.path.join(server,
                                    prod,
                                    env.SET_PATH,
                                    assetName,
                                    env.P_PATH,
                                    env.DRESSING,
                                    assetName + env.P_TXT + env.DRESSING + env.ASCII)

        shutil.copyfile(source_dress, dest_dress_edit)
        shutil.copyfile(source_dress, dest_dress_publish)
        os.rename(dest_dress_edit, new_dress_edit)
        os.rename(dest_dress_publish, new_dress_publish)

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

def create_new_item_FN(name, server, prod, assetName):

    departments = os.listdir( os.path.join(r"\\gandalf/3D4_21_22",
                                        prod,
                                        env.SET_PATH,
                                        name ,
                                        env.E_PATH))

    try:
        departments.remove(env.DRESSING)
    except:
        print ( "No dressing folder")


    #CREATE FOLDER IN SOURCEIMAGES
    os.makedirs(os.path.join(r"\\gandalf/3D4_21_22",
                                        prod,
                                        env.SET_PATH,
                                        name,
                                        env.SRC_IMG_PATH,
                                        assetName))

    #CREATE FOLDER IN DEPARTMENTS
    for dep in departments:

        os.makedirs(os.path.join(r"\\gandalf/3D4_21_22",
                                        prod,
                                        env.SET_PATH,
                                        name,
                                        env.E_PATH,
                                        dep,
                                        assetName))

        
        source = os.path.join(r"\\gandalf/3D4_21_22",
                                prod ,
                                env.TMP_ASSET_PATH,
                                env.E_PATH,
                                dep,
                                env.TMP_SCN_TYPE_E + env.ASCII)

        dest_edit = os.path.join(r"\\gandalf/3D4_21_22",
                                prod,
                                env.SET_PATH,
                                name,
                                env.E_PATH,
                                dep,
                                assetName,
                                env.TMP_SCN_TYPE_E + env.ASCII)
        
        dest_publish = os.path.join(r"\\gandalf/3D4_21_22",
                                prod,
                                env.SET_PATH,
                                name,
                                env.P_PATH,
                                dep,
                                env.TMP_SCN_TYPE_E + env.ASCII)

        new_name_edit = os.path.join(r"\\gandalf/3D4_21_22",
                                prod,
                                env.SET_PATH,
                                name,
                                env.E_PATH,
                                dep,
                                assetName,
                                assetName + env.E_TXT + dep + "_001" + env.ASCII)

        new_name_publish = os.path.join(r"\\gandalf/3D4_21_22",
                                prod,
                                env.SET_PATH,
                                name,
                                env.P_PATH,
                                dep,
                                assetName + env.P_TXT + dep + env.ASCII)

        #   Copy template
        shutil.copyfile(source, dest_edit)
        shutil.copyfile(source, dest_publish)
        print ( "Template copied")
            
        try:
            os.rename(dest_edit, new_name_edit)
            os.rename(dest_publish, new_name_publish)
            print (" Template renamed, it works well")
        except:
            print ( "I couldn't rename " + assetName + " correctly ! Please do it by hand !")


    print ( "done" )
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

def open_last_dress_FN(name, server, prod):
    path = os.path.join(server  ,
                            prod ,
                            env.SET_PATH ,
                            name,
                            env.E_PATH ,
                            env.DRESSING)
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

def open_publish_dress_FN(name, server, prod):
    path = os.path.join(server  ,
                            prod ,
                            env.SET_PATH ,
                            name,
                            env.P_PATH ,
                            env.DRESSING)
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

def open_in_folder_edits_FN(item_name, name, dep, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            name,
                            env.E_PATH,
                            dep,
                            item_name)
    os.startfile(path)

def delete_item_FN (item_name, name, dep, server, prod ):
    
    departments = os.listdir( os.path.join(r"\\gandalf/3D4_21_22",
                                        prod,
                                        env.SET_PATH,
                                        name ,
                                        env.E_PATH))

    try:
        departments.remove(env.DRESSING)
    except:
        print ( "No dressing folder")
    

    for dpt in departments:
        path = os.path.join(server,
                                    prod,
                                    env.SET_PATH ,
                                    name,
                                    env.E_PATH,
                                    dpt,
                                    item_name)

     
        try :
            shutil.rmtree(path)
        except:
            print ("You already removed " + dpt )




    departments_publish = os.listdir( os.path.join(r"\\gandalf/3D4_21_22",
                                        prod,
                                        env.SET_PATH,
                                        name ,
                                        env.P_PATH))

    try:
        departments_publish.remove(env.DRESSING)
    except:
        print ( "No dressing folder")

    for dpt in departments_publish:
        path = os.path.join(server,
                                    prod,
                                    env.SET_PATH ,
                                    name,
                                    env.P_PATH,
                                    dpt,
                                    item_name + env.P_TXT + dpt + env.ASCII)

        try :
            os.remove(path)
        except:
            print ("You already removed " + dpt )

        print ( path )

    print ( name + " deleted with success.")

def delete_module_FN (name, server, prod ):
    
    path = os.path.join(server,
                                prod,
                                env.SET_PATH ,
                                name)
    try :
        shutil.rmtree(path)
    except:
        print ("You already removed " + path )

    print ( path )

    try:
        os.remove(os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.SET_TYPE,
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

def open_in_folder_module_FN(name, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            name,
                            env.MAYA_TYPE,
                            env.SCN_TYPE)
    os.startfile(path)

def open_in_folder_dress_FN(name, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            name,
                            env.E_PATH,
                            env.DRESSING)
    os.startfile(path)

def substance_FN(item_name, name, server, prod):
    src = os.path.join(r"\\gandalf/3D4_21_22",
                            prod,
                            env.LIBRARY,
                            env.RMAN_LIB,
                            "library.json")

    srcImg_path = os.path.join(server  ,
                            prod,
                            env.SET_PATH ,
                            name ,
                            env.SRC_IMG_PATH,
                            item_name)

    dst = os.path.join(r"\\gandalf/3D4_21_22" ,
                            prod,
                            env.SET_PATH ,
                            name ,
                            env.SRC_IMG_PATH,
                            item_name,
                            env.RMAN_LIB,
                            "library.json")

    dictionary = {
    "RenderManAssetLibrary": {
        "author" : env.USER,
        "description": "",
        "name": name,
        "protected": "",
        "rendererVersion": "24.1",
        "version": "1.0",
        "versionControl": "none"
        }
    }

    try:
        os.makedirs(os.path.join(srcImg_path,
                        env.RMAN_LIB,
                        env.RMAN_MAT))

        shutil.copyfile(src, dst)

        with open(dst, "w") as outfile:
            json.dump(dictionary, outfile)

        print ( "Substance Library created" )
        
    except:
        print ( "Substance Library already created" )