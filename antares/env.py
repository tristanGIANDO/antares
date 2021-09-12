import  os


#Global Path
# SERVER = os.path.join("C:\\", "Users", "Windows", "Desktop")
# SERVER = os.path.join("C:\\", "Users", "stage", "Desktop")
# SERVER = os.path.join("C:\\", "Users", "Manon", "Documents", "antares-main", "antares", "resources")
SERVER = os.path.join("S:\\", "packages", "antares", "dev", "antares", "resources")
RESOURCES = os.path.join("S:\\", "packages", "antares", "dev", "antares", "resources")


#Set Templates

userComplete = str(os.listdir(os.path.join(SERVER, "icons", "_user")))
userSplitText = userComplete.replace('.png', '')
userSplitCroc01 = userSplitText.replace("['", "")
userSplit = userSplitCroc01.replace("']", "")
USER = userSplit
TMP_PROD = "template_pipeline_film"
TMP_ASSET = "_template_workspace_asset"
TMP_FX = "_template_workspace_houdini"
TMP_SCN_FX = "template_001.hipnc"
TMP_SCN_TYPE_E = "template_E_modeling_001"
TMP_SCN_TYPE_P = "template_P_assetLayout"
TMP_SCN_TYPE_SCULPT = "template_E_sculpt_001"
TMP_IMAGE = "template.png"
# Set Directories"
ASSET_TYPE = "04_asset"
SHOT_TYPE = "05_shot"
CHAR_TYPE = "character"
PROP_TYPE = "prop"
FX_TYPE = "FX"
MAYA_TYPE= "maya"
SCULPT_TYPE = "sculpt"
SCN_TYPE = "scenes"
EDIT_TYPE = "edit"
PUBLISH_TYPE = "publish"
# Path
IMAGES_PATH = os.path.join("icons", "_library", "Images")
TMP_ASSET_PATH = os.path.join(ASSET_TYPE,TMP_ASSET)
TMP_FX_PATH = os.path.join(ASSET_TYPE,TMP_FX)
SET_PATH = os.path.join(ASSET_TYPE, "set")
E_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, EDIT_TYPE)
P_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, PUBLISH_TYPE)
CHAR_PATH = os.path.join(ASSET_TYPE, CHAR_TYPE )
PROP_PATH = os.path.join(ASSET_TYPE, PROP_TYPE )
FX_PATH = os.path.join(ASSET_TYPE, FX_TYPE )

PORT = 1789