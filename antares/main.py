import sys, os, shutil, time, datetime

import Qt
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QPixmap
from functools import partial
import fn, env, subprocess

class MainWindow(QWidget) :

    def __init__(self) :
        super(MainWindow,self).__init__()
        self.title = "ANTARES_v0.1.011"
        self.attr = "QPushButton {background-color: #18537d; color: white;}"
        self.grpBgc = u"background-color: rgb(50, 50, 50); color : white;"
        
        
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
        
        base.addWidget(groupChara)
        #Create PROPS frame
        groupProp = QGroupBox("PROPS")
        base.addWidget(groupProp)
        #Create SET frame
        groupSet = QGroupBox("SETS")
        base.addWidget(groupSet)

        #SET CHARACTER GROUP ---------------------------------------------------------------------------------------------------------------------------------------------------
        layoutChar = FlowLayout()
        groupChara.setLayout(layoutChar)
        #Variable
        characterPath = os.path.join(env.SERVER, prod, env.ASSET_DIR, env.TYPE_CHAR)
        assetcharacter = os.listdir( characterPath )
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            
            if name == '':
                continue
            imageDir = os.path.join(env.SERVER, prod, "11_library","Images", "Character", name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            button.setStyleSheet("QPushButton{text-align : bottom;}")
            path = os.path.join(env.SERVER, prod)
            #button.setStyleSheet("QPushButton{border-image: url(" + path + "/11_library/Images/character/" + name + ".png);}")
            layoutChar.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(characterPath , name , env.E_DIR))
            #CREER MENU
            menu = QMenu(parent = self)
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
                #Recuperer tous les edits
                E_DIRs = items.addMenu("All Edits")
                allE_DIRs = os.listdir(os.path.join( env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.E_DIR , dep ))
                for i in allE_DIRs:
                    E_DIRs.addAction(i + " (" + date + ") (To Do)")  
                #reference
                refPublish = items.addAction("Reference Publish")
                refPublish.triggered.connect(partial(self.refPublish_UI, name, dep))     
            a = menu.addAction("Rename Asset (BUG)")
            a.triggered.connect(partial(self.showRenameWindow, name, prod))
            menu.addAction("Duplicate Asset (To Do)")
            delete = menu.addAction("Delete Asset")
            delete.triggered.connect(partial(self.deleteAsset_UI, name, assetcharacter))
            menu.addAction("Create New Task (To Do)")

            button.setMenu(menu)
        self.newCharBTN.setFixedSize(100, 100)
        layoutChar.addWidget(self.newCharBTN)

       

        mayaTab.setLayout(base)

        return mayaTab

    def showRenameWindow(self, name, prod):
        renameUI = RenameWindow(self)
        renameUI.show()

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

    def deleteAsset_UI(self, name, assetcharacter):
        prod = self.prodName.text()
        fn.deleteAsset_FN(name, assetcharacter, prod = prod)

    def refPublish_UI(self, name, dep):
        prod = self.prodName.text()
        project = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.P_DIR , dep , name + "_P_" + dep + ".ma")
        here = os.path.realpath(os.path.dirname(__file__))
        script_path = os.path.join(here , 'refPublish.py').replace("\\", "/")
        PYTHON_EXE=sys.executable

        cmd=["C:/Program Files/Autodesk/Maya2020/bin/maya.exe", "-c", 'python("execfile(\'%s\')")' %script_path]
        print (cmd)
           
        subprocess.Popen(
                        cmd
                        # env={'PYTHONPATH':""}
                        #creationflags=subprocess.CREATE_NEW_CONSOLE,
                        )
            

class RenameWindow(QWidget) :

    def __init__(self, parent) :
        

        self.title = "ASSET_RENAMER"
        super(RenameWindow, self).__init__(parent)
        self.resize(300, 60)
        self.move(100, 100)
        self.setWindowFlags(self.windowFlags() | Qt.Window) 
        self.createWidget()
        self.createLayout()

        # prod = self.prodName.text()
        

    def createWidget(self):
        self.newName = QLineEdit("NewName")
        self.newNameLabel = QLabel ( "New Name")
        self.renameButton = QPushButton("OK")
        self.renameButton.clicked.connect(self.renameAsset_UI)
        self.cancelButton = QPushButton("Cancel")

    def createLayout(self):
        #window
        
        self.setWindowTitle(self.title)
        # Layout principal
        mainLayout = QVBoxLayout(self)
        layoutUp = QGridLayout()
        layoutUp.addWidget(self.newNameLabel, 0,0)
        layoutUp.addWidget(self.newName, 0,1)
        layoutDwn = QHBoxLayout()
        layoutDwn.addWidget(self.renameButton)
        layoutDwn.addWidget(self.cancelButton)
        mainLayout.addLayout(layoutUp)
        mainLayout.addLayout(layoutDwn)

    def renameAsset_UI(self):
        newName = self.newName.text()
        # print (prod)
        print ( newName )
        fn.renameAsset_FN (newName = newName)

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
        painter.drawPixmap(QRect(QPoint(0,0),QSize(100,80)), self.pixmap)        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(application.exec_())
else:
    window = None