import sys, os, time, fn, env, subprocess, Qt, psutil
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QPixmap
from functools import partial

class MainWindow(QWidget) :

    def __init__(self) :
        super(MainWindow,self).__init__()
        self.title = "ANTARES_v0.2.002"
        self.attr = "QPushButton {background-color: #18537d; color: white;}"
        self.grpBgc = u"background-color: rgb(10, 40, 50);"
        self.resize(858, 540)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        
        self.createWidget()
        self.createLayout()

    def createWidget(self):
        self.prodTitle = QLabel ( env.CURRENT_PROD)
        #Set production
        self.serverName = QLineEdit(env.SERVER)
        self.prodName = QLineEdit(env.CURRENT_PROD)
        self.assetDirName = QLineEdit(env.ASSET_DIR)
        self.shotDirName = QLineEdit(env.SHOT_DIR)
        self.prodLabel = QLabel ( "Enter Server and Production Name")
        self.setProd = QPushButton("Set Production")
        #NEW ASSETS
        self.newCharBTN = QPushButton("NEW CHARACTER")
        self.newPropBTN = QPushButton("NEW PROP (to do)")
        self.item = QPushButton("NEW ITEM (to do)")
        self.lib = QPushButton("NEW LIBRARY (to do)")
        self.newHip = QPushButton("NEW HIP (to do)")
        self.incrementSave = QPushButton("INCREMENT AND SAVE")
        #RENAME ASSET
        self.assetName = QLineEdit("Antares")
        self.oldName = QLineEdit("Antares")
        self.newName = QLineEdit("NewName")
        self.newNameLabel = QLabel ( "New Name")
        self.oldNameLabel = QLabel ( "Old Name")
        self.renameButton = QPushButton("Rename Asset")
        #CONNECTIONS
        self.newCharBTN.clicked.connect(self.createNewChara_UI)
        self.newPropBTN.clicked.connect(self.createNewProp_UI)
        self.renameButton.clicked.connect(self.renameAsset_UI)

    def createLayout(self):
        # LAYOUT HIERARCHY
        outerLayout = QGridLayout()
        topLayout = QFormLayout()
        Layout_L = QVBoxLayout()
        tabsLayout_L = QTabWidget()
        tab01_Lay_L = QWidget()
        up_tab01_Layout_L = QVBoxLayout()
        mid_tab01_Layout_L = QGridLayout()
        dwn_tab01_Layout_L = QHBoxLayout()
        Layout_R = QVBoxLayout()
        tabs_Lay_R = QTabWidget()
        #ADD WIDGETS
        topLayout.addWidget(self.prodTitle)
        for widget in [self.prodLabel, self.serverName, self.prodName, self.setProd, self.assetName]:
            up_tab01_Layout_L.addWidget(widget)
        for widget in [self.oldNameLabel, self.oldName, self.newNameLabel, self.newName]:
            mid_tab01_Layout_L.addWidget( widget )
        dwn_tab01_Layout_L.addWidget(self.renameButton)
        Layout_L.addWidget(tabsLayout_L)
        Layout_R.addWidget(tabs_Lay_R)
        tabsLayout_L.addTab(tab01_Lay_L, "HOME")
        tabs_Lay_R.addTab(self.assetTabUI(), "ASSETS")
        tabs_Lay_R.addTab(self.shotTabUI(), "SHOTS")
        #ADD LAYOUTS
        up_tab01_Layout_L.addLayout(mid_tab01_Layout_L)
        up_tab01_Layout_L.addLayout(dwn_tab01_Layout_L)
        outerLayout.addLayout(topLayout, 1, 0, 1, 2)
        outerLayout.addLayout(Layout_L, 2, 0)
        outerLayout.addLayout(Layout_R, 2, 1)
        tab01_Lay_L.setLayout(up_tab01_Layout_L)
        #SET CUSTOM
        outerLayout.setColumnStretch(1,1)
        up_tab01_Layout_L.addStretch(1)
        up_tab01_Layout_L.setSpacing(5)
        tabsLayout_L.setTabPosition(tabsLayout_L.West)
        tabsLayout_L.setMovable(True)

        self.setLayout(outerLayout)
        self.show()
    
    #############

    # ASSETS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def assetTabUI(self):
        outLayout = QWidget()
        globalLayout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.mayaTab_UI(), "MAYA")
        globalLayout.addWidget(tabs)
        outLayout.setLayout(globalLayout)
        return outLayout

    def mayaTab_UI(self):
        prod = self.prodName.text()
        #CHECK PID
        PROCNAME = "maya.exe"
        for pid in psutil.process_iter(['pid', 'name', 'username']):
            if pid.name() == PROCNAME:
                result = str(pid.info)

        mayaTab = QWidget() 
        base = QGridLayout()
        groupChara = QGroupBox("CHARACTERS")
        groupProp = QGroupBox("PROPS")
        groupSet = QGroupBox("SETS")
        base.addWidget(self.incrementSave)
        base.addWidget(groupChara)
        base.addWidget(groupProp)
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
            
            path = os.path.join(env.SERVER, prod)
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
                allE_DIRs = os.listdir(os.path.join( env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.E_DIR , dep ))

                #SubMenu
                items = menu.addMenu(dep)
                lastEdit = items.addAction(QIcon(E_DIRImage), "Open Last Edit (" + date + ")" )
                openPublish = items.addAction(QIcon(publishImage),"Open Publish (" + date + ")")
                items.addAction("Open In Folder (To Do)")
                E_DIRs = items.addMenu("All Edits")
                for i in allE_DIRs:
                    E_DIRs.addAction(i + " (" + date + ") (To Do)")  
                refPublish = items.addMenu("Reference Publish")
                for pid in ["Reference Publish"]:
                    # refPublish.addAction(result)
                    refPublish.addAction("NEW MAYA")
                #CONNECTIONS
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep)) 
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))  
                refPublish.triggered.connect(partial(self.refPublish_UI, name, dep)) 

            #MENU ITEMS GLOBAL
            menu.addAction("Duplicate Asset (To Do)")
            delete = menu.addAction("Delete Asset")
            menu.addAction("Create New Task (To Do)")
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_UI, name, assetcharacter))

            button.setMenu(menu)
        #New Chara Button
        self.newCharBTN.setFixedSize(100, 100)
        layoutChar.addWidget(self.newCharBTN)

        mayaTab.setLayout(base)
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

    ## CONNECTIONS UI ##

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
        here = os.path.realpath(os.path.dirname(__file__))
        script_path = os.path.join(here , 'refPublish.py').replace("\\", "/")
        '''
        # cmd=["C:/Program Files/Autodesk/Maya2020/bin/maya.exe", "-c", 'python("execfile(\'%s\')")' %script_path]
        cmd=["-c", 'python("execfile(\'%s\')")' %script_path]
        print (cmd)
           
        subprocess.Popen(
                        cmd
                        # env={'PYTHONPATH':""}
                        #creationflags=subprocess.CREATE_NEW_CONSOLE,
                        )
        '''

    def renameAsset_UI(self):
        prod = self.prodName.text()
        oldName = self.oldName.text()
        newName = self.newName.text()
        print ( newName )
        fn.renameAsset_FN (prod = prod, oldName = oldName, newName = newName)

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

    application.setStyle('Fusion')

    window = MainWindow()

    sys.exit(application.exec_())
else:
    window = None