import os
import maya.cmds as cmds
'''
cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
print ("Connection Okay")
'''
# project = os.path.join(env.SERVER , prod , env.TYPE_CHAR_PATH , name , env.P_DIR , dep , name + "_P_" + dep + ".ma")
# cmds.file( "C:\Users\Windows\Desktop\rigManon\manon_E_rig_002.ma", r=True, namespace = "CHAR_1")
cmds.joint()
print ("Done")