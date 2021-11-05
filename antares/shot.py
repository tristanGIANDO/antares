import os, shutil, env

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

def create_new_shot_FN(nb_seq, nb_shot, prefix, server, prod):

    true_scn_temp = os.path.join(server,
                            prod,
                            env.LIBRARY,
                            env.TMP_SCN_TYPE_SHOT)
                            
    
    scn_temp = os.path.join(server,
                            prod,
                            env.TMP_ASSET_PATH,
                            env.E_PATH,
                            env.GEO_LO,
                            env.TMP_SCN_TYPE_E + env.ASCII)


    scn_temp_nuke = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            env.TMP_SEQ_TYPE_NUKE,
                            env.TMP_SCN_TYPE_NUKE)


    seq_path_main = os.path.join(server,
                            prod,
                            env.SHOT_TYPE,
                            env.SEQ + nb_seq,
                            env.SEQ + nb_seq + "_sh" + nb_shot
                            )

    seq_path_compo = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            env.SEQ + nb_seq,
                            env.SEQ + nb_seq + "_sh" + nb_shot
                            )

    # MAIN BRANCH
    try:
        os.makedirs(seq_path_main)
        
        for soft in ["camera", env.HOUDINI_TYPE, env.MAYA_TYPE, env.UNREAL_TYPE]:
            os.makedirs(os.path.join(seq_path_main,
                            soft))

        for dep in ["abc", "audio", "comp", "desk", "flip", "geo", "hdz", env.RENDER_TYPE, "scripts", "sim", env.SCN_TYPE, "tex", "video"]:
            os.makedirs(os.path.join(seq_path_main,
                            "houdini",
                            dep))

        for maya_folders in ["cache", "images", "movies", env.SCN_TYPE, env.SRC_IMG_TYPE]:
            os.makedirs(os.path.join(seq_path_main,
                            "maya",
                            maya_folders))

        for category in [env.ANIM_TYPE, env.CFX_TYPE, env.VFX_TYPE, env.RENDER_TYPE]:
            path = os.makedirs(os.path.join(seq_path_main,
                            env.MAYA_TYPE,
                            env.SCN_TYPE,
                            category))

            dest_scn_tmp = os.path.join ( seq_path_main,
                            env.MAYA_TYPE,
                            env.SCN_TYPE,
                            category,
                            env.TMP_SCN_TYPE_E + env.ASCII )
            
            renamed_file = os.path.join ( seq_path_main,
                            env.MAYA_TYPE,
                            env.SCN_TYPE,
                            category,
                            prefix + env.SEQ_ + nb_seq + env.SHOT_ + nb_shot + "_" + category + "_001" + env.ASCII )

            
            try:
                shutil.copyfile(true_scn_temp, dest_scn_tmp)
                os.rename(dest_scn_tmp, renamed_file)

                print ( env.SEQ + nb_seq + env.SHOT_ + nb_shot + " in " + env.SHOT_TYPE + " created with success !!")
            except:
                shutil.copyfile(scn_temp, dest_scn_tmp)
                os.rename(dest_scn_tmp, renamed_file)
                print ( "scenes from geoLo copied")

        
    except:
        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.SHOT_TYPE + " already created")

    # COMPO BRANCH
    try:   
        os.makedirs(seq_path_compo)

        for directory in [env.INPUT_TYPE, env.OUTPUT_TYPE]:
            os.makedirs(os.path.join(seq_path_compo,
                            directory))

        for input in ["abc", "filtered", "nonFiltered"]:
            os.makedirs(os.path.join(seq_path_compo,
                            env.INPUT_TYPE,
                            input))

        for output in ["DCP", "DPX", "Preview"]:
            os.makedirs(os.path.join(seq_path_compo,
                            env.OUTPUT_TYPE,
                            output))
        
        dest_scn_tmp = os.path.join ( seq_path_compo,
                            env.TMP_SCN_TYPE_NUKE)
    
        renamed_file = os.path.join ( seq_path_compo,
                            prefix + env.SEQ_ + nb_seq + env.SHOT_ + nb_shot + "_compo_001.nk")

        try:
            shutil.copyfile(scn_temp_nuke, dest_scn_tmp)
            os.rename(dest_scn_tmp, renamed_file)
        except:
            print ( "no scene copied")

        print ( env.SEQ + nb_seq + env.SHOT_ + nb_shot + " in " + env.COMPO_TYPE + " created with success !!")
    except:
        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.COMPO_TYPE + " already created")


def layout_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.LAYOUT_PATH
                            )

    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.LAYOUT_PATH + " yet, or the layout is on another server")
    
    try:
        destination.remove("_data")
    except:
        print ( "No data")

    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def layout_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.LAYOUT_PATH
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def anim_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.ANIM_PATH
                            )

    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.ANIM_PATH + " yet, or the animation is on another server")
    
    try:
        destination.remove("_data")
    except:
        print ( "No data")

    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def anim_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.ANIM_PATH
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def render_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.RENDER_PATH
                            )

    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.RENDER_PATH + " yet, or the render is on another server")
    
    try:
        destination.remove("_data")
    except:
        print ( "No data")

    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def render_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.RENDER_PATH
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def cfx_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.CFX_PATH
                            )

    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.CFX_PATH + " yet, or the cfx are on another server")
    
    try:
        destination.remove("_data")
    except:
        print ( "No data")

    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def cfx_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.CFX_PATH
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def vfx_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.VFX_PATH
                            )

    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.VFX_PATH + " yet, or the vfx are on another server")
    
    try:
        destination.remove("_data")
    except:
        print ( "No data")
    
    
    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def vfx_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.VFX_PATH
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def compo_open_last_edit_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.COMPO_TYPE ,
                            seq,
                            name ,
                            )
    
    try:
        destination = os.listdir( path )
    except:
        print ( "Or there is no folder in " + env.COMPO_TYPE + " yet, or the compositing is on another server")
    
    try:
        destination.remove("input")
        destination.remove("output")
    except:
        print ( "No input, no output")
    
    
    try:
        project = os.path.join(path,  destination[-1])
        print ( project )
        os.startfile(project)
        print ("Let's open this scene !!")
    except:
        print ( "no file created yet")

def compo_open_in_folder_FN(name, seq, server, prod):
    path = os.path.join(server  ,
                            prod,
                            env.COMPO_TYPE ,
                            seq,
                            name ,
                            )
    print (path)

    try:
        os.startfile(path)
        print ("Let's open this folder !!")
    except:
        print ( "I can't see any folder")

def render_send_to_nuke_FN(name, seq, rendu, server, prod):
    path = os.path.join(server,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.MAYA_TYPE,
                            "images",
                            rendu
                            )

    compo_path = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            seq,
                            name,
                            env.INPUT_TYPE,
                            rendu
                            )
    print ( path )
    print ( compo_path )

    try:
        shutil.copytree(path, compo_path)
        print ( "It's copied")
    except:
        print ( "I can't see any folder to send")
