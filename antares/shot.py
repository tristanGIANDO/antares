import os, json, env

def create_new_seq_FN(server, prod):
    print ( "CREER le template")

def create_new_shot_FN(assetName, seq, server, prod):
    print ( "CREER le template")

def open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.ANIM_PATH
                            )
    destination = os.listdir( path )
    try:
        destination.remove("_data")
    except:
        print ( "No data")
    project = os.path.join(path,  destination[-1])
    print ( project )
    print ("Let's open this scene !!")
    os.startfile(project)