import sys, os, time, fn, env, subprocess #psutil
'''
from Qt.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from Qt.QtCore import *
from Qt.QtGui import * #QPixmap
from Qt import QtCore, QtGui, QtWidgets
'''
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial


class MainWindow(QWidget) :

    def __init__(self) :
        super(MainWindow,self).__init__()
        self.title = "ANTARES_v0.2.0"
        self.attr = "QPushButton {background-color: #18537d; color: white;}"
        self.grpBgc = u"background-color: rgb(10, 40, 50);"
        self.icon = os.path.join(env.RESOURCES, "icons", "_UI", "logo.png")
        self.resize(850, 500)
        self.move(100, 100)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        
        self.createWidget()
        self.createLayout()


    def createWidget(self):
        self.prodTitle = QLabel ( env.TMP_PROD)
        self.userLabel = QLabel ( "Welcome " + env.USER)
        self.reloadBTN = QPushButton("MANON LE DINDON")
        #Set production
        self.serverName = QLineEdit(env.SERVER)
        self.prodName = QLineEdit(env.TMP_PROD)
        self.assetDirName = QLineEdit(env.ASSET_TYPE)
        self.shotDirName = QLineEdit(env.SHOT_TYPE)
        self.prodLabel = QLabel ( "Enter Server and Production Name")
        self.createProd = QPushButton("Create Production")
        self.setProd = QPushButton("Set Production")
        #NEW ASSETS
        self.newCharBTN = QPushButton("NEW CHARACTER")
        self.newPropBTN = QPushButton("NEW PROP (to do)")
        self.itemBTN = QPushButton("NEW ITEM (to do)")
        self.IMAGES_PATHBTN = QPushButton("NEW IMAGES_PATHRARY (to do)")
        self.setBTN = QPushButton("NEW SET (to do)")
        self.newHip = QPushButton("NEW HIP (to do)")
        self.incrementSave = QPushButton("INCREMENT AND SAVE")
        #RENAME ASSET
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
        #CONNECTIONS
        self.newCharBTN.clicked.connect(self.createNewChara_UI)
        self.newPropBTN.clicked.connect(self.createNewProp_UI)
        self.renameButton.clicked.connect(self.renameAsset_UI)
        self.reloadBTN.clicked.connect(self.test_UI)

    def createLayout(self):
        # LAYOUT HIERARCHY
        outerLayout = QGridLayout()
        topLayout = QHBoxLayout()
        Layout_L = QVBoxLayout()
        tabsLayout_L = QTabWidget()
        tab01_Lay_L = QWidget()
        up_tab01_Layout_L = QVBoxLayout()
        mid_tab01_Layout_L = QGridLayout()
        dwn_tab01_Layout_L = QVBoxLayout()
        Layout_R = QVBoxLayout()
        tabs_Lay_R = QTabWidget()
        #ADD WIDGETS
        topLayout.addWidget(self.userLabel)
        topLayout.addWidget(self.prodTitle)
        topLayout.addWidget(self.reloadBTN)
        for widget in [self.prodLabel, self.serverName, self.prodName, self.assetDirName, self.shotDirName, self.createProd, self.setProd, self.assetName]:
            up_tab01_Layout_L.addWidget(widget)
        mid_tab01_Layout_L.addWidget( self.oldNameLabel, 0,0 )
        mid_tab01_Layout_L.addWidget( self.oldName, 0, 1 )
        mid_tab01_Layout_L.addWidget( self.newNameLabel , 1,0)
        mid_tab01_Layout_L.addWidget( self.newName , 1,1)
        mid_tab01_Layout_L.addWidget(self.renameButton)
        dwn_tab01_Layout_L.addWidget(self.plugIn_Label)
        dwn_tab01_Layout_L.addWidget(self.checkBoxAbc)
        dwn_tab01_Layout_L.addWidget(self.checkBoxMash)
        dwn_tab01_Layout_L.addWidget(self.checkBoxRenderMan)
        Layout_L.addWidget(tabsLayout_L)
        Layout_R.addWidget(tabs_Lay_R)
        tabsLayout_L.addTab(tab01_Lay_L, "HOME")
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
        
        #SET CUSTOM
        outerLayout.setColumnStretch(1,1)
        up_tab01_Layout_L.addStretch(1)
        up_tab01_Layout_L.setSpacing(5)
        tabsLayout_L.setTabPosition(tabsLayout_L.West)
        tabsLayout_L.setMovable(True)
        # tabsLayout_L.tabBarClicked(self.openTab)

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
        '''
        for pid in psutil.process_iter(['pid', 'name', 'username']):
            if pid.name() == PROCNAME:
                result = str(pid.info)
        '''        


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
        characterPath = os.path.join(env.SERVER, prod, env.ASSET_TYPE, env.CHAR_TYPE)
        assetcharacter = os.listdir( characterPath )
        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, assetcharacter):
            if name == '':
                continue
            imageDir = os.path.join(env.SERVER, env.IMAGES_PATH, "character", name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(env.SERVER, prod)
            layoutChar.addWidget(button)

            # CREER LISTE DE TOUS LES DEPARTEMENTS
            departmentList = os.listdir( os.path.join(characterPath , name , env.E_PATH))
            #CREER MENU
            menu = QMenu(parent = self)
            for dep in departmentList:
                #VARIABLES
                path = os.path.join(characterPath , name , env.E_PATH , dep)
                EDIT_TYPEProject = os.listdir( os.path.join(path , "_data" ))
                EDIT_TYPEImage = os.path.join(path , "_data", EDIT_TYPEProject[-1])
                publishImage = os.path.join(characterPath , name , env.PUBLISH_TYPE , dep , name , "_P_" , dep , ".png")
                destination = os.listdir( os.path.join(env.SERVER , prod , env.CHAR_PATH , name , env.E_PATH , dep ))
                file = os.path.join(env.SERVER , prod , env.CHAR_PATH , name , env.E_PATH ,dep , destination[-1])
                modified = os.path.getmtime(file)
                year,month,day,hour,minute,second=time.localtime(modified)[:-3]
                date = "%02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second)
                allEDIT_TYPEs = os.listdir(os.path.join( env.SERVER , prod , env.CHAR_PATH , name , env.E_PATH , dep ))

                #SubMenu
                items = menu.addMenu(dep)
                lastEdit = items.addAction(QIcon(EDIT_TYPEImage), "Open Last Edit (" + date + ")" )
                openPublish = items.addAction(QIcon(publishImage),"Open Publish (" + date + ")")
                items.addAction("Open In Folder (To Do)")
                EDIT_TYPEs = items.addMenu("All Edits")
                for i in allEDIT_TYPEs:
                    EDIT_TYPEs.addAction(i + " (" + date + ") (To Do)")  
                refPublish = items.addAction("Reference Publish")
                importPublish = items.addAction("Import Publish")
                #CONNECTIONS
                lastEdit.triggered.connect(partial(self.openLastEdit_UI, name, dep)) 
                openPublish.triggered.connect(partial(self.openPublish_UI, name, dep))  
                refPublish.triggered.connect(partial(self.refPublish_UI, name, dep)) 
                importPublish.triggered.connect(partial(self.importPublish_Char_UI, name, dep)) 

            #MENU ITEMS GLOBAL
            menu.addAction("Duplicate Asset (To Do)")
            delete = menu.addAction("Delete Asset")
            menu.addAction("Create New Task (To Do)")
            #Connections
            delete.triggered.connect(partial(self.deleteAsset_UI, name))

            button.setMenu(menu)
        #New Chara Button
        self.newCharBTN.setFixedSize(100, 100)
        layoutChar.addWidget(self.newCharBTN)

        #SET PROP GROUP
        layoutProp = FlowLayout()
        groupProp.setLayout(layoutProp)
        #New Chara Button
        self.newPropBTN.setFixedSize(100, 100)
        layoutProp.addWidget(self.newPropBTN)

        mayaTab.setLayout(base)
        return mayaTab

    # SHOTS -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def shotTabUI(self):
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        seqDIR = os.listdir(os.path.join(env.SERVER, prod, env.SHOT_TYPE))
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

    # SETS -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def setTabUI(self):
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        setDIR = os.listdir(os.path.join(env.SERVER, prod, env.SET_PATH))
        for setName in setDIR :
            tabs.addTab(self.moduleTabUI(setName), setName)
        n.addWidget(tabs)
        n.addWidget(self.setBTN)
        n.addWidget(self.IMAGES_PATHBTN)
        n.addWidget(self.itemBTN)
        layout.setLayout(n)
        return layout
    
    def moduleTabUI(self, setName):
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        tabs = QTabWidget()
        moduleDIR = os.listdir(os.path.join(env.SERVER, prod, env.SET_PATH, setName))
        for modName in moduleDIR :
            tabs.addTab(self.itemTabUI(setName, modName), modName)
        
        n.addWidget(tabs)
        
        layout.setLayout(n)
        return layout

    def itemTabUI(self, setName, modName):
        prod = self.prodName.text()
        layout = QWidget()
        n = QVBoxLayout()
        item = QPushButton()
        itemDIR = os.listdir(os.path.join(env.SERVER, prod, env.SET_PATH, setName, modName))

        #Create Button characters 
        positions = [(i, j) for i in range(50) for j in range(5)]
        for position, name in zip(positions, itemDIR):
            if name == '':
                continue
            imageDir = os.path.join(env.SERVER, env.IMAGES_PATH, "character", name + ".png")
            button = ImagePushButton(name, path = imageDir)
            button.setFixedSize(100, 100)
            
            path = os.path.join(env.SERVER, prod)
            n.addWidget(button)
            

        layout.setLayout(n)

        return layout

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

    def deleteAsset_UI(self, name):
        prod = self.prodName.text()
        fn.deleteAsset_FN(name, prod = prod)

    def renameAsset_UI(self):
        prod = self.prodName.text()
        oldName = self.oldName.text()
        newName = self.newName.text()
        print ( newName )
        fn.renameAsset_FN (prod = prod, oldName = oldName, newName = newName)

    def test_UI(self):
        fn.testFN()

    def refPublish_UI(self, name, dep):
        prod = self.prodName.text()
        fn.refPublishFN(name, dep, prod = prod)

    def importPublish_Char_UI(self, name, dep):
        prod = self.prodName.text()
        fn.importPublish_Char_FN(name, dep, prod = prod)

    ## UI CUSTOMIZE ##

    def openTab(self, tab01_Lay_L, up_tab01_Layout_L):
        tab01_Lay_L.setLayout(up_tab01_Layout_L)
'''
def setupData(self):
    self.lineEdit1 = QtWidgets.QLineEdit(self.prodName)
    self.lineEdit1.setObjectName("lineEdit1")
    self.lineEdit1.returnPressed.connect(self.return_pressed)
    self.autocomplete_list = ["suchomimus", "beast"]
    self.completer = QtWidgets.QCompleter(self.autocomplete_list)
    self.lineEdit1.setCompleter(self.completer)


def return_pressed(self):
    user_input = self.lineEdit1.text()
    updated_list = [x for x in self.autocomplete_list if x not in user_input]
    print(updated_list)
    self.completer = QtWidgets.QCompleter(updated_list)
    self.lineEdit1.setCompleter(self.completer)
    print('Gets to here')
'''
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