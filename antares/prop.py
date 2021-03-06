import os, shutil, json
import env

def newProp_FN(server, prod, assetName):
    check = os.listdir(os.path.join(server ,
                                    prod,
                                    env.PROP_PATH))
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
                            env.PROP_PATH,
                            env.TMP_ASSET)

        path = os.path.join(server ,
                            prod,
                            env.PROP_PATH ,
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
                                        env.PROP_PATH,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".mud")

        mudbox_renamed = os.path.join(server,
                                        prod,
                                        env.PROP_PATH,
                                        assetName,
                                        env.MUDBOX_PATH,
                                        assetName + "_E_sculpt_001.mud")

        zbrush_to_rename = os.path.join(server,
                                        prod,
                                        env.PROP_PATH,
                                        assetName,
                                        env.ZBRUSH_PATH,
                                        env.TMP_SCN_TYPE_SCULPT + ".ZPR")

        zbrush_renamed = os.path.join(server,
                                        prod,
                                        env.PROP_PATH,
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
                                        env.PROP_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.PROP_TYPE ,
                                        assetName + ".png")
        try:
            shutil.copyfile( picTMP_ASSET_PATH, picDst)
            os.rename(picDst, picRenamed)
            print ( "Image renamed correctly")
            print ("New Prop created with success")
        except:
            print ( "There is no profile picture, sorry... ...")
            print ( "Try again, it will work better")

def openLastEdit_FN(name, dep, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.PROP_PATH ,
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

def openPublish_FN(server, name, dep, prod):
     project = os.path.join(server ,
                            prod ,
                            env.PROP_PATH ,
                            name ,
                            env.P_PATH ,
                            dep ,
                            name + "_P_" + dep + ".ma")
     print ( project )
     print ("Publish Path")
     os.startfile(project)

def openLastSculpt_FN(name, soft, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.SCULPT_TYPE,
                            soft)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-1])
    print ( project )
    os.startfile(project)

def openInFolder_FN(name, server,prod):
    path = os.path.join( server,
                        prod,
                        env.PROP_PATH,
                        name,
                        env.MAYA_TYPE,
                        env.SCN_TYPE )
    os.startfile(path)

def open_in_folder_sculpt_FN(name, soft, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.SCULPT_TYPE,
                            soft)
    os.startfile(path)

def open_in_folder_edits_FN(name, dep, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.E_PATH ,
                            dep)
    os.startfile(path)

def deleteAsset_FN (name, server, prod ):
    try :
        shutil.rmtree(os.path.join(server,
                                    prod,
                                    env.PROP_PATH ,
                                    name))
    except:
        print ("You already removed the folder.")
    try:
        os.remove(os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.PROP_TYPE,
                                    name + ".png"))
    except:
        print ("You already removed the asset picture.")
    
    print ( name + " deleted with success.")
    
def substance_FN(name, server, prod):
    src = os.path.join(r"\\gandalf/3D4_21_22",
                            prod,
                            env.LIBRARY,
                            env.RMAN_LIB,
                            "library.json")

    srcImg_path = os.path.join(server  ,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.SRC_IMG_PATH)

    dst = os.path.join(r"\\gandalf/3D4_21_22" ,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.SRC_IMG_PATH,
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