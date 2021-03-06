import  os, json



prefs_file = open("prefs.json", "r")
prefs_json = prefs_file.read()
prefs = json.loads(prefs_json)


VERSION = "2.0"

#Set Templates
server = r"\\gandalf\3D4_21_22"
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
ICON = os.path.join(server,
                                "_partage",
                                "ANTARES",
                                prefs['tmp_package'],
                                prefs['tmp_appli'],
                                prefs['tmp_version'],
                                prefs['tmp_appli'],
                                "logo.ico")

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
TMP_SEQ_TYPE_NUKE = "FILM_s0010_sh0010"
TMP_SCN_TYPE_NUKE = "comp.nk"
TMP_SCN_TYPE_NUKE_TRUE = "template_comp.nk"
TMP_SCN_TYPE_SHOT = "template_shot.ma"
TMP_IMAGE = "template.png"
TMP_FRAME = "XXXX-XXXX.txt"

# Set Directories"
ASSET_TYPE = "04_asset"
SHOT_TYPE = "05_shot"
COMPO_TYPE = "06_compo"
EDITING_TYPE = "07_editing"
DELIVERY_TYPE = "00_delivery"
CHAR_TYPE = "character"
PROP_TYPE = "prop"
SET_TYPE = "set"
FX_TYPE = "FX"
HOUDINI_TYPE = "houdini"
MAYA_TYPE= "maya"
UNREAL_TYPE = "unreal"
SRC_IMG_TYPE = "sourceimages"
MUDBOX_TYPE = "mudbox"
ZBRUSH_TYPE = "zBrush"
SCULPT_TYPE = "sculpt"
SCN_TYPE = "scenes"
EDIT_TYPE = "edit"
PUBLISH_TYPE = "publish"
RENDER_TYPE = "render"
LAYOUT_TYPE = "layout"
ANIM_TYPE = "anim"
CFX_TYPE = "cfx"
VFX_TYPE = "vfx"
LIBRARY = "_library"
SHOT_LIB = "shot"
RMAN_LIB = "RenderManAssetLibrary"
RMAN_MAT = "Materials"
INPUT_TYPE = "input"
OUTPUT_TYPE = "output"
NON_FILTERED = "nonFiltered"
#DEPARTEMENTS
P_TXT = "_P_"
E_TXT = "_E_"
DATA = "_data"
GEO_LO = "geoLo"
GEO_HI = "geoHi"
DRESSING = "dressing"
#FORMAT
PNG = ".png"
ASCII = ".ma"
SEQ = "seq"
SEQ_ = "_seq"
SHOT_ = "_sh"

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

LAYOUT_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, LAYOUT_TYPE)
ANIM_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, ANIM_TYPE)
RENDER_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, RENDER_TYPE)
CFX_PATH = os.path.join(MAYA_TYPE, SCN_TYPE, CFX_TYPE)
VFX_PATH = os.path.join(HOUDINI_TYPE, SCN_TYPE)
MUDBOX_PATH = os.path.join(SCULPT_TYPE, MUDBOX_TYPE)
ZBRUSH_PATH = os.path.join(SCULPT_TYPE, ZBRUSH_TYPE)
SRC_IMG_PATH = os.path.join(MAYA_TYPE, SRC_IMG_TYPE)

PORT = 1789