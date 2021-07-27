import os, shutil
import env


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
                editToRename = os.path.join(path , env.E_DIR , dpt , "data" , env.TMP_SCN_E + n)
                editRenamed = os.path.join(path , env.E_DIR , dpt , "data" , assetName + "_E_" + dpt + "_001" + n)
                publishToRename = os.path.join(path , env.P_DIR , dpt , env.TMP_SCN_P + n)
                publishRenamed = os.path.join(path , env.P_DIR , dpt , assetName + "_P_" + dpt + n)
                os.rename(editToRename, editRenamed)
                os.rename(publishToRename, publishRenamed)
        # PROFILE PICTURE
        picSrc = os.path.join(env.SERVER , prod, env.LIB_IMG, "template.png")
        picDst = os.path.join(env.SERVER , prod, env.LIB_IMG, env.TYPE_CHAR,"template.png")
        picRenamed = os.path.join(env.SERVER, prod, env.LIB_IMG, env.TYPE_CHAR , assetName + ".png")
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
        picSrc = os.path.join(env.SERVER , prod, env.LIB_IMG, "template.png")
        picDst = os.path.join(env.SERVER , prod, env.LIB_IMG, env.TYPE_PROP,"template.png")
        picRenamed = os.path.join(env.SERVER, prod, env.LIB_IMG, env.TYPE_PROP , assetName + ".png")
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
    project = os.path.join(path,  destination[-1])
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
            editPath = os.path.join(newPath , env.E_DIR , dpt, "data" )
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
