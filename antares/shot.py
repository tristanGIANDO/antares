import os, shutil, env, datetime

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

    true_scn_temp_nuke = os.path.join(server,
                            prod,
                            env.COMPO_TYPE,
                            env.TMP_SEQ_TYPE_NUKE,
                            env.TMP_SCN_TYPE_NUKE_TRUE)

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

        

        for dep in ["abc", "audio", "comp", "desk", "flip", "geo", "hdz", env.RENDER_TYPE, "scripts", "sim", "tex", "video"]:
            os.makedirs(os.path.join(seq_path_main,
                            "houdini",
                            dep))

        for maya_folders in ["cache", "images", "movies", env.SCN_TYPE, env.SRC_IMG_TYPE]:
            os.makedirs(os.path.join(seq_path_main,
                            "maya",
                            maya_folders))

        for category in [env.ANIM_TYPE, env.CFX_TYPE, env.VFX_TYPE, env.RENDER_TYPE, env.LAYOUT_TYPE]:
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
            shutil.copyfile(scn_temp_nuke, dest_scn_tmp)
            os.rename(dest_scn_tmp, renamed_file)

        print ( env.SEQ + nb_seq + env.SHOT_ + nb_shot + " in " + env.COMPO_TYPE + " created with success !!")
    
        
        src_tmp_frame = os.path.join(server,
                        prod,
                        env.LIBRARY,
                        env.TMP_FRAME)
        
        dst_tmp_frame = os.path.join(server,
                        prod,
                        env.SHOT_TYPE,
                        env.SEQ + nb_seq,
                        env.SEQ + nb_seq + env.SHOT_ + nb_shot,
                        env.TMP_FRAME)
        print ( src_tmp_frame )
        print (dst_tmp_frame)

        try:
            shutil.copyfile(src_tmp_frame, dst_tmp_frame)
        except:
            print ( "no template frame file")

    except:
        print ( "seq" + nb_seq + "_sh" + nb_shot + " in " + env.COMPO_TYPE + " already created")

    # LIBRARY
    try:
        src_img = os.path.join(server,
                            prod,
                            env.IMAGES_PATH,
                            env.TMP_IMAGE)

        dst_img = os.path.join(server,
                            prod,
                            env.IMAGES_PATH,
                            env.SHOT_LIB,
                            env.TMP_IMAGE)

        renamed_dst_img = os.path.join(server,
                            prod,
                            env.IMAGES_PATH,
                            env.SHOT_LIB,
                            env.SEQ + nb_seq + env.SHOT_ + nb_shot + env.PNG)

        print ( src_img )
        print ( dst_img )

        shutil.copyfile(src_img, dst_img)
    except:
        print ( "no image profile ")

    try:
        os.rename(dst_img, renamed_dst_img)
    except:
        print ( "profile picture not renamed")

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
                            env.HOUDINI_TYPE
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
                            env.HOUDINI_TYPE
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
                            env.NON_FILTERED,
                            rendu
                            )
    print ( path )
    print ( compo_path )

    try:
        shutil.copytree(path, compo_path)
        print ( "It's copied")
    except:
        print ( "I can't see any folder to send")

def anim_send_to_delivery_FN(name, seq, playblast, server, prod):

    date = datetime.datetime.now()
    str(date)
    year = date.year
    month = date.month
    day = date.day
    print ( year, month, day )
    converted_year = "{}".format(year)
    print(type(converted_year))
    converted_month = "{}".format(month)
    print(type(converted_month))
    converted_day = "{}".format(day)
    print(type(converted_day))
    annemojr = converted_year + converted_month + converted_day

    try:
        os.makedirs(os.path.join(server,
                            prod,
                            env.EDITING_TYPE,
                            "IN",
                            "published",
                            env.DELIVERY_TYPE,
                            annemojr))
                        
    except:
        print ( "Delivery folder of the day already exists." )

    path = os.path.join(server,
                            prod,
                            env.SHOT_TYPE ,
                            seq,
                            name ,
                            env.MAYA_TYPE,
                            "movies",
                            playblast
                            )

    delivery_path = os.path.join(server,
                            prod,
                            env.EDITING_TYPE,
                            "IN",
                            "published",
                            env.DELIVERY_TYPE,
                            annemojr,
                            playblast
                            )

    renamed_delivery_path = os.path.join(server,
                            prod,
                            env.EDITING_TYPE,
                            "IN",
                            "published",
                            env.DELIVERY_TYPE,
                            annemojr,
                            env.ANIM_TYPE + "_" + playblast
                            )

    print ( path )
    print ( delivery_path )

    try:
        shutil.copyfile(path, delivery_path)
        os.rename(delivery_path, renamed_delivery_path)
        print ( "It's copied")
    except:
        print ( "I can't see any playblast to send")