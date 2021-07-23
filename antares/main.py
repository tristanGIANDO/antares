import sys, os, shutil, time, datetime
import Qt
from Qt.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from Qt.QtCore import *
from Qt.QtGui import * #QPixmap
from functools import partial
import fn, env

class MainWindow(QWidget) :

    def __init__(self) :
        #super().__init__()
        self.title = "ANTARES_v0.1.011"
        self.attr = "QPushButton {background-color: #18537d; color: white;}"
        
        self.createWidget()
        self.createLayout()

    ####################
    ## USER INTERFACE ##
    ####################

    def createWidget(self):
        self.prodTitle = QLabel ( "PROD NAME")
        #Set production
        self.serverName = QLineEdit(os.path.join("C:\\", "Users", "Windows", "Desktop"))
        self.prodName = QLineEdit("suchomimus")
        self.prodLabel = QLabel ( "Enter Server and Production Name")
        #self.prodLabel.setStyleSheet("color: white")
        self.setProd = QPushButton("Set Production")
        #Create new ASSET_DIR
        #MAYA
        self.assetNameLabel = QLabel ( "Enter Asset Name")
        self.assetName = QLineEdit("Antares")
        self.newCharBTN = QPushButton("NEW CHARACTER")
        self.newCharBTN.clicked.connect(self.createNewChara_UI)
        self.newPropBTN = QPushButton("NEW PROP (to do)")
        self.newPropBTN.clicked.connect(self.createNewProp_UI)
        self.item = QPushButton("NEW ITEM (to do)")
        self.lib = QPushButton("NEW LIBRARY (to do)")
        #HOUDINI
        self.assetHouLabel = QLabel ( "Enter Asset Name")
        self.assetHou = QLineEdit()
        self.newHip = QPushButton("NEW HIP (to do)")
        self.newHip.setFixedWidth(200)

    def createLayout(self):
        #window
        self.resize(858, 540)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        #self.setStyleSheet(u"background-color: rgb(10, 40, 50);")
        # Layout principal
        outerLayout = QGridLayout()
        outerLayout.setColumnStretch(1,1)
        #Layout du haut pour titres etc
        topLayout = QFormLayout()
        topLayout.addWidget(self.prodTitle)
        #CREATE LEFT MENU
        leftLayout = QVBoxLayout()
        sideTabs = QTabWidget()
        sideTabs.setTabPosition(sideTabs.West)
        sideTabs.setMovable(True)
        #HOME LAYOUT a l interieur du left layout
        layout = QWidget()
        n = QVBoxLayout()
        n.setSpacing(5)
        n.addWidget(self.prodLabel)
        n.addWidget(self.serverName)
        n.addWidget(self.prodName)
        n.addWidget(self.setProd)
        layout.setLayout(n)
        n.addStretch(1)
        #Ajouter les layouts dans des tabs 
        sideTabs.addTab(layout, "HOME")
        sideTabs.addTab(self.assetTabButtons(), "NEW assetS")
        sideTabs.addTab(self.SHOTTabButtons(), "NEW SHOTS")
        leftLayout.addWidget(sideTabs)
        #Gros content browser layout a droite
        rightLayout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.assetTabUI(), "ASSETS")
        tabs.addTab(self.shotTabUI(), "SHOTS")
        rightLayout.addWidget(tabs)
        #ajout des layouts au layout global
        outerLayout.addLayout(topLayout, 1, 0, 1, 2)
        outerLayout.addLayout(leftLayout, 2, 0)
        outerLayout.addLayout(rightLayout, 2, 1)

        self.setLayout(outerLayout)
        self.show()
    
    #############
    ## LAYOUTS ##
    #############
    # Bientot osolete
    def assetTabButtons(self):
        layout = QWidget()
        out = QVBoxLayout()
        #CURRENT_SOFT
        mayaGrp = QGroupBox("IN CURRENT_SOFT")
        mayaIn = QVBoxLayout()
        mayaGrp.setLayout(mayaIn)
        #mayaGrp.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        mayaIn.addWidget(self.assetNameLabel)
        mayaIn.addWidget(self.assetName)
        mayaIn.addWidget(self.item)
        mayaIn.addWidget(self.lib)
        mayaIn.addStretch(1)
        #HOUDINI
        houGrp = QGroupBox("IN HOUDINI")
        houIn = QVBoxLayout()
        houGrp.setLayout(houIn)
        #houGrp.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        houIn.addWidget(self.assetHouLabel)
        houIn.addWidget(self.assetHou)
        houIn.addWidget(self.newHip)
        #ADD GROUPS
        out.addWidget(mayaGrp)
        out.addWidget(houGrp)
        out.setSpacing(20)
        layout.setLayout(out)
        return layout

    def SHOTTabButtons(self):
        layout = QWidget()
        out = QVBoxLayout()
        #CURRENT_SOFT
        mayaGrp = QGroupBox("IN CURRENT_SOFT")
        mayaIn = QVBoxLayout()
        mayaGrp.setLayout(mayaIn)
        #mayaGrp.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        mayaIn.addStretch(1)
        #HOUDINI
        houGrp = QGroupBox("IN HOUDINI")
        houIn = QVBoxLayout()
        houGrp.setLayout(houIn)
        #houGrp.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        #ADD GROUPS
        out.addWidget(mayaGrp)
        out.addWidget(houGrp)
        out.setSpacing(20)
        layout.setLayout(out)
        return layout

    # ASSETS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def assetTabUI(self):
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.mayaTabUI(), "MAYA")
        tabs.addTab(self.houdiniTabUI(), "HOUDINI")
        tabs.addTab(self.sculptTabUI(), "SCULPT")
        tabs.addTab(self.paintTabUI(), "PAINT 3D")
        n.addWidget(tabs)
        layout.setLayout(n)
        return layout

    def mayaTabUI(self):
        prod = self.prodName.text()
        print ("Current production = " + prod)
        mayaTab = QWidget() 
        base = QGridLayout()
        #Create character frame
        groupChara = QGroupBox("CHARACTERS")
        #groupChara.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        base.addWidget(groupChara)
        #Create PROPS frame
        groupProp = QGroupBox("PROPS")
        #groupProps.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        base.addWidget(groupProp)
        #Create SET frame
        groupSet = QGroupBox("SETS")
        #groupSet.setStyleSheet(u"background-color: rgb(50, 50, 50); color : white;")
        base.addWidget(groupSet)

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = QGridLayout()
        groupChara.setLayout(layoutChar)
        layoutChar.setRowStretch(1,1)
        #Variable
        characterPath = os.path.join(env.SERVER, prod, env.ASSET_DIR, env.TYPE_CHAR)
        assetcharacter = os.listdir( characterPath )
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            
            if name == '':
                continue
            button = QPushButton(name)
            button.setFixedSize(100, 100)
            button.setStyleSheet("QPushButton{border-image: url(C:/Users/Windows/Desktop/suchomimus/11_library/Images/character/" + name + ".png);}")
            layoutChar.addWidget(button, *position)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(characterPath , name , env.E_DIR))
            #CREER MENU
            menu = QMenu()
            for dep in departmentList:
                #VARIABLES
                path = os.path.join(characterPath , name , env.E_DIR , dep)
                E_DIRProject = os.listdir( os.path.join(path , "data" ))
                E_DIRImage = os.path.join(path , "data", E_DIRProject[-1])
                publishImage = os.path.join(characterPath , name , env.P_DIR , dep , name , "_P_" , dep , ".png")
                destination = os.listdir( os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.E_DIR , dep ))
                file = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.E_DIR ,dep , destination[-1])
                modified = os.path.getmtime(file)
                year,month,day,hour,minute,second=time.localtime(modified)[:-3]
                date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                #SubMenu
                items = menu.addMenu(dep)
                #lastEdit
                lastEdit = items.addAction(QIcon(E_DIRImage), "Open Last Edit (" + date + ")" )
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep))
                #publish
                openPublish = items.addAction(QIcon(publishImage),"Open Publish (" + date + ")")
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))
                items.addAction("Open In Folder (To Do)")
                #Recuperer tous les E_DIRs
                E_DIRs = items.addMenu("All Edits")
                allE_DIRs = os.listdir(os.path.join( env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.E_DIR , dep ))
                for i in allE_DIRs:
                    E_DIRs.addAction(i + " (" + date + ") (To Do)")       
            a = menu.addAction("Rename Asset (To Do)")
            a.triggered.connect(renameWindow)
            menu.addAction("Duplicate Asset (To Do)")
            delete = menu.addAction("Delete Asset")
            delete.triggered.connect(partial(self.deleteAsset_UI, name))
            menu.addAction("Create New Task (To Do)")

            button.setMenu(menu)
        self.newCharBTN.setFixedSize(100, 100)
        layoutChar.addWidget(self.newCharBTN)

        #SET PROPS GROUP --------------------------------------------------------------------------------------------------------------------------------------------------------
        layoutProp = QGridLayout()
        groupProp.setLayout(layoutProp)
        layoutProp.setRowStretch(1,1)
        #Variable
        propPath = os.path.join(env.SERVER, prod, env.ASSET_DIR, env.TYPE_PROP)
        assetProp = os.listdir( propPath )
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetProp):
            
            if name == '':
                continue
            button = QPushButton(name)
            button.setFixedSize(100, 100)
            button.setStyleSheet("QPushButton{border-image: url(C:/Users/Windows/Desktop/suchomimus/11_library/Images/character/" + name + ".png);}")
            layoutProp.addWidget(button, *position)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(propPath , name , env.E_DIR))
            #CREER MENU
            menu = QMenu()
            for dep in departmentList:
                #VARIABLES
                path = os.path.join(propPath , name , env.E_DIR , dep)
                editProject = os.listdir( os.path.join(path , "data" ))
                editImage = os.path.join(path , "data", editProject[-1])
                publishImage = os.path.join(propPath , name , env.P_DIR , dep , name , "_P_" , dep , ".png")
                destination = os.listdir( os.path.join(env.SERVER , prod , env.TYPE_PROP_PATH , name , env.E_DIR , dep ))
                file = os.path.join(env.SERVER , prod , env.TYPE_PROP_PATH , name , env.E_DIR ,dep , destination[-1])
                modified = os.path.getmtime(file)
                year,month,day,hour,minute,second=time.localtime(modified)[:-3]
                date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                #SubMenu
                items = menu.addMenu(dep)
                #lastEdit
                lastEdit = items.addAction(QIcon(editImage), "Open Last Edit (" + date + ")" )
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep))
                #publish
                openPublish = items.addAction(QIcon(publishImage),"Open Publish (" + date + ")")
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))
                items.addAction("Open In Folder (To Do)")
                #Recuperer tous les E_DIRs
                edits = items.addMenu("All Edits")
                allEdits = os.listdir(os.path.join( env.SERVER , prod , env.TYPE_PROP_PATH , name , env.E_DIR , dep ))
                for i in allEdits:
                    edits.addAction(i + " (" + date + ") (To Do)")       
            a = menu.addAction("Rename Asset (To Do)")
            a.triggered.connect(renameWindow)
            menu.addAction("Duplicate Asset (To Do)")
            delete = menu.addAction("Delete Asset")
            delete.triggered.connect(partial(self.deleteAsset_UI, name))
            menu.addAction("Create New Task (To Do)")

            button.setMenu(menu)
        self.newPropBTN.setFixedSize(100, 100)
        layoutProp.addWidget(self.newPropBTN)

        mayaTab.setLayout(base)

        return mayaTab

    def houdiniTabUI(self):
        houdiniTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("character"))
        layout.addWidget(QPushButton("FX"))
        houdiniTab.setLayout(layout)
        return houdiniTab

    def sculptTabUI(self):
        mayaTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("character"))
        mayaTab.setLayout(layout)
        return mayaTab

    def paintTabUI(self):
        mayaTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("character"))
        mayaTab.setLayout(layout)
        return mayaTab

    # SHOTS -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def shotTabUI(self):
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        seqDIR = os.listdir(os.path.join(env.SERVER, prod, env.SHOT_DIR))
        for seq in seqDIR :
            tabs.addTab(self.insideShotTabUI(), seq)
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

    ####################
    ## CONNECTIONS UI ##
    ####################
    
    def createNewChara_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        if not prod:
            return
        if not assetName:
            return
        fn.newCharFN(prod = prod, assetName = assetName)

    def createNewProp_UI(self):
        prod = self.prodName.text()
        assetName = self.assetName.text()
        if not prod:
            return
        if not assetName:
            return
        fn.newPropFN(prod = prod, assetName = assetName)

    def openLastEdit_UI(self, name, dep):
        prod = self.prodName.text()
        fn.openLastEdit_FN (name, dep, prod = prod)
    
    def openPublish_UI(self, name, dep):
        prod = self.prodName.text()
        fn.openPublish_FN (name, dep, prod = prod)

    def deleteAsset_UI(self, name):
        prod = self.prodName.text()
        fn.deleteAsset_FN(name, prod = prod)

# GROS WIP --------------------------------------------------------------------------------------------------------------------------------------------------------------------
class renameWindow(QWidget) :

    def __init__(self) :

        self.title = "Rename Asset"
        super().__init__()
        self.createWidget()
        self.createLayout()

    def createWidget(self):
        self.prodTitle = QLabel ( "PROD NAME")

    def createLayout(self):
        #window
        self.resize(300, 200)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        # Layout principal
        outerLayout = QGridLayout()
        outerLayout.setColumnStretch(1,1)
        outerLayout.addWidget(self.prodTitle)
        self.setLayout(outerLayout)
        self.show()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(application.exec_())
else:
    window = None