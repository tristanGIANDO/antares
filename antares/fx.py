import os, shutil
import env



def newFX_FN(prod, assetName):
    check = os.listdir(os.path.join(env.SERVER , prod, env.CHAR_PATH))
    if assetName in check :
        # raise RuntimeError("Sorry, can't do this ! " + assetName + " already exists !")
        print ("Sorry, can't do this ! " + assetName + " already exists !")
	    
    else:
        departments = ["geoLo", "cloth", "dressing", "groom", "lookdev", "geoHi", "rig" ]
        source = os.path.join(env.SERVER,
                            prod ,
                            env.TMP_ASSET_PATH)

        destination = os.path.join(env.SERVER ,
                            prod ,
                            env.CHAR_PATH,
                            env.TMP_ASSET)

        path = os.path.join(env.SERVER ,
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

        # PROFILE PICTURE
        picTMP_ASSET_PATH = os.path.join(env.RESOURCES ,
                                        env.IMAGES_PATH,
                                        env.TMP_IMAGE)

        picDst = os.path.join(env.RESOURCES,
                                        env.IMAGES_PATH,
                                        env.CHAR_TYPE,
                                        env.TMP_IMAGE)

        picRenamed = os.path.join(env.SERVER,
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

def openInFolder_Char_FN(name, prod):
    path = os.path.join( env.SERVER,
                        prod,
                        env.CHAR_PATH,
                        name,
                        env.MAYA_TYPE,
                        env.SCN_TYPE )
    os.system('explorer.exe %s'%path)

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