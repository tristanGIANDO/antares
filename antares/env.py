import  os


#Global Path
# SERVER = os.path.join("C:\\", "Users", "Windows", "Desktop")
# SERVER = os.path.join("C:\\", "Users", "stage", "Desktop")
# SERVER = os.path.join("C:\\", "Users", "Manon", "Documents", "antares-main", "antares", "resources")
SERVER = os.path.join("S:\\", "packages", "antares", "dev", "antares", "resources")

CURRENT_PROD = "template_pipeline_film"
#Set Templates
userComplete = str(os.listdir(os.path.join(SERVER, "icons", "_user")))
userSplitText = userComplete.replace('.png', '')
userSplitCroc01 = userSplitText.replace("['", "")
userSplit = userSplitCroc01.replace("']", "")
USER = userSplit
TMP_ASSET = "_template_workspace_asset"
TMP_SCN_E = "template_E_modeling_001"
TMP_SCN_P = "template_P_assetLayout"
# Set Directories"
ASSET_DIR = "04_asset"
SHOT_DIR = "05_shot"
SET_DIR = os.path.join(ASSET_DIR, "set")
TYPE_CHAR = "character"
TYPE_PROP = "prop"
CURRENT_SOFT= "maya"
SCN = "scenes"
E_DIR = "edit"
P_DIR = "publish"
LIB_IMG = os.path.join("11_library","Images")
LIB = os.path.join("icons", "_library", "Images")
SRC = os.path.join(ASSET_DIR,TMP_ASSET)
E_DIR = os.path.join(CURRENT_SOFT, SCN, E_DIR)
P_DIR = os.path.join(CURRENT_SOFT, SCN, P_DIR)
TYPE_CHAR_PATH = os.path.join(ASSET_DIR, TYPE_CHAR )
TYPE_PROP_PATH = os.path.join(ASSET_DIR, TYPE_PROP )