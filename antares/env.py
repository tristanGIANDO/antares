import  os, json



prefs_file = open("prefs.json", "r")
prefs_json = prefs_file.read()
prefs = json.loads(prefs_json)


VERSION = "1.1"

#Set Templates
TMP_SERVER = os.path.join(prefs['tmp_server'],
                                prefs['tmp_package'],
                                prefs['tmp_appli'],
                                prefs['tmp_version'],
                                prefs['tmp_appli'],
                                prefs['tmp_resources'])

RESOURCES = os.path.join(prefs['tmp_server'],
                                prefs['tmp_package'],
                                prefs['tmp_appli'],
                                prefs['tmp_version'],
                                prefs['tmp_appli'],
                                prefs['tmp_resources'])

TMP_PROD = prefs['tmp_prod']

ICON = os.path.join(prefs['tmp_server'],
                                prefs['tmp_package'],
                                prefs['tmp_appli'],
                                prefs['tmp_version'],
                                prefs['tmp_appli'],
                                "icon.ico")

userComplete = str(os.listdir(os.path.join("C:\\", "antares_user")))
userSplitText = userComplete.replace('.png', '')
userSplitCroc01 = userSplitText.replace("['", "")
userSplit = userSplitCroc01.replace("']", "")
USER = userSplit
USER_PIC = os.path.join("C:\\",
                        "antares_user",
                        USER + ".png")
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
SET_TYPE = "set"
FX_TYPE = "FX"
MAYA_TYPE= "maya"
SCULPT_TYPE = "sculpt"
SCN_TYPE = "scenes"
EDIT_TYPE = "edit"
PUBLISH_TYPE = "publish"
LIBRARY = "_library"
# Path
IMAGES_PATH = os.path.join("_library", "Images")
TMP_ASSET_PATH = os.path.join(ASSET_TYPE,TMP_ASSET)
TMP_FX_PATH = os.path.join(ASSET_TYPE,TMP_FX)
E_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, EDIT_TYPE)
P_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, PUBLISH_TYPE)
CHAR_PATH = os.path.join(ASSET_TYPE, CHAR_TYPE )
PROP_PATH = os.path.join(ASSET_TYPE, PROP_TYPE )
SET_PATH = os.path.join(ASSET_TYPE, SET_TYPE )
FX_PATH = os.path.join(ASSET_TYPE, FX_TYPE )

PORT = 1789