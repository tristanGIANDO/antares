import os, shutil
import env



def newFX_FN(server, prod, assetName):
    check = os.listdir(os.path.join(server , prod, env.FX_PATH))
    if assetName in check :
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(server,
                            prod ,
                            env.TMP_FX_PATH)

        destination = os.path.join(server ,
                            prod ,
                            env.FX_PATH,
                            env.TMP_FX)

        path = os.path.join(server ,
                            prod,
                            env.FX_PATH ,
                            assetName)

        #   Copy template
        if os.path.isdir(destination):
            print ("_Template_asset is already there")
        else:
            shutil.copytree(source, destination)
            print ( "Template copied")

        # Rename template 
        try:
            os.rename(destination, path)
            print (" Template renamed, it works well")
        except:
            print ( "I couldn't rename " + assetName + " correctly ! Please do it by hand !")


        oldScn = os.path.join(server ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            "scenes",
                            env.TMP_SCN_FX)

        newScn = os.path.join(server ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            "scenes",
                            assetName + "_001.hipnc")

        print ( oldScn )
        print ( newScn )

        try:
            os.rename(oldScn, newScn)
        except:
            print ( "Try again to rename the scene")

        #DATA
        old_data = os.path.join(server ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            "_data",
                            "template_001.png")

        new_data = os.path.join(server ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            "_data",
                            assetName + "_001.png")

        try:
            os.rename(old_data, new_data)
        except:
            print ( "Try again to rename data")

        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.TMP_IMAGE)

        picDst = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.FX_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(server,
                                        prod,
                                        env.IMAGES_PATH,
                                        env.FX_TYPE ,
                                        assetName + ".png")

        try:
            shutil.copyfile( picTMP_ASSET_PATH, picDst)
            os.rename(picDst, picRenamed)
            print ( "Image renamed correctly")
            print ("New Hip created with success")
        except:
            print ( "Try again")

        path = os.path.join(server  ,
                                prod,
                                env.FX_PATH ,
                                assetName,
                                "scenes")
        destination = os.listdir( path )
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)

def open_last_FX_FN(name, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.FX_PATH ,
                            name,
                            "scenes")
    destination = os.listdir( path )
    project = os.path.join(path,  destination[-1])
    print ( project )
    os.startfile(project)

def delete_FX_FN (name, server, prod ):
    try :
        shutil.rmtree(os.path.join(server,
                                    prod,
                                    env.FX_PATH ,
                                    name))
    except:
        print ("You already removed the folder.")
    try:
        os.remove(os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.FX_TYPE,
                                    name + ".png"))
    except:
        print ("You already removed the asset picture.")
    
    print ( name + " deleted with success.")

def open_in_folder_dep_FX_FN(name, dep, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.FX_PATH ,
                            name,
                            dep)
    print (path)
    os.startfile(path)

def open_all_FX_FN(name, edit, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.FX_PATH ,
                            name,
                            "scenes",
                            edit)

    print (path)
    os.startfile(path)