import os, shutil
import env



def newFX_FN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.FX_PATH))
    if assetName in check :
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(env.SERVER,
                            prod ,
                            env.TMP_FX_PATH)

        destination = os.path.join(env.SERVER ,
                            prod ,
                            env.FX_PATH,
                            env.TMP_FX)

        path = os.path.join(env.SERVER ,
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


        oldScn = os.path.join(env.SERVER ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            env.TMP_SCN_FX)

        newScn = os.path.join(env.SERVER ,
                            prod,
                            env.FX_PATH ,
                            assetName,
                            assetName + ".hipnc")

        print ( oldScn )
        print ( newScn )

        try:
            os.rename(oldScn, newScn)
        except:
            print ( "Try again")

        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(env.RESOURCES ,
                                        env.IMAGES_PATH,
                                        env.TMP_IMAGE)

        picDst = os.path.join(env.RESOURCES,
                                        env.IMAGES_PATH,
                                        env.FX_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(env.SERVER,
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


def open_last_FX_FN(name, prod):
    path = os.path.join(env.SERVER  ,
                            prod,
                            env.FX_PATH ,
                            name)
    destination = os.listdir( path )
    project = os.path.join(path,  destination[0])
    print ( project )
    the_list = [ name + "_*"]
    print ( the_list )

    if project.startswith(name):
        os.startfile(project)
    else:
        print ( "Try again")