import sys
sys.path.append("..")
# import package
import os, time, fn, env, fx, json, subprocess #psutil
import os.path
from os import PathLike, path
'''
from Qt.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from Qt.QtCore import *
from Qt.QtGui import * #QPixmap
from Qt import QtCore, QtGui, QtWidgets
'''
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QPixmap
from PyQt5 import QtGui

from functools import partial


class MainWindow(QWidget) :

    def __init__(self) :
        super(MainWindow,self).__init__()
        self.title = f"ANTARES_v0.6"
        self.icon = os.path.join(env.RESOURCES,
                                "icons",
                                "_UI", "logo.png")
        self.resize(850, 500)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        
        self.createWidget()
        self.createLayout()


    def createWidget(self):

        # SET PREFERENCES #######################################################
        prefs_file = open("prefs.json", "r")
        prefs_json = prefs_file.read()
        prefs = json.loads(prefs_json)


        self.prodTitle = QLabel ( prefs['prod'])
        self.userLabel = QLabel ( "Welcome " + env.USER)
        self.reloadBTN = QPushButton("RELOAD")
        #Set production
        slash = "/"
        path = os.path.join(prefs['server'])
        self.serverName = QLineEdit(r"\\gandalf/3D4_21_22")
        self.folderName = QLineEdit("prefs['folder']")
        self.prodName = QLineEdit(prefs['prod'])
        self.assetDirName = QLineEdit(env.ASSET_TYPE)
        self.shotDirName = QLineEdit(env.SHOT_TYPE)
        self.char_type_name = QLineEdit(env.CHAR_TYPE)
        self.prop_type_name = QLineEdit(env.PROP_TYPE)
        self.fx_type_name = QLineEdit(env.FX_TYPE)
        self.maya_type_name = QLineEdit(env.MAYA_TYPE)
        self.sculpt_type_name = QLineEdit(env.SCULPT_TYPE)
        self.scn_type_name = QLineEdit(env.SCN_TYPE)
        self.edit_type_name = QLineEdit(env.EDIT_TYPE)
        self.publish_type_name = QLineEdit(env.PUBLISH_TYPE)
        self.server_LBL = QLabel ( "SERVER" )
        self.prod_LBL = QLabel ( "CURRENT PROD" )
        self.assetDir_LBL = QLabel ( "CURRENT ASSET DIR" ) 
        self.shotDir_LBL = QLabel ( "CURRENT SHOT DIR" )
        self.char_type_LBL = QLabel ( "ASSET TYPE CHARACTER" )
        self.prop_type_LBL = QLabel ( "ASSET_TYPE PROP" )
        self.fx_type_LBL = QLabel ( "ASSET TYPE FX " )
        self.maya_type_LBL = QLabel ( "SOFT MAYA" )
        self.sculpt_type_LBL = QLabel ( "SOFT SCULPT" )
        self.scn_type_LBL = QLabel ( "SCENES DIR" )
        self.edit_type_LBL = QLabel ( "WORK DIR" )
        self.publish_type_LBL = QLabel ( "PUBLISH DIR" )                

        self.prodLabel = QLabel ( "Enter Server and Production Name")
        self.createProd = QPushButton("Create Production")
        self.setProd = QPushButton("Set Production")
        #NEW ASSETS
        self.newCharBTN = QPushButton("NEW CHARACTER")
        self.newPropBTN = QPushButton("NEW PROP (to do)")
        self.itemBTN = QPushButton("NEW ITEM (to do)")
        self.libraryBTN = QPushButton("NEW IMAGES_PATHRARY (to do)")
        self.setBTN = QPushButton("NEW SET (to do)")
        self.newFX_BTN = QPushButton("NEW HIP")
        self.incrementSave = QPushButton("INCREMENT AND SAVE")
        #RENAME ASSET
        self.assetName_LBL = QLabel ( "Please Enter New Asset Name")
        self.assetName = QLineEdit("Antares")
        self.oldName = QLineEdit("Antares")
        self.newName = QLineEdit("NewName")
        self.newNameLabel = QLabel ( "New Name")
        self.oldNameLabel = QLabel ( "Old Name")
        self.renameButton = QPushButton("Rename Asset")
        #PLUG-INS
        self.plugIn_Label = QLabel ( "Load Plug-ins")
        self.checkBoxAbc = QCheckBox("Abc Import/Export")
        self.checkBoxMash = QCheckBox("MASH")
        self.checkBoxRenderMan = QCheckBox("Pixar RenderMan")
        for check in [self.checkBoxAbc, self.checkBoxMash, self.checkBoxRenderMan]:
            check.setChecked(True)


        #PREFS MENU
        self.shortcut_LBL = QLabel ( "Access to some shortcuts" )
        self.resources_BTN = QPushButton("RESOURCES")
        self.maya_prefs_BTN = QPushButton("MAYA PREFERENCES")
        self.library_LBL = QLabel ( "Modify Assets and User profile pictures" )
        self.library_BTN = QPushButton("MODIFY LIBRARY")
        self.user_BTN = QPushButton("MODIFY USER PROFILE PICTURE")
        self.theme_LBL = QLabel ( "Choose your theme" )
        self.defaultTheme_BTN = QPushButton("Default Theme")
        self.darkTheme_BTN = QPushButton("Dark Theme")
        
        #IN MENU
        self.last_edit_LBL = "Open Last Edit "
        self.open_publish_LBL = "Open Publish"
        self.ref_publish_LBL = "Reference Publish"
        self.import_publish_LBL = "Import Publish"
        self.open_in_folder_LBL = "Open In Folder"
        self.duplicate_asset_LBL = "Duplicate Asset"
        self.delete_asset_LBL = "Delete Asset"
        self.create_new_task_LBL = "Create New Task"

        #CONNECTIONS
        self.newCharBTN.clicked.connect(self.createNewChara_UI)
        self.newPropBTN.clicked.connect(self.createNewProp_UI)
        self.newFX_BTN.clicked.connect(self.create_new_FX_UI)
        self.renameButton.clicked.connect(self.renameAsset_UI)
        self.reloadBTN.clicked.connect(self.reload)
        self.setProd.clicked.connect(self.setProd_FN)



    def createLayout(self):
        # LAYOUT HIERARCHY
        outerLayout = QGridLayout()
        topLayout = QHBoxLayout()
        Layout_L = QVBoxLayout()
        tabsLayout_L = QTabWidget()
        tab01_Lay_L = QWidget()
        tab02_Lay_L = QWidget()
        up_tab01_Layout_L = QVBoxLayout()
        mid_tab01_Layout_L = QGridLayout()
        dwn_tab01_Layout_L = QVBoxLayout()
        main_tab02_Layout_L = QVBoxLayout()
        Layout_R = QVBoxLayout()
        tabs_Lay_R = QTabWidget()
        Separador = QFrame()
        
        #ADD WIDGETS
        topLayout.addWidget(self.userLabel)
        topLayout.addWidget(self.prodTitle)
        topLayout.addWidget(self.reloadBTN)
        for widget in [self.prodLabel,
                        self.createProd,
                        self.setProd]:
            up_tab01_Layout_L.addWidget(widget)

        mid_tab01_Layout_L.addWidget(self.serverName, 0,1)
        mid_tab01_Layout_L.addWidget(self.prodName, 1,1)
        mid_tab01_Layout_L.addWidget(self.assetDirName, 2,1)
        mid_tab01_Layout_L.addWidget(self.shotDirName, 3,1)
        mid_tab01_Layout_L.addWidget(self.char_type_name, 4,1)
        mid_tab01_Layout_L.addWidget(self.prop_type_name, 5,1)
        mid_tab01_Layout_L.addWidget(self.fx_type_name, 6,1)
        mid_tab01_Layout_L.addWidget(self.maya_type_name, 7,1)
        mid_tab01_Layout_L.addWidget(self.sculpt_type_name, 8,1)
        mid_tab01_Layout_L.addWidget(self.scn_type_name, 9,1)
        mid_tab01_Layout_L.addWidget(self.edit_type_name, 10,1)
        mid_tab01_Layout_L.addWidget(self.publish_type_name, 11,1)
        
        mid_tab01_Layout_L.addWidget(self.server_LBL, 0,0)
        mid_tab01_Layout_L.addWidget(self.prod_LBL, 1,0)
        mid_tab01_Layout_L.addWidget(self.assetDir_LBL, 2,0)
        mid_tab01_Layout_L.addWidget(self.shotDir_LBL, 3,0)
        mid_tab01_Layout_L.addWidget(self.char_type_LBL, 4,0)
        mid_tab01_Layout_L.addWidget(self.prop_type_LBL, 5,0)
        mid_tab01_Layout_L.addWidget(self.fx_type_LBL, 6,0)
        mid_tab01_Layout_L.addWidget(self.maya_type_LBL, 7,0)
        mid_tab01_Layout_L.addWidget(self.sculpt_type_LBL, 8,0)
        mid_tab01_Layout_L.addWidget(self.scn_type_LBL, 9,0)
        mid_tab01_Layout_L.addWidget(self.edit_type_LBL, 10,0)
        mid_tab01_Layout_L.addWidget(self.publish_type_LBL, 11,0)

        mid_tab01_Layout_L.addWidget(Separador, 12,0)
        

        mid_tab01_Layout_L.addWidget( self.oldNameLabel, 13,0 )
        mid_tab01_Layout_L.addWidget( self.oldName, 13, 1 )
        mid_tab01_Layout_L.addWidget( self.newNameLabel , 14,0)
        mid_tab01_Layout_L.addWidget( self.newName , 14,1)
        mid_tab01_Layout_L.addWidget(self.renameButton, 15,0)

        for widget in [self.plugIn_Label,
                        self.checkBoxAbc,
                        self.checkBoxMash,
                        self.checkBoxRenderMan]:
            dwn_tab01_Layout_L.addWidget(widget)
        Layout_L.addWidget(tabsLayout_L)
        Layout_R.addWidget(tabs_Lay_R)


        for widget in [self.shortcut_LBL,
                        self.resources_BTN,
                        self.maya_prefs_BTN,
                        self.library_LBL,
                        self.library_BTN,
                        self.user_BTN,
                        self.theme_LBL,
                        self.defaultTheme_BTN,
                        self.darkTheme_BTN]:
            main_tab02_Layout_L.addWidget(widget)

        tabsLayout_L.addTab(tab01_Lay_L, "HOME")
        tabsLayout_L.addTab(tab02_Lay_L, "PREFS")
        tabs_Lay_R.addTab(self.assetTabUI(), "ASSETS")
        tabs_Lay_R.addTab(self.shotTabUI(), "SHOTS")
        tabs_Lay_R.addTab(self.setTabUI(), "SETS")


        #ADD LAYOUTS
        up_tab01_Layout_L.addLayout(mid_tab01_Layout_L)
        up_tab01_Layout_L.addLayout(dwn_tab01_Layout_L)
        outerLayout.addLayout(topLayout, 1, 0, 1, 2)
        outerLayout.addLayout(Layout_L, 2, 0)
        outerLayout.addLayout(Layout_R, 2, 1)
        tab01_Lay_L.setLayout(up_tab01_Layout_L)
        tab02_Lay_L.setLayout(main_tab02_Layout_L)
        
        #SET CUSTOM
        outerLayout.setColumnStretch(1,1)
        up_tab01_Layout_L.addStretch(1)
        up_tab01_Layout_L.setSpacing(5)
        main_tab02_Layout_L.addStretch(1)
        tabsLayout_L.setTabPosition(tabsLayout_L.West)
        tabsLayout_L.setMovable(True)
        Separador.setFrameShape(QFrame.HLine)
        Separador.setLineWidth(1)
        # tabsLayout_L.tabBarClicked(self.openTab)

        self.setLayout(outerLayout)

        

        self.show()
    
    #############

    # ASSETS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def assetTabUI(self):
        Separador = QFrame()
        Separador.setFrameShape(QFrame.HLine)
        Separador.setLineWidth(1)

        outLayout = QWidget()
        globalLayout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.mayaTab_UI(), "MAYA")
        tabs.addTab(self.houdiniTab_UI(), "HOUDINI")
        globalLayout.addWidget(self.assetName_LBL)
        globalLayout.addWidget(self.assetName)
        globalLayout.addWidget(Separador)
        globalLayout.addWidget(tabs)
        outLayout.setLayout(globalLayout)
        return outLayout
    
    def mayaTab_UI(self):
        server = self.serverName.text()
        cwd = os.getcwd
        print ( cwd )
        if os.path.exists(server):
            server = self.serverName.text()
            print ( server )

            if os.path.exists(os.path.join(server,
                                        self.prodName.text())):
                prod = self.prodName.text()
                print ( prod )
                print ( "production set")
            else:
                server = env.TMP_SERVER
                print ( server )
                prod = env.TMP_PROD
                print ( prod )
                print ( "error prod")

        else:
            server = env.TMP_SERVER
            print ( server )
            prod = env.TMP_PROD
            print ( prod )
            print ( "error server")
        

        mayaTab = QWidget() 
        base = QGridLayout()
        groupChara = QGroupBox("CHARACTERS")
        groupProp = QGroupBox("PROPS")
        # groupSet = QGroupBox("SETS")
        base.addWidget(groupChara)
        base.addWidget(groupProp)
        # base.addWidget(groupSet)
        base.addWidget(self.incrementSave)

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = FlowLayout()
        groupChara.setLayout(layoutChar)
        #Variable
        characterPath = os.path.join(server,
                                    prod,
                                    env.CHAR_PATH)
        assetcharacter = os.listdir( characterPath )
        print (characterPath)
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            if name == '':
                continue
            imageDir = os.path.join(env.TMP_SERVER,
                                    env.IMAGES_PATH,
                                    env.CHAR_TYPE,
                                    name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                prod)
            layoutChar.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(characterPath ,
                                                        name ,
                                                        env.E_PATH))
            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )
            menu.addSeparator()
            for dep in departmentList:
                #VARIABLES
                path = os.path.join(characterPath ,
                                    name ,
                                    env.E_PATH ,
                                    dep)
                editProject = os.listdir( os.path.join(path ,
                                                    "_data" ))

                editImage = os.path.join(path ,
                                    "_data",
                                    editProject[-2])

                publishImage = os.path.join(characterPath ,
                                    name ,
                                    env.P_PATH ,
                                    dep ,
                                    name + "_P_" + dep + ".png")

                destination = os.listdir( os.path.join(server,
                                    prod ,
                                    env.CHAR_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))

                file = os.path.join(server,
                                    prod ,
                                    env.CHAR_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ,
                                    destination[-1])

                modified = os.path.getmtime(file)
                year,month,day,hour,minute,second=time.localtime(modified)[:-3]
                date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                allEdits = os.listdir(os.path.join( server ,
                                     
                                    prod ,
                                    env.CHAR_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))

                #SubMenu
                items = menu.addMenu(dep)
                lastEdit = items.addAction(QIcon(editImage), self.last_edit_LBL + "( " + date + " )" )
                openPublish = items.addAction(QIcon(publishImage), self.open_publish_LBL +  " ( " + date + " )")
                
                Edits = items.addMenu("All Edits")
                for i in allEdits:
                    Edits.addAction(i + " (" + date + ") (To Do)")  
                refPublish = items.addAction(self.ref_publish_LBL)
                importPublish = items.addAction(self.import_publish_LBL)

                #CONNECTIONS
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep)) 
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))  
                refPublish.triggered.connect(partial(self.refPublish_UI, name, dep)) 
                importPublish.triggered.connect(partial(self.importPublish_Char_UI, name, dep)) 
                



            #MENU ITEMS GLOBAL
            sculpt = menu.addMenu("sculpt")
            sculpt_path = os.listdir(os.path.join(server,
                                         
                                        prod,
                                        env.CHAR_PATH,
                                        name,
                                        env.SCULPT_TYPE))
            for soft in sculpt_path:
                actions = sculpt.addMenu(soft)
                lastSculpt = actions.addAction(self.last_edit_LBL)
                actions.addAction(self.open_in_folder_LBL)

                lastSculpt.triggered.connect(partial(self.openLastSculpt_UI, name, soft)) 


            menu.addSeparator()
            openInFolder = menu.addAction(self.open_in_folder_LBL)
            menu.addAction(self.duplicate_asset_LBL)
            delete = menu.addAction(self.delete_asset_LBL)
            menu.addAction(self.create_new_task_LBL)
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_UI, name))
            openInFolder.triggered.connect(partial(self.openInFolder_Char_UI, name)) 

            

            button.setMenu(menu)
        #New Chara Button
        self.newCharBTN.setFixedSize(100, 100)
        layoutChar.addWidget(self.newCharBTN)
        #SET PROP GROUP
        layoutProp = FlowLayout()
        groupProp.setLayout(layoutProp)
        #New Chara Buttons
        self.newPropBTN.setFixedSize(100, 100)
        layoutProp.addWidget(self.newPropBTN)

        mayaTab.setLayout(base)
        return mayaTab

    def houdiniTab_UI(self):
        server = self.serverName.text()
        folder = self.folderName.text()
        if os.path.exists(server):
            server = self.serverName.text()
            print ( server )

            if os.path.exists(os.path.join(server,
                                        self.prodName.text())):
                prod = self.prodName.text()
                print ( prod )
            else:
                server = env.TMP_SERVER
                print ( server )
                prod = env.TMP_PROD
                print ( prod )

        else:
            server = env.TMP_SERVER
            print ( server )
            prod = env.TMP_PROD
            print ( prod )

        houdini_Tab = QWidget()
        base = QGridLayout()
        group_01 = QGroupBox("FX")
        base.addWidget(group_01)
        flowLayout = FlowLayout()
        group_01.setLayout(flowLayout)
        

        #Variable
        fx_Path = os.path.join(server,
                                    prod,
                                    env.FX_PATH)
        assetcharacter = os.listdir( fx_Path )
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    env.IMAGES_PATH,
                                    env.FX_TYPE,
                                    name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                 
                                prod,
                                env.FX_PATH,
                                name)
            flowLayout.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            asset_list = os.listdir( os.path.join(fx_Path ,
                                                    name ))
            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )
            menu.addSeparator()

            for dep in ["abc", "audio", "comp", "desk", "flip", "geo", "hdz", "render", "scripts", "sim", "tex", "video"]:

                editProject = os.listdir( os.path.join(path ,
                                                    "_data" ))

                editImage = os.path.join(path ,
                                    "_data",
                                    editProject[-1])
                #SubMenu
                items = menu.addAction(dep)
                items.triggered.connect(partial(self.openInFolder_Char_UI, name))
                

            #MENU ITEMS GLOBAL

            menu.addSeparator()
            lastEdit = menu.addAction(QIcon(editImage), self.last_edit_LBL )
            delete = menu.addAction(self.delete_asset_LBL)
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_UI, name))
            lastEdit.triggered.connect(partial(self.open_last_FX_UI, name)) 

            

            button.setMenu(menu)

        self.newFX_BTN.setFixedSize(100, 100)
        flowLayout.addWidget(self.newFX_BTN)

        houdini_Tab.setLayout(base)
        return houdini_Tab

    # SHOTS -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def shotTabUI(self):
        server = self.serverName.text()
        folder = self.folderName.text()
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        # seqDIR = os.listdir(os.path.join(server,
                                        #  
                                        # prod,
                                        # env.SHOT_TYPE))
        # for seq in seqDIR :
        #     tabs.addTab(self.insideShotTabUI(), seq)
        n.addWidget(tabs)
        layout.setLayout(n)
        return layout
  
    def insideShotTabUI(self):
        houdiniTab = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("seq0010_sh0010"))
        self.cb = QComboBox()
        self.cb.addItem("Tractor On")
        self.cb.addItem("Tractor Off")
        layout.addWidget(self.cb)
        houdiniTab.setLayout(layout)
        return houdiniTab

    # SETS -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def setTabUI(self):

        server = self.serverName.text()
        folder = self.folderName.text()
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        # setDIR = os.listdir(os.path.join(server,
                                         
        #                                 prod,
        #                                 env.SET_PATH))
        # for setName in setDIR :
        #     tabs.addTab(self.moduleTabUI(setName), setName)
        n.addWidget(tabs)
        n.addWidget(self.setBTN)
        n.addWidget(self.libraryBTN)
        n.addWidget(self.itemBTN)
        layout.setLayout(n)
        return layout
    
    def moduleTabUI(self, setName):
        server = self.serverName.text()
        folder = self.serverName.text()
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        moduleDIR = os.listdir(os.path.join(server,
                                            prod,
                                            env.SET_PATH,
                                            setName))
        for modName in moduleDIR :
            tabs.addTab(self.itemTabUI(setName, modName), modName)
        
        n.addWidget(tabs)
        
        layout.setLayout(n)
        return layout

    def itemTabUI(self, setName, modName):
        server = self.serverName.text()
        folder = self.serverName.text()
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        item = QPushButton()
        itemDIR = os.listdir(os.path.join(server,
                                             
                                            prod,
                                            env.SET_PATH,
                                            setName,
                                            modName))

        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, itemDIR):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    env.IMAGES_PATH,
                                    "items",
                                    name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                     
                                    prod)
            n.addWidget(button)
            

        layout.setLayout(n)

        return layout

    ## CONNECTIONS UI ##

    def createNewChara_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        if not prod:
            return
        if not assetName:
            return
        fn.newCharFN( server = server, prod = prod, assetName = assetName)
        self.reload()

    def createNewProp_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        if not prod:
            return
        if not assetName:
            return
        fn.newPropFN(prod = prod, assetName = assetName)
        self.reload()

    def create_new_FX_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        if not prod:
            return
        if not assetName:
            return
        fx.newFX_FN(  server, prod = prod, assetName = assetName)
        self.reload()

    def openLastEdit_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        print ( prod )
        print ( server )
        if not server:
            return
        fn.openLastEdit_FN (  name, dep, server, prod = prod)
    
    def openPublish_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        fn.openPublish_FN (  name, dep, prod = prod, server = server)

    def deleteAsset_UI(self, name):
        
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()

        fn.deleteAsset_FN(  name, server,  prod = prod)
        self.reload()

    def renameAsset_UI(self):
        prod = self.prodName.text()
        oldName = self.oldName.text()
        newName = self.newName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        print ( newName )
        fn.renameAsset_FN (   server, prod = prod, oldName = oldName, newName = newName)
        self.reload()

    def test_UI(self):
        fn.testFN()

    def refPublish_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        fn.refPublishFN(  name, dep, prod = prod, server = server)

    def importPublish_Char_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        fn.importPublish_Char_FN(  name, dep, prod = prod, server = server)

    def openInFolder_Char_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        fn.openInFolder_Char_FN(  name, server, prod = prod)
   
    def openLastSculpt_UI(self, name, soft):
        prod = self.prodName.text()
        server = self.serverName.text()

        if not server:
            return
        fn.openLastSculpt_FN (name, soft, server, prod = prod)
  
    def open_last_FX_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fx.open_last_FX_FN (name, server, prod = prod)

    ## UI CUSTOMIZE ##

    def openTab(self, tab01_Lay_L, up_tab01_Layout_L):
        tab01_Lay_L.setLayout(up_tab01_Layout_L)

    def reload(self):
        
        self.close() 
        MainWindow()
        
    def setProd_FN(self):
        server = self.serverName.text()
        prod = self.prodName.text()
        
        listOfStr = ["server",
                    "prod",
                    "tmp_server",
                    "tmp_package",
                    "tmp_appli",
                    "tmp_version",
                    "tmp_resources",
                    "tmp_prod"]
        listOfTxt = [server,
                    prod,
                    "S:\\",
                    "packages",
                    "antares",
                    "dev",
                    "resources",
                    "template_pipeline_film"]

        zipObj = zip(listOfStr, listOfTxt)
        new_dico = dict(zipObj)
        base_file = open("prefs.json", "w")
        json.dump(new_dico, base_file)
        base_file.close()

        self.reload()

class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=-1, spacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._margin = margin
        if parent is not None:
            self.setMargin(margin)
        self.setSpacing(spacing)
        self.itemList=[]

    def margin(self):
        return self._margin

    def __del__(self):
        item=self.takeAt(0)
        while item:
            item=self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]
        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height=self._doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size=QSize()
        for item in self.itemList:
            size=size.expandedTo(item.minimumSize())
        size += QSize(2 * self.margin(), 2 * self.margin())
        return size

    def _doLayout(self, rect, testOnly):
        x=rect.x()
        y=rect.y()
        lineHeight=0
        for item in self.itemList:
            wid=item.widget()
            spaceX=self.spacing() 
            spaceY=self.spacing() 
            nextX=x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x=rect.x()
                y=y + lineHeight + spaceY
                nextX=x + item.sizeHint().width() + spaceX
                lineHeight=0
            if not testOnly:
                item.setGeometry(
                    QRect(QPoint(x, y), item.sizeHint()))
            x=nextX
            lineHeight=max(lineHeight, item.sizeHint().height())
        return y + lineHeight - rect.y()

class ImagePushButton(QPushButton):

    def __init__(self, *args, **kwargs):
        path = kwargs.pop("path")
        super(ImagePushButton, self).__init__(*args, **kwargs)
        self.set_image(path)

    def set_image(self, path):
        icon = QImage(path)
        icon = icon.scaled(
            self.width(), 
            self.height(),  
            Qt.IgnoreAspectRatio, 
            Qt.SmoothTransformation
        )
        self.pixmap = QPixmap()
        self.pixmap.convertFromImage(icon)
        self.update()

    def paintEvent(self, event):
        super(ImagePushButton, self).paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(QRect(QPoint(2,2),QSize(88,88)), self.pixmap)        

if __name__ == "__main__":
    
    application = QApplication(sys.argv)

    # application.setStyle('Fusion')
    file = QFile("./darkTheme.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    application.setStyleSheet(stream.readAll())

    window = MainWindow()
    # window.setupData()

    sys.exit(application.exec_())


else:
    window = None