# blender_animation_engine.py
import subprocess
import os
import shutil
import bpy


def blender_animation_engine(blender_file, script_file):
    # Get the path to the Blender executable
    blender_bin = shutil.which("blender")
    if blender_bin:
        print(f"found:\t {blender_bin}")
        bpy.app.binary_path = blender_bin
        blender_exe = bpy.app.binary_path

    # Check if the Blender executable exists
    elif not os.path.exists(bpy.app.binary_path):
        print(f"Unable to find Blender executable at {bpy.app.binary_path}")
        return

    # Call Blender from the command line and pass the script as an argument
    subprocess.call([blender_exe, '-b', blender_file, '-P', script_file])
