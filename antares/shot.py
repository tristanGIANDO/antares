import os, json, env

def create_new_seq_FN(nb_seq, server, prod):
    print ( nb_seq )
    print ( server )
    print ( prod )

    seq_path_main = os.path.join(server,
                            prod,
                            env.SHOT_TYPE,
                            "seq" + nb_seq
                            )

    seq_path_compo = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            "seq" + nb_seq
                            )
    
    try:
        os.makedirs(seq_path_main)
        print ( "seq" + nb_seq + " in " + env.SHOT_TYPE + " created with success !!")
    except:
        print ( "seq" + nb_seq + " in " + env.SHOT_TYPE + " already created")
    try:   
        os.makedirs(seq_path_compo)
        print ( "seq" + nb_seq + " in " + env.COMPO_TYPE + " created with success !!")
    except:
        print ( "seq" + nb_seq + " in " + env.COMPO_TYPE + " already created")

    

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