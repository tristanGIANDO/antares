def LockRendermanAttributes():
    selected = cmds.ls(sl = True)
    for obj in selected:
    	
        cmds.setAttr (obj +'.rman_matteObject',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_holdout',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_nestedInstancing',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_maxDiffuseDepth',keyable = False, cb = False, lock = True)
    	cmds.setAttr (obj +'.rman_maxSpecularDepth',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_relativePixelVariance',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_intersectPriority',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_visibilityCamera',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_visibilityIndirect',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_visibilityTransmission',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_userAttrs',keyable = False, cb = False, lock = True)
        cmds.setAttr (obj +'.rman_motionSamples',keyable = False, cb = False, lock = True)

LockRendermanAttributes()