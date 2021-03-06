import sys
sys.path.append("..")
# import package
import os, time, fn, env, fx, item, prop, shot, json
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
        self.title = f"ANTARES_v" + env.VERSION
        self.icon = env.ICON
        
        self.resize(1000, 600)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        
        print ( ">>  Welcome on ANTARES v" + env.VERSION + "  <<")
        print ("")
        print ( "Created by Tristan Giandoriggio")
        print ( "tel = +33651839815" )
        print ( "mail = giando.tristan@gmail.com")
        print ("")

        self.createWidget()
        self.createLayout()

        
   
    def createWidget(self):

        # SET PREFERENCES #######################################################
        prefs_file = open("prefs.json", "r")
        prefs_json = prefs_file.read()
        prefs = json.loads(prefs_json)

        self.prodTitle = QLabel ( prefs['prod'])
        self.userPic = QLabel ( "Welcome ")
        self.userLabel = QLabel ( "Welcome " + env.USER)
        self.pixmap = QPixmap(env.USER_PIC)
        self.reloadBTN = QPushButton("RELOAD")
        #Set production
        self.serverName = QLineEdit(r"\\gandalf/3D4_21_22")
        # self.serverName = QLineEdit(r"D:\\")
        self.tmp_server_Name = QLineEdit(prefs['tmp_server'])
        self.prodName = QLineEdit(prefs['prod'])
        self.prefixName = QLineEdit(prefs['prefix'])
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
        self.prefix_LBL = QLabel ( "PREFIX" )
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
        self.newPropBTN = QPushButton("NEW PROP")
        self.new_item_BTN = QPushButton("NEW ITEM")
        self.new_module_BTN = QPushButton("NEW MODULE")
        self.new_set_BTN = QPushButton("NEW SET")
        self.newFX_BTN = QPushButton("NEW HIP")
        self.newFX_BTN = QPushButton("NEW HIP")

        self.new_seq_BTN = QPushButton("NEW SEQ")
        self.new_shot_BTN = QPushButton("NEW SHOT")
        self.new_seq_LBL = QLabel ( "N??SEQ >> seq" )
        self.new_seq_TXT = QLineEdit("XXXX")
        self.new_shot_LBL = QLabel ( "N??SHOT >> sh")
        self.new_shot_TXT = QLineEdit("XXXX")

        


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
        self.shot_Label = QLabel ( "Coming Soon !")
        self.edit_Label = QLabel ( "Coming Soon !")

        #PREFS MENU
        self.shortcut_LBL = QLabel ( "Access to some shortcuts" )
        self.resources_BTN = QPushButton("Resources of << " + prefs['prod'] + " >>")
        self.antares_for_maya_BTN = QPushButton("ANTARES FOR MAYA")
        self.library_LBL = QLabel ( "Modify Assets and User profile pictures" )
        self.library_BTN = QPushButton("MODIFY LIBRARY")
        self.user_BTN = QPushButton("MODIFY USER PROFILE PICTURE")
        self.theme_LBL = QLabel ( "Choose your theme" )
        self.lightTheme_BTN = QPushButton("Light Theme")
        self.darkTheme_BTN = QPushButton("Dark Theme")
        
        #IN MENU
        self.last_edit_LBL = "Open Last Edit "
        self.open_publish_LBL = "Open Publish"
        self.ref_publish_LBL = "Reference Publish (open socket)"
        self.import_publish_LBL = "Import Publish (open socket)"
        self.open_in_folder_LBL = "Open In Folder"
        self.duplicate_asset_LBL = "Duplicate Asset (to do)"
        self.delete_asset_LBL = "Delete Asset !!"
        self.delete_module_LBL = "Delete Module !!"
        self.rename_asset_LBL = "Rename Asset"
        self.create_new_task_LBL = "Create New Task (to do)"
        self.new_item_LBL = "Create New Item"
        self.substance_LBL = "Create Substance Library"
        self.dressing_LBL = "DRESSING"
        
        # self.progress = QProgressBar(self)
        # self.progress.setGeometry(830,10,150,20)
        # self.progress.setValue(0)

       
        '''
        # CONNECTIONS
        '''

        self.newCharBTN.clicked.connect(self.createNewChara_UI)
        self.newPropBTN.clicked.connect(self.createNewProp_UI)
        self.newFX_BTN.clicked.connect(self.create_new_FX_UI)
        self.renameButton.clicked.connect(self.rename_char_UI)
        self.reloadBTN.clicked.connect(self.reload)
        self.setProd.clicked.connect(self.setProd_FN)
        self.library_BTN.clicked.connect(self.open_library_UI)
        self.resources_BTN.clicked.connect(self.open_resources_UI)
        self.user_BTN.clicked.connect(self.open_user_picture_UI)
        self.antares_for_maya_BTN.clicked.connect(self.open_prefs_UI)
        self.new_module_BTN.clicked.connect(self.create_new_module_UI)
        self.new_item_BTN.clicked.connect(self.create_new_item_UI)
        self.new_seq_BTN.clicked.connect(self.create_new_seq_UI)
        self.new_shot_BTN.clicked.connect(self.create_new_shot_UI)

        self.userPic.setPixmap(self.pixmap)
        self.prodTitle.setFont(QFont('Times', 30))

    def createLayout(self):
        server = self.serverName.text()
        prod = self.prodName.text()

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

        # create menu
        menubar = QMenuBar()

        outerLayout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        menubar.addMenu("Help")
        
     
        #ADD WIDGETS
        topLayout.addWidget(self.userPic)
        topLayout.addWidget(self.userLabel)
        topLayout.addWidget(self.prodTitle)
        topLayout.addWidget(self.reloadBTN)
        
        up_tab01_Layout_L.addWidget(self.prodLabel)
        mid_tab01_Layout_L.addWidget(self.serverName, 0,1)
        mid_tab01_Layout_L.addWidget(self.prodName, 1,1)
        mid_tab01_Layout_L.addWidget(self.prefixName, 2,1)
        # mid_tab01_Layout_L.addWidget(self.assetDirName, 2,1)
        # mid_tab01_Layout_L.addWidget(self.shotDirName, 3,1)
        # mid_tab01_Layout_L.addWidget(self.char_type_name, 4,1)
        # mid_tab01_Layout_L.addWidget(self.prop_type_name, 5,1)
        # mid_tab01_Layout_L.addWidget(self.fx_type_name, 6,1)
        # mid_tab01_Layout_L.addWidget(self.maya_type_name, 7,1)
        # mid_tab01_Layout_L.addWidget(self.sculpt_type_name, 8,1)
        # mid_tab01_Layout_L.addWidget(self.scn_type_name, 9,1)
        # mid_tab01_Layout_L.addWidget(self.edit_type_name, 10,1)
        # mid_tab01_Layout_L.addWidget(self.publish_type_name, 11,1)
        
        mid_tab01_Layout_L.addWidget(self.server_LBL, 0,0)
        mid_tab01_Layout_L.addWidget(self.prod_LBL, 1,0)
        # mid_tab01_Layout_L.addWidget(self.assetDir_LBL, 2,0)
        # mid_tab01_Layout_L.addWidget(self.shotDir_LBL, 3,0)
        # mid_tab01_Layout_L.addWidget(self.char_type_LBL, 4,0)
        # mid_tab01_Layout_L.addWidget(self.prop_type_LBL, 5,0)
        # mid_tab01_Layout_L.addWidget(self.fx_type_LBL, 6,0)
        # mid_tab01_Layout_L.addWidget(self.maya_type_LBL, 7,0)
        # mid_tab01_Layout_L.addWidget(self.sculpt_type_LBL, 8,0)
        # mid_tab01_Layout_L.addWidget(self.scn_type_LBL, 9,0)
        # mid_tab01_Layout_L.addWidget(self.edit_type_LBL, 10,0)
        # mid_tab01_Layout_L.addWidget(self.publish_type_LBL, 11,0)

        mid_tab01_Layout_L.addWidget(Separador, 12,0)
        
        for widget in [#self.createProd,
                        self.setProd]:
            dwn_tab01_Layout_L.addWidget(widget)
            
        # for widget in [self.plugIn_Label,
        #                 self.checkBoxAbc,
        #                 self.checkBoxMash,
        #                 self.checkBoxRenderMan]:
        #     dwn_tab01_Layout_L.addWidget(widget)
        Layout_L.addWidget(tabsLayout_L)
        Layout_R.addWidget(tabs_Lay_R)


        for widget in [self.shortcut_LBL,
                        self.antares_for_maya_BTN,
                        self.resources_BTN,
                        self.library_LBL,
                        self.library_BTN,
                        self.user_BTN]:
                        # self.theme_LBL,
                        # self.lightTheme_BTN,
                        # self.darkTheme_BTN]:
                        # self.tmp_server_Name]:
            main_tab02_Layout_L.addWidget(widget)

        tabsLayout_L.addTab(tab01_Lay_L, "HOME")
        tabsLayout_L.addTab(tab02_Lay_L, "PREFS")
        tabs_Lay_R.addTab(self.assetTabUI(), "ASSETS")
        tabs_Lay_R.addTab(self.shotTabUI(), "SHOTS")
        # tabs_Lay_R.addTab(self.editTabUI(), "EDITING")


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

    '''
    # ASSETS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''

    def assetTabUI(self):

        

        Separador = QFrame()
        Separador.setFrameShape(QFrame.HLine)
        Separador.setLineWidth(1)

        outLayout = QWidget()
        globalLayout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.character_tab_UI(), "CHARACTERS")
        tabs.addTab(self.propsTab_UI(), "PROPS")
        tabs.addTab(self.setTabUI(), "ENVIROS")
        tabs.addTab(self.houdiniTab_UI(), "FX")
        globalLayout.addWidget(self.assetName_LBL)
        globalLayout.addWidget(self.assetName)
        globalLayout.addWidget(Separador)
        globalLayout.addWidget(tabs)
        outLayout.setLayout(globalLayout)
        return outLayout
    
    def character_tab_UI(self):
        server = self.serverName.text()
        
        if os.path.exists(server):
            server = self.serverName.text()
            
            if os.path.exists(os.path.join(server,
                                        self.prodName.text())):
                prod = self.prodName.text()
                
                print ( "production set on", server, " >>>> ", prod)
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
        base.addWidget(groupChara)

        

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = FlowLayout()
        groupChara.setLayout(layoutChar)
        #Variable
        characterPath = os.path.join(server,
                                    prod,
                                    env.CHAR_PATH)
        assetcharacter = os.listdir( characterPath )
        

        #New Chara Button
        self.newCharBTN.setFixedSize(90, 100)
        layoutChar.addWidget(self.newCharBTN)

        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.CHAR_TYPE,
                                    name + env.PNG)
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
                                                    env.DATA ))

                editImage = os.path.join(path ,
                                    env.DATA,
                                    editProject[-1])

                publishImage = os.path.join(characterPath ,
                                    name ,
                                    env.P_PATH ,
                                    dep ,
                                    name + env.P_TXT + dep + env.PNG)

                destination = os.listdir( os.path.join(server,
                                    prod ,
                                    env.CHAR_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))
                #LAST EDIT
                last_path = os.path.join(server,
                            prod,
                            env.CHAR_PATH ,
                            name ,
                            env.E_PATH ,
                            dep)
                destination = os.listdir( last_path )
                try:
                    destination.remove(env.DATA)
                except:
                    print ( "No data")
                last_edit_file = os.path.join(last_path,  destination[-1])
                
                publish_file = os.path.join(server ,
                            prod ,
                            env.CHAR_PATH ,
                            name ,
                            env.P_PATH ,
                            dep ,
                            name + env.P_TXT + dep + env.ASCII)

                # DATE LAST EDIT
                last_edit_modified = os.path.getmtime(last_edit_file)
                year,month,day,hour,minute,second=time.localtime(last_edit_modified)[:-3]
                date_last_edit = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                
                # DATE LAST EDIT
                publish_modified = os.path.getmtime(publish_file)
                year,month,day,hour,minute,second=time.localtime(publish_modified)[:-3]
                publish_date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)

                allEdits = os.listdir(os.path.join( server ,
                                     
                                    prod ,
                                    env.CHAR_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))

                #SubMenu
                items = menu.addMenu(dep)
                lastEdit = items.addAction(QIcon(editImage), self.last_edit_LBL + "( " + date_last_edit + " )" )
                openPublish = items.addAction(QIcon(publishImage), self.open_publish_LBL +  " ( " + publish_date + " )")
                
                Edits = items.addAction("All Edits")  
                refPublish = items.addAction(self.ref_publish_LBL)
                importPublish = items.addAction(self.import_publish_LBL)

                #CONNECTIONS
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep)) 
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))  
                refPublish.triggered.connect(partial(self.refPublish_UI, name, dep)) 
                importPublish.triggered.connect(partial(self.importPublish_Char_UI, name, dep)) 
                Edits.triggered.connect(partial(self.open_in_folder_edits_char_UI, name, dep))
                



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
                openInFolder_sculpt = actions.addAction(self.open_in_folder_LBL)

                lastSculpt.triggered.connect(partial(self.openLastSculpt_UI, name, soft))
                openInFolder_sculpt.triggered.connect(partial(self.open_in_folder_sculpt_char_UI, name, soft)) 


            menu.addSeparator()
            openInFolder = menu.addAction(self.open_in_folder_LBL)
            # menu.addAction(self.duplicate_asset_LBL)
            # renamer = menu.addAction(self.rename_asset_LBL)
            substance = menu.addAction(self.substance_LBL)
            menu.addSeparator()
            delete = menu.addAction(self.delete_asset_LBL)
            # menu.addAction(self.create_new_task_LBL)
            
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_UI, name))
            openInFolder.triggered.connect(partial(self.openInFolder_Char_UI, name)) 
            # renamer.triggered.connect(partial(self.rename_char_UI, name)) 
            substance.triggered.connect(partial(self.substance_char_UI, name))

            

            button.setMenu(menu)
        
        
        

        mayaTab.setLayout(base)
        return mayaTab

    def propsTab_UI(self):
        server = self.serverName.text()

        if os.path.exists(server):
            server = self.serverName.text()
            

            if os.path.exists(os.path.join(server,
                                        self.prodName.text())):
                prod = self.prodName.text()
                
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

        prop_tab = QWidget() 
        base = QGridLayout()
        group_prop = QGroupBox("PROPS")
        base.addWidget(group_prop)

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutProp = FlowLayout()
        group_prop.setLayout(layoutProp)
        #Variable
        prop_path = os.path.join(server,
                                    prod,
                                    env.PROP_PATH)
        assetcharacter = os.listdir( prop_path )
        

        #New Chara Button
        self.newPropBTN.setFixedSize(100, 100)
        layoutProp.addWidget(self.newPropBTN)

        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.PROP_TYPE,
                                    name + env.PNG)
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                prod)
            layoutProp.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(prop_path ,
                                                        name ,
                                                        env.E_PATH))
            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )
            menu.addSeparator()
            for dep in departmentList:
                #VARIABLES
                path = os.path.join(prop_path ,
                                    name ,
                                    env.E_PATH ,
                                    dep)
                editProject = os.listdir( os.path.join(path ,
                                                    env.DATA ))

                editImage = os.path.join(path ,
                                    env.DATA,
                                    editProject[-1])

                publishImage = os.path.join(prop_path ,
                                    name ,
                                    env.P_PATH ,
                                    dep ,
                                    name + env.P_TXT + dep + env.PNG)

                destination = os.listdir( os.path.join(server,
                                    prod ,
                                    env.PROP_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))

                #LAST EDIT
                last_path = os.path.join(server,
                            prod,
                            env.PROP_PATH ,
                            name ,
                            env.E_PATH ,
                            dep)
                destination = os.listdir( last_path )
                try:
                    destination.remove(env.DATA)
                except:
                    print ( "No data")
                last_edit_file = os.path.join(last_path,  destination[-1])
                
                publish_file = os.path.join(server ,
                            prod ,
                            env.PROP_PATH ,
                            name ,
                            env.P_PATH ,
                            dep ,
                            name + env.P_TXT + dep + env.ASCII)

                # DATE LAST EDIT
                last_edit_modified = os.path.getmtime(last_edit_file)
                year,month,day,hour,minute,second=time.localtime(last_edit_modified)[:-3]
                date_last_edit = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                
                # DATE LAST EDIT
                publish_modified = os.path.getmtime(publish_file)
                year,month,day,hour,minute,second=time.localtime(publish_modified)[:-3]
                publish_date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)

                

                #SubMenu
                items = menu.addMenu(dep)
                lastEdit = items.addAction(QIcon(editImage), self.last_edit_LBL + "( " + date_last_edit + " )" )
                openPublish = items.addAction(QIcon(publishImage), self.open_publish_LBL +  " ( " + publish_date + " )")
                
                allEdits = os.listdir(os.path.join( server ,
                                    prod ,
                                    env.PROP_PATH ,
                                    name ,
                                    env.E_PATH ,
                                    dep ))

                Edits = items.addAction("All Edits")
                # for i in allEdits:
                #     Edits.addAction(i + " (" + date + ") (To Do)")  
                # refPublish = items.addAction(self.ref_publish_LBL)
                # importPublish = items.addAction(self.import_publish_LBL)

                #CONNECTIONS
                lastEdit.triggered.connect(partial(self.openLastEdit_prop_UI, name, dep)) 
                openPublish.triggered.connect(partial(self.openPublish_prop_UI, name, dep))  
                Edits.triggered.connect(partial(self.open_in_folder_edits_prop_UI, name, dep))

                



            #MENU ITEMS GLOBAL
            sculpt = menu.addMenu("sculpt")
            sculpt_path = os.listdir(os.path.join(server,
                                         
                                        prod,
                                        env.PROP_PATH,
                                        name,
                                        env.SCULPT_TYPE))
            for soft in sculpt_path:
                actions = sculpt.addMenu(soft)
                lastSculpt = actions.addAction(self.last_edit_LBL)
                openInFolder_sculpt = actions.addAction(self.open_in_folder_LBL)

                lastSculpt.triggered.connect(partial(self.openLastSculpt_prop_UI, name, soft)) 
                openInFolder_sculpt.triggered.connect(partial(self.open_in_folder_sculpt_prop_UI, name, soft)) 


            menu.addSeparator()
            openInFolder = menu.addAction(self.open_in_folder_LBL)
            menu.addAction(self.duplicate_asset_LBL)
            menu.addAction(self.create_new_task_LBL)
            menu.addSeparator()
            delete = menu.addAction(self.delete_asset_LBL)
            substance = menu.addAction(self.substance_LBL)
            substance.triggered.connect(partial(self.substance_prop_UI, name))
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_prop_UI, name))
            openInFolder.triggered.connect(partial(self.openInFolder_prop_UI, name)) 

            

            button.setMenu(menu)
        
        
        

        prop_tab.setLayout(base)
        return prop_tab

    def houdiniTab_UI(self):
        server = self.serverName.text()
        if os.path.exists(server):
            server = self.serverName.text()
            

            if os.path.exists(os.path.join(server,
                                        self.prodName.text())):
                prod = self.prodName.text()
                
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
                                    prod,
                                    env.IMAGES_PATH,
                                    env.FX_TYPE,
                                    name + env.PNG)
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                prod,
                                env.FX_PATH,
                                name)
            editProject = os.listdir( os.path.join(path ,
                                                    env.DATA ))
            editImage = os.path.join(path ,
                                    env.DATA,
                                    editProject[-1])

            flowLayout.addWidget(button)

            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )
            menu.addSeparator()
            department = ["abc", "audio", "comp", "desk", "flip", "geo", "hdz", "render", "scripts", "sim", "tex", "video"]

            for dep in department:
                #SubMenu
                items = menu.addAction(dep)
                items.triggered.connect(partial(self.open_dep_FX_UI, name, dep))
                
            #MENU ITEMS GLOBAL
            menu.addSeparator()
            delete = menu.addAction(self.delete_asset_LBL)
            Edits = menu.addAction("All Edits")
            # for edit in scenes:
            #     Edits.addAction(edit)  
            lastEdit = menu.addAction(QIcon(editImage), self.last_edit_LBL )
            # Edits.triggered.connect(partial(self.open_all_FX_UI, name, edit))
            
            #Connections
            delete.triggered.connect(partial(self.delete_FX_UI, name))
            lastEdit.triggered.connect(partial(self.open_last_FX_UI, name)) 
            Edits.triggered.connect(partial(self.open_in_folder_edits_FX_UI, name))

            

            button.setMenu(menu)

        self.newFX_BTN.setFixedSize(100, 100)
        flowLayout.addWidget(self.newFX_BTN)

        houdini_Tab.setLayout(base)
        return houdini_Tab


    '''
    # SETS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    def setTabUI(self):
        server = self.serverName.text()
        prod = self.prodName.text()
        module_path = os.listdir(os.path.join(server,
                                        prod,
                                        env.SET_PATH))
    

        mayaTab = QWidget() 
        base = QGridLayout()
        groupModules = QGroupBox("MODULES")
        base.addWidget(groupModules)

        

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = FlowLayout()
        groupModules.setLayout(layoutChar)
        #Variable

        #LISTER LES MODULES
        module_path = os.path.join(server,
                                    prod,
                                    env.SET_PATH)
        asset_module = os.listdir( module_path )
        

        #New Module Button
        self.new_module_BTN.setFixedSize(90, 100)
        layoutChar.addWidget(self.new_module_BTN)

        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, asset_module):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.SET_TYPE,
                                    name + env.PNG)
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(server,
                                prod)
            layoutChar.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(module_path ,
                                                        name ,
                                                        env.E_PATH))
            
            try :
                departmentList.remove(env.DRESSING)
            except:
                print ( "No dressing folder")
            
            item_list = os.listdir( os.path.join(module_path,
                                                        name,
                                                        env.E_PATH,
                                                        env.GEO_LO))
            
            try:
                item_list.remove(env.DATA)
            except:
                print ( "No data")


            
            

            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )
            menu.addSeparator()
            #DRESSING
            dress_menu = menu.addMenu(self.dressing_LBL)
            last_dress = dress_menu.addAction(self.last_edit_LBL)
            publish_dress = dress_menu.addAction(self.open_publish_LBL)
            dress_menu.addSeparator()
            open_in_folder_dress = dress_menu.addAction(self.open_in_folder_LBL)

            menu.addSeparator()

            # CREER SUBMENU AVEC LE NOM DES ITEMS
            
            for item_name in item_list:
                item_menu = menu.addMenu(item_name)
                
                # CREER SUBMENU POUR LES DEPARTEMENTS
                for dep in departmentList:
                    #VARIABLES
                    path = os.path.join(module_path ,
                                        name ,
                                        env.E_PATH ,
                                        dep)
                    editProject = os.listdir( os.path.join(path ,
                                                        env.DATA ))

                    # editImage = os.path.join(path ,
                    #                     env.DATA,
                    #                     editProject[-1])

                    publishImage = os.path.join(module_path ,
                                        name ,
                                        env.P_PATH ,
                                        dep ,
                                        name + env.P_TXT + dep + env.PNG)

                    destination = os.listdir( os.path.join(server,
                                        prod ,
                                        env.SET_PATH ,
                                        name ,
                                        env.E_PATH ,
                                        dep ))
                    #LAST EDIT
                    last_path = os.path.join(server,
                                prod,
                                env.SET_PATH ,
                                name ,
                                env.E_PATH ,
                                dep)
                    
                    destination = os.listdir( last_path )
                    try:
                        destination.remove(env.DATA)
                    except:
                        print ( "No data")
                    # last_edit_file = os.path.join(last_path,  destination[-1])
                    
                    publish_file = os.path.join(server ,
                                prod ,
                                env.SET_PATH ,
                                name ,
                                env.P_PATH ,
                                dep ,
                                name + env.P_TXT + dep + env.ASCII)

                    # DATE LAST EDIT
                    # last_edit_modified = os.path.getmtime(last_edit_file)
                    # year,month,day,hour,minute,second=time.localtime(last_edit_modified)[:-3]
                    # date_last_edit = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                    
                    # # DATE LAST EDIT
                    # publish_modified = os.path.getmtime(publish_file)
                    # year,month,day,hour,minute,second=time.localtime(publish_modified)[:-3]
                    # publish_date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)

                    allEdits = os.listdir(os.path.join( server ,
                                        
                                        prod ,
                                        env.SET_PATH ,
                                        name ,
                                        env.E_PATH ,
                                        dep ))

                    #SubMenu
                    item_dep = item_menu.addMenu(dep)
                    lastEdit = item_dep.addAction(QIcon(), self.last_edit_LBL + "( "" )" )
                    openPublish = item_dep.addAction(QIcon(publishImage), self.open_publish_LBL +  " ( "  " )")
                    
                    Edits = item_dep.addAction("All Edits")

                    
                    #CONNECTIONS
                    lastEdit.triggered.connect(partial(self.openLastEdit_item_UI, item_name, name, dep)) 
                    openPublish.triggered.connect(partial(self.openPublish_item_UI, item_name, name, dep))  
                    Edits.triggered.connect(partial(self.open_in_folder_edits_item_UI, item_name, name, dep))
                    



                #MENU ITEMS GLOBAL
                sculpt = item_dep.addMenu("sculpt")
                sculpt_path = os.listdir(os.path.join(server,
                                            prod,
                                            env.SET_PATH,
                                            name,
                                            env.SCULPT_TYPE))
                for soft in sculpt_path:
                    actions = sculpt.addMenu(soft)
                    lastSculpt = actions.addAction(self.last_edit_LBL)
                    openInFolder_sculpt = actions.addAction(self.open_in_folder_LBL)

                    lastSculpt.triggered.connect(partial(self.openLastSculpt_UI, name, soft))
                    openInFolder_sculpt.triggered.connect(partial(self.open_in_folder_sculpt_char_UI, name, soft)) 


                item_menu.addSeparator()
                
                delete = item_menu.addAction(self.delete_asset_LBL)
                
                #Connections
                delete.triggered.connect(partial(self.delete_item_UI, item_name, name, dep))
                

                
                
                button.setMenu(menu)

            
                
            #NEW ITEM
            menu.addSeparator()
            create_new_item = menu.addAction(self.new_item_LBL)
            openInFolder = menu.addAction(self.open_in_folder_LBL)
            substance = menu.addAction(self.substance_LBL)
            menu.addSeparator()
            delete_module = menu.addAction(self.delete_module_LBL)

            #CONNECTIONS
            last_dress.triggered.connect(partial(self.open_last_dress_item_UI, name))
            publish_dress.triggered.connect(partial(self.open_publish_dress_item_UI, name))
            create_new_item.triggered.connect(partial(self.create_new_item_UI, name))
            delete_module.triggered.connect(partial(self.delete_module_UI, name))
            openInFolder.triggered.connect(partial(self.open_in_folder_module_UI, name)) 
            open_in_folder_dress.triggered.connect(partial(self.open_in_folder_dress_UI, name))
            substance.triggered.connect(partial(self.substance_item_UI, item_name, name)) 
            
        
        

        mayaTab.setLayout(base)
        return mayaTab


    
    '''
    # SHOTS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    def shotTabUI(self):
        server = self.serverName.text()
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        buttons = QHBoxLayout()
        tabs = QTabWidget()

        seqDIR = os.listdir(os.path.join(server,
                                        prod,
                                        env.SHOT_TYPE))

        try:
            seqDIR.remove("Infos.odt")
        except:
            print ( "no info file")
        try:
            seqDIR.remove("_backup")
        except:
            print ("no backup folder")
        try:
            seqDIR.remove("_camera_published")
        except:
            print ("no camera published ")
        try:
            seqDIR.remove("_credits")
        except:
            print ("no credits ")
        try:
            seqDIR.remove("_master_previz")
        except:
            print ("no master previz")
        try:
            seqDIR.remove("shotTest")
        except:
            print ("no shot test")
        try:
            seqDIR.remove("Thumbs.db")
        except:
            print ("no thumbs")
           
        for seq in seqDIR :
            tabs.addTab(self.insideShotTabUI(seq), seq)

        n.addWidget(tabs)
        n.addLayout(buttons)
        # buttons.addWidget(self.new_seq_BTN)
        # buttons.addWidget(self.arrow_01_LBL)
        # buttons.addWidget(self.new_shot_BTN)

        # self.cb = QComboBox()
        # self.cb_shot = QComboBox()

        # for combo_seq in seqDIR :
        #     shot_path = os.listdir(os.path.join(server,
        #                                 prod,
        #                                 env.SHOT_TYPE,
        #                                 combo_seq))

        #     self.cb.addItem(combo_seq)

        #     for combo_shot in shot_path:
        #         self.cb_shot.addItem(combo_shot)

        # self.cb.addItem("NEW SEQ")

        # buttons.addWidget(self.cb)
        # buttons.addWidget(self.cb_shot)

        buttons.addWidget(self.new_seq_LBL)
        buttons.addWidget(self.new_seq_TXT)
        buttons.addWidget(self.new_shot_LBL)
        buttons.addWidget(self.new_shot_TXT)
        buttons.addWidget(self.new_seq_BTN)
        buttons.addWidget(self.new_shot_BTN)

        layout.setLayout(n)
        return layout
  
    def insideShotTabUI(self, seq):
        server = self.serverName.text()
        prod = self.prodName.text()

        shot_tab = QWidget() 
        base = QVBoxLayout()
        group_shot = QGroupBox("SHOTS")
        base.addWidget(group_shot)

        

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = FlowLayout()
        group_shot.setLayout(layoutChar)

        shot_path = os.listdir(os.path.join(server,
                                        prod,
                                        env.SHOT_TYPE,
                                        seq))

        

        #Create Button characters 
        positions = [(i, j) for i in range(3) for j in range(3)]
        for position, name in zip(positions, shot_path):
            if name == '':
                continue
            imageDir = os.path.join(server,
                                    prod,
                                    env.IMAGES_PATH,
                                    env.SHOT_LIB,
                                    name + env.PNG)

            

            button = ImagePushButton(name, path = imageDir)
            button.setMinimumWidth(2050)
            button.setMinimumHeight(90)
            
            path = os.path.join(server,
                                prod)
            layoutChar.addWidget(button)

            #CREER MENU
            menu = QMenu(parent = self)
            menu.addAction( "Name = " + name )

            try:
                nb_frame = os.listdir(os.path.join(server,
                                        prod,
                                        env.SHOT_TYPE,
                                        seq,
                                        name
                                        ))
                nb_frame.remove("camera")
                nb_frame.remove(env.HOUDINI_TYPE)
                nb_frame.remove(env.MAYA_TYPE)
                nb_frame.remove(env.UNREAL_TYPE)

                for frame in nb_frame:
                    menu.addAction( "Frames = " + frame )
                    
            except:
                print ( "no file frame")

            menu.addSeparator()
            #CREATE MENUS
            layout_menu = menu.addMenu("layout")
            anim_menu = menu.addMenu("animation")
            render_menu = menu.addMenu("render")
            cfx_menu = menu.addMenu("cfx")
            vfx_menu = menu.addMenu("vfx")
            compo_menu = menu.addMenu("compositing")
            
            #CREATE SUBMENUS
            layout_last_edit = layout_menu.addAction(QIcon(), self.last_edit_LBL)
            layout_open_in_folder = layout_menu.addAction(QIcon(), self.open_in_folder_LBL)
            anim_last_edit = anim_menu.addAction(QIcon(), self.last_edit_LBL)
            anim_open_in_folder = anim_menu.addAction(QIcon(), self.open_in_folder_LBL)
            render_last_edit = render_menu.addAction(QIcon(), self.last_edit_LBL)
            render_open_in_folder = render_menu.addAction(QIcon(), self.open_in_folder_LBL)
            render_menu.addSeparator()
            anim_menu.addSeparator()
            
            cfx_last_edit = cfx_menu.addAction(QIcon(), self.last_edit_LBL)
            cfx_open_in_folder = cfx_menu.addAction(QIcon(), self.open_in_folder_LBL)
            vfx_last_edit = vfx_menu.addAction(QIcon(), self.last_edit_LBL)
            vfx_open_in_folder = vfx_menu.addAction(QIcon(), self.open_in_folder_LBL)
            compo_last_edit = compo_menu.addAction(QIcon(), self.last_edit_LBL)
            compo_open_in_folder = compo_menu.addAction(QIcon(), self.open_in_folder_LBL)

            #SEND TO NUKE
            try:
                images_render = os.listdir(os.path.join(server,
                                                    prod,
                                                    env.SHOT_TYPE,
                                                    seq,
                                                    name,
                                                    env.MAYA_TYPE,
                                                    "images"))
                for rendu in images_render:
                    render_images_menu = render_menu.addMenu(QIcon(), rendu)
                    render_send_to_nuke = render_images_menu.addAction(QIcon(), "Send Images to Nuke")
                    render_send_to_nuke.triggered.connect(partial(self.render_send_to_nuke_UI, name, seq, rendu))
            except:
                print ( "no images")

            # SEND TO DELIVERY
            try:
                movies = os.listdir(os.path.join(server,
                                                    prod,
                                                    env.SHOT_TYPE,
                                                    seq,
                                                    name,
                                                    env.MAYA_TYPE,
                                                    "movies"))
                for playblast in movies:
                    movies_menu = anim_menu.addMenu(QIcon(), playblast)
                    playblast_to_delivery = movies_menu.addAction(QIcon(), "Send Playblast To Delivery")
                    playblast_to_delivery.triggered.connect(partial(self.anim_send_to_delivery_UI, name, seq, playblast))
            except:
                print ( "no images")



            #CONNECTIONS
            layout_last_edit.triggered.connect(partial(self.layout_open_last_edit_UI, name, seq))
            layout_open_in_folder.triggered.connect(partial(self.layout_open_in_folder_UI, name, seq))
            anim_last_edit.triggered.connect(partial(self.anim_open_last_edit_UI, name, seq))
            anim_open_in_folder.triggered.connect(partial(self.anim_open_in_folder_UI, name, seq))
            render_last_edit.triggered.connect(partial(self.render_open_last_edit_UI, name, seq))
            render_open_in_folder.triggered.connect(partial(self.render_open_in_folder_UI, name, seq))
            cfx_last_edit.triggered.connect(partial(self.cfx_open_last_edit_UI, name, seq))
            cfx_open_in_folder.triggered.connect(partial(self.cfx_open_in_folder_UI, name, seq))
            vfx_last_edit.triggered.connect(partial(self.vfx_open_last_edit_UI, name, seq))
            vfx_open_in_folder.triggered.connect(partial(self.vfx_open_in_folder_UI, name, seq))
            compo_last_edit.triggered.connect(partial(self.compo_open_last_edit_UI, name, seq))
            compo_open_in_folder.triggered.connect(partial(self.compo_open_in_folder_UI, name, seq))
            

            button.setMenu(menu)
            

        shot_tab.setLayout(base)
        return shot_tab



    '''
    # EDITING ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    # def editTabUI(self):
    #     server = self.serverName.text()
    #     prod = self.prodName.text()
    #     layout = QWidget()
    #     n = QVBoxLayout()
    #     n.addWidget(self.edit_Label)
    #     tabs = QTabWidget()

    #     n.addWidget(tabs)
    #     layout.setLayout(n)
    #     return layout
    
    '''  
    ## CONNECTIONS UI ## ------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    #CHARACTER
    def createNewChara_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        server = self.serverName.text()
        if not server:
            return
        if not prod:
            return
        if not assetName:
            return
        fn.newCharFN( server = server, prod = prod, assetName = assetName)
        self.reload()

    def openLastSculpt_UI(self, name, soft):
        prod = self.prodName.text()
        server = self.serverName.text()

        if not server:
            return
        fn.openLastSculpt_FN (name, soft, server, prod = prod)
    
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
        fn.openPublish_FN (  name, dep, server, prod = prod)

    def deleteAsset_UI(self, name):
        
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()

        fn.deleteAsset_FN(  name, server,  prod = prod)
        self.reload()

    def rename_char_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        assetName = self.assetName.text()
        if not server:
            return
        fn.rename_FN (   name, server = server, prod = prod, assetName = assetName )
        self.reload()

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

    def open_in_folder_sculpt_char_UI(self, name, soft):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fn.open_in_folder_sculpt_FN(  name, soft, server, prod = prod)

    def open_in_folder_edits_char_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fn.open_in_folder_edits_FN (  name, dep, server, prod)

    def substance_char_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fn.substance_FN (  name, server, prod)
        


    # PROPS
    def createNewProp_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        server = self.serverName.text()
        if not prod:
            return
        if not assetName:
            return
        prop.newProp_FN(server, prod = prod, assetName = assetName)
        self.reload()

    def openLastEdit_prop_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.openLastEdit_FN (  name, dep, server, prod = prod)    

    def openPublish_prop_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.openPublish_FN (  server, name, dep, prod = prod)

    def openLastSculpt_prop_UI(self, name, soft):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.openLastSculpt_FN (name, soft, server, prod = prod)

    def openInFolder_prop_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        prop.openInFolder_FN(  name, server, prod = prod)

    def open_in_folder_sculpt_prop_UI(self, name, soft):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.open_in_folder_sculpt_FN(  name, soft, server, prod = prod)

    def open_in_folder_edits_prop_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.open_in_folder_edits_FN (  name, dep, server, prod)

    def deleteAsset_prop_UI(self, name):
        
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()

        prop.deleteAsset_FN(  name, server,  prod = prod)
        self.reload()

    def substance_prop_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        prop.substance_FN (  name, server, prod)

    # ITEMS
    def create_new_module_UI(self):
        prod = self.prodName.text()
        server = self.serverName.text()
        assetName = self.assetName.text()
        if not server:
            return
        item.create_new_module_FN (  server = server, prod = prod, assetName = assetName )
        self.reload()

    def create_new_item_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        assetName = self.assetName.text()
        if not server:
            return
        item.create_new_item_FN ( name, server = server, prod = prod, assetName = assetName)
        self.reload()

    def openLastEdit_item_UI(self, item_name, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        print ( prod )
        print ( server )
        if not server:
            return
        item.openLastEdit_FN (  item_name, name, dep, server, prod = prod)

    def openPublish_item_UI(self, item_name, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        item.openPublish_FN (  item_name, name, dep, server, prod = prod)

    def open_last_dress_item_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        print ( prod )
        print ( server )
        if not server:
            return
        item.open_last_dress_FN (  name, server, prod = prod)

    def open_publish_dress_item_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        print ( prod )
        print ( server )
        if not server:
            return
        item.open_publish_dress_FN (  name, server, prod = prod)

    def openLastSculpt_item_UI(self, name, soft, setName, modName):
        prod = self.prodName.text()
        server = self.serverName.text()

        if not server:
            return
        item.openLastSculpt_FN (name, soft, server, setName, modName, prod = prod)

    def open_in_folder_sculpt_item_UI(self, name, soft, setName, modName):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        item.open_in_folder_sculpt_FN(  name, soft, server, setName, modName, prod = prod)
   
    def open_in_folder_edits_item_UI(self, item_name, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        item.open_in_folder_edits_FN (  item_name, name, dep, server, prod)
    
    def open_in_folder_module_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        item.open_in_folder_module_FN(  name, server, prod = prod)

    def open_in_folder_dress_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        folder = self.serverName.text()
        if not server:
            return
        item.open_in_folder_dress_FN(  name, server, prod = prod)

    def delete_item_UI(self, item_name, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        item.delete_item_FN(  item_name, name, dep, server, prod)
        self.reload()
    
    def delete_module_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        item.delete_module_FN (  name, server, prod)
        self.reload()

    def substance_item_UI(self, item_name, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        item.substance_FN (  item_name, name, server, prod)

    # FX

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

    def open_last_FX_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fx.open_last_FX_FN (name, server, prod = prod)

    def open_dep_FX_UI(self, name, dep):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fx.open_in_folder_dep_FX_FN (  name, dep, server, prod)

    def open_all_FX_UI(self, name, edit):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fx.open_all_FX_FN (  name, edit, server, prod)
        print ( edit )

    def open_in_folder_edits_FX_UI(self, name):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fx.open_in_folder_edits_FN (  name, server, prod)

    def delete_FX_UI(self, name):
        
        prod = self.prodName.text()
        server = self.serverName.text()

        fx.delete_FX_FN(  name, server,  prod = prod)
        self.reload()

    #  SHOTS

    def layout_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.layout_open_last_edit_FN (  name, seq, server, prod = prod)    

    def layout_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.layout_open_in_folder_FN (  name, seq, server, prod = prod) 

    def anim_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.anim_open_last_edit_FN (  name, seq, server, prod = prod)    

    def anim_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.anim_open_in_folder_FN (  name, seq, server, prod = prod) 

    def anim_send_to_delivery_UI(self, name, seq, playblast):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.anim_send_to_delivery_FN (  name, seq, playblast, server, prod = prod)

    def render_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.render_open_last_edit_FN (  name, seq, server, prod = prod)    

    def render_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.render_open_in_folder_FN (  name, seq, server, prod = prod) 

    def render_send_to_nuke_UI(self, name, seq, rendu):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.render_send_to_nuke_FN (  name, seq, rendu, server, prod = prod)

    def cfx_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.cfx_open_last_edit_FN (  name, seq, server, prod = prod)    

    def cfx_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.cfx_open_in_folder_FN (  name, seq, server, prod = prod) 

    def vfx_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.vfx_open_last_edit_FN (  name, seq, server, prod = prod)    

    def vfx_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.vfx_open_in_folder_FN (  name, seq, server, prod = prod) 

    def compo_open_last_edit_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.compo_open_last_edit_FN (  name, seq, server, prod = prod)    

    def compo_open_in_folder_UI(self, name, seq):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        shot.compo_open_in_folder_FN (  name, seq, server, prod = prod) 

    def create_new_seq_UI(self):
        prod = self.prodName.text()
        server = self.serverName.text()
        nb_seq = self.new_seq_TXT.text()
        if not server:
            return
        shot.create_new_seq_FN ( nb_seq, server, prod = prod)  
        self.reload() 

    def create_new_shot_UI(self):
        prod = self.prodName.text()
        server = self.serverName.text()
        prefix = self.prefixName.text()
        nb_seq = self.new_seq_TXT.text()
        nb_shot = self.new_shot_TXT.text()
        if not server:
            return
        shot.create_new_shot_FN ( nb_seq, nb_shot, prefix, server, prod = prod)   
        self.reload()



    ## UI CUSTOMIZE ##

    def openTab(self, tab01_Lay_L, up_tab01_Layout_L):
        tab01_Lay_L.setLayout(up_tab01_Layout_L)

    def reload(self):
        
        self.close() 
        MainWindow()
        
    def setProd_FN(self):
        server = self.serverName.text()
        prod = self.prodName.text()
        prefix = self.prefixName.text()
        tmp_server = self.tmp_server_Name.text()
        
        listOfStr = ["server",
                    "prod",
                    "prefix",
                    "tmp_server",
                    "tmp_package",
                    "tmp_appli",
                    "tmp_version",
                    "tmp_resources",
                    "tmp_prod"]
        listOfTxt = [server,
                    prod,
                    prefix,
                    tmp_server,
                    "packages",
                    "antares",
                    env.VERSION,
                    "resources",
                    "template_pipeline_film"]

        zipObj = zip(listOfStr, listOfTxt)
        new_dico = dict(zipObj)
        base_file = open("prefs.json", "w")
        json.dump(new_dico, base_file)
        base_file.close()

        self.reload()

    def open_library_UI(self):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fn.open_library_FN(  server, prod)

    def open_resources_UI(self):
        prod = self.prodName.text()
        server = self.serverName.text()
        if not server:
            return
        fn.open_resources_FN(  server, prod)

    def open_user_picture_UI(self):
        fn.open_user_picture_FN()

    def open_prefs_UI(self):
        server = self.serverName.text()
        fn.open_prefs_FN(server)

    def lightTheme_FN(self):
        

        application = QApplication(sys.argv)

        application.setStyle('Fusion')

        file = QFile("./darkTheme.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        application.setStyleSheet(stream.readAll())


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
    
    # file = QFile("./greenTheme.qss")
    # file = QFile("./darkTheme.qss")
    file = QFile("./blueTheme.qss")
    # file = QFile("./pinkTheme.qss")

    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    application.setStyleSheet(stream.readAll())

    window = MainWindow()
    # window.setupData()

    sys.exit(application.exec_())


else:
    window = None