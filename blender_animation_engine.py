import shutil
import subprocess


def blender_animation_engine(blender_file, script_file):
    # Get the path to the Blender executable
    blender_exe = shutil.which("blender")
    if blender_exe:
        print(f"Found: {blender_exe}")
    else:
        print("Unable to find Blender!")
        return

    # Call Blender from the command line and pass the script as an argument
    subprocess.call([blender_exe, '-b', blender_file, '-P', script_file])
