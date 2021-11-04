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

def create_new_shot_FN(nb_seq, nb_shot, server, prod):
    seq_path_main = os.path.join(server,
                            prod,
                            env.SHOT_TYPE,
                            "seq" + nb_seq,
                            "seq" + nb_seq + "_sh" + nb_shot
                            )

    seq_path_compo = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            "seq" + nb_seq,
                            "seq" + nb_seq + "_sh" + nb_shot
                            )
                            
    # MAIN BRANCH
    try:
        os.makedirs(seq_path_main)
        
        for soft in ["camera", "houdini", "maya", "unreal"]:
            os.makedirs(os.path.join(seq_path_main,
                            soft))

        for dep in ["abc", "audio", "comp", "desk", "flip", "geo", "hdz", "render", "scripts", "sim", "scenes", "tex", "video"]:
            os.makedirs(os.path.join(seq_path_main,
                            "houdini",
                            dep))

        for maya_folders in ["cache", "images", "movies", "scenes", "sourceimages"]:
            os.makedirs(os.path.join(seq_path_main,
                            "maya",
                            maya_folders))

        for category in ["anim", "cfx", "layout", "render"]:
            os.makedirs(os.path.join(seq_path_main,
                            "maya",
                            "scenes",
                            category))

        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.SHOT_TYPE + " created with success !!")
    except:
        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.SHOT_TYPE + " already created")

    # COMPO BRANCH
    try:   
        os.makedirs(seq_path_compo)

        for directory in ["input", "output"]:
            os.makedirs(os.path.join(seq_path_compo,
                            directory))

        for input in ["abc", "filtered", "nonFiltered"]:
            os.makedirs(os.path.join(seq_path_compo,
                            "input",
                            input))

        for output in ["DCP", "DPX", "Preview"]:
            os.makedirs(os.path.join(seq_path_compo,
                            "output",
                            output))

        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.COMPO_TYPE + " created with success !!")
    except:
        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.COMPO_TYPE + " already created")


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