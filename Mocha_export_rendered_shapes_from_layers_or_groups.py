import mocha.project as mp
import os

""" This script exports rendered shapes to png sequences
for either all visible layers or for all groups in the project.

If groups exist in the project, each group will be exported separately with 
the group name appended to the exported files.

If no groups exist, all visible layers will be exported as a png sequence with '_all'
appended to the exported files.

File name allways starts with the project name.
The exported files are saved in a folder named 'savedMattes' one level above the project file location.

"""

def has_groups():
    proj = mp.get_current_project()
    if len(proj.groups) == 0:
        return(False)

def export_rendered_shapes_for_groups():
    # Hent det aktuelle projekt
    proj = mp.get_current_project()

    # Få projektets filnavn uden sti og extension
    project_name = os.path.splitext(os.path.basename(proj.project_file))[0]
    project_dir = os.path.dirname(proj.project_file)
    save_dir = os.path.join(project_dir, "..", "savedMattes")

    print(f"projekt: {project_name} \n  dir: {project_dir} \n  save_dir: {save_dir}\n")

    # Iterer gennem alle grupper i projektet
    for group in proj.groups:
        group_name = group.name
        print(f"  Group: {group.name}")
        if group.visibility == False:
            print(f"  .. er ikke synlig. Springes over")
            continue

        save_name = f"{project_name}_{group_name}"
        save_path = os.path.join(save_dir, save_name)

        # Saml alle lag i gruppen
        layers = group.layers
        layernames = [layer.name for layer in layers]

        print(f"  Eksporterer lagene: {layernames}\n  frames: {proj.in_out_range}\n  filnavn: {save_name}\n  i: {save_path}")

        # Eksporter rendered shapes
        proj.export_rendered_shapes(
            layers,
            mp.ColorizeOutput.Grayscale,  # Eksport as grayscale
            save_path,
            ".png",  # Eksporter som MP4
            save_name,
            "",
            proj.in_out_range[0],
            proj.in_out_range[1],
            5
        )

        print(f"Eksporteret: {save_name}\n")

def export_rendered_shapes():
    # Hent det aktuelle projekt
    proj = mp.get_current_project()

    # Få projektets filnavn uden sti og extension
    project_name = os.path.splitext(os.path.basename(proj.project_file))[0]
    project_dir = os.path.dirname(proj.project_file)
    save_dir = os.path.join(project_dir, "..", "savedMattes")

    print(f"projekt: {project_name} \n  dir: {project_dir} \n  save_dir: {save_dir}\n")

    save_name = f"{project_name}_alle"
    save_path = os.path.join(save_dir, save_name)

    
    vis_layers = []
    layer_list = proj.layers

    for layer in layer_list:
        # print(layer.name)
        if layer.visibility:
            vis_layers.append(layer)

    layernames = [layer.name for layer in vis_layers]

    print(f"  Eksporterer lagene: {layernames}\n  frames: {proj.in_out_range}\n  filnavn: {save_name}\n  i: {save_path}")

        # Eksporter rendered shapes
    proj.export_rendered_shapes(
        vis_layers,
        mp.ColorizeOutput.Grayscale,  # Export as grayscale
        save_path,
        ".png",
        save_name+"_",
        "",
        proj.in_out_range[0],
        proj.in_out_range[1],
        index_width=5,
        offset=proj.in_out_range[0]
    )

    print(f"Eksporteret: {save_name}\n")
        
def render_shapes():
    if has_groups():
        print("Har group")
        export_rendered_shapes_for_groups()
    else:
        print("Har ikke group")
        export_rendered_shapes()