import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math



###### CREATE MATRIX ######


def create_matrix ( *args ):
    sl = cmds.ls(sl=True, sn=True)
    Master = sl[0]
    Slave = sl[1]


    # CREATE NODES

    MultMatX  = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_'+Slave)
    DecMatX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_'+Slave)
    MultMatX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+Slave)
    DecMatX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+Slave)


    # CREATE OFFSET
    
    if(cmds.checkBox(checkOffset,q=1,v=1)):

        cmds.connectAttr(Slave+'.worldMatrix[0]',MultMatX_Offset+'.matrixIn[0]')
        cmds.connectAttr(Master+'.worldInverseMatrix[0]',MultMatX_Offset+'.matrixIn[1]')
        cmds.connectAttr(MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
        cmds.disconnectAttr (MultMatX_Offset+'.matrixSum',DecMatX_Offset+'.inputMatrix')
        cmds.delete(MultMatX_Offset)
        
    elif(cmds.checkBox(checkOffset,q=1,v=0)):
        
        cmds.connectAttr(Slave+'.worldMatrix[0]', DecMatX_Offset+'.inputMatrix')
        cmds.connectAttr(Master+'.worldInverseMatrix[0]', DecMatX_Offset+'.inputMatrix')
        

    # CONNECT OFFSET TO MULTIPLY AND DECOMPOSE MATRIX

    cmds.connectAttr(DecMatX_Offset+'.inputMatrix',MultMatX+'.matrixIn[0]')
    cmds.connectAttr(Master+'.worldMatrix[0]',MultMatX+'.matrixIn[1]')
    cmds.connectAttr(Slave+'.parentInverseMatrix[0]',MultMatX+'.matrixIn[2]')
    cmds.connectAttr(MultMatX+'.matrixSum',DecMatX+'.inputMatrix')




    #CHECKBOX INFO
 
    
    #TRANSLATE
    if(cmds.checkBoxGrp(checkMat,q=1,v1=1)):
        print "Button is pushed."
        cmds.connectAttr(DecMatX+'.outputTranslate',Slave+'.t')
        print "Constraint Translate successful"
 
       
    #ROTATE    
    if(cmds.checkBoxGrp(checkMat,q=1,v2=1)): 
        print "Button is pushed."   
        cmds.connectAttr(DecMatX+'.outputRotate',Slave+'.r') 
        print "Constraint Rotate successful"
 
 
    #SCALE        
    if(cmds.checkBoxGrp(checkMat,q=1,v3=1)): 
        print "Button is pushed."
        cmds.connectAttr(DecMatX+'.outputScale',Slave+'.s')
        print "Constraint Rotate successful"







#############################
## USER INTERFACE SETTINGS ##
#############################


diUi = {}
diUi["lays"] = {}
diUi["ctrls"] = {}
diUi["window"] = {}

if cmds.window("giandoMatrix", exists=True):
	cmds.deleteUI("giandoMatrix")
window = diUi["window"]["main"]= cmds.window("giandoMatrix", title="Giando_Matrix", sizeable=True, maximizeButton=False)


###### LAYERS HIERARCHY

diUi["lays"]["root"] = cmds.frameLayout(l="MATRIX", p=diUi["window"]["main"], bgc=(0.0,0.1,0.25), h=50)
diUi["lays"]["rootPan1"] = cmds.columnLayout(adj=True, p=diUi["lays"]["root"])



cmds.setParent (diUi["lays"]["rootPan1"])
cmds.text ( label = "Select Master and Slave before running the script.", align="center")
checkOffset = cmds.checkBox( label = "Maintain Offset", al="center", v=True )
checkMat = cmds.checkBoxGrp( numberOfCheckBoxes=3, label="Constraint", labelArray3=["Translate", "Rotate", "Scale"], va3=[True, True, True], vr= True )
cmds.button ( label= "Create Matrix", enableBackground=True, command=create_matrix, backgroundColor=[0.0, 0.4, 0.4])




cmds.showWindow (diUi["window"]["main"])