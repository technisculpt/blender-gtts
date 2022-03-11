bl_info = {
    "name": "Text to Speech",
    "description": "turns text into speech",
    "author": "Mark Lagana",
    "version": (1, 0),
    "blender": (2, 93, 4),
    "location": "SEQUENCE_EDITOR > UI > Text to Speech",
    "warning": "",
    "doc_url": "https://github.com/technisculpt/blender-text-to-speech",
    "support": "COMMUNITY",
    "category": "Sequencer",
}

from numbers import Number
from re import T
import sys
import os

import bpy

try:
    import gtts

except ModuleNotFoundError:
    print("installing gtts...")
    import subprocess
    from pathlib import Path

    if bpy.app.version < (2, 92, 0):
        py_exec = bpy.app.binary_path_python
        subprocess.call([str(py_exec), "-m", "ensurepip", "--user"])
        subprocess.call([str(py_exec), "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.call([str(py_exec),"-m", "pip", "install", "--user", "gtts"])
    else:
        py_exec = str(sys.executable)
        lib = os.path.join(Path(py_exec).parent.parent, "lib")
        subprocess.call([py_exec, "-m", "ensurepip", "--user" ])
        subprocess.call([py_exec, "-m", "pip", "install", "--upgrade", "pip" ])
        subprocess.call([py_exec,"-m", "pip", "install", f"--target={str(lib)}", "gtts"])
        
        try:
            import gtts
            print("gtts installed")
        except PermissionError:
            print("to install, right click the Blender icon and run as Administrator")
        except:
            print("Error installing gtts")

from . import operators
from . import ui

classes = (
    ui.TextToSpeechSettings,
    ui.TextToSpeech_PT,
    operators.TextToSpeechOperator,
    operators.ImportClosedCapFile,
    operators.LoadFileButton,
    operators.ExportFileName,
    operators.ExportFileButton,
    )

def register_handlers():
    for handler in bpy.app.handlers.load_post:
        if handler.__name__ == 'load_handler':
            bpy.app.handlers.load_post.remove(handler)

    for handler in bpy.app.handlers.save_pre:
        if handler.__name__ == 'save_handler':
            bpy.app.handlers.save_pre.remove(handler)

    bpy.app.handlers.load_post.append(operators.load_handler)
    bpy.app.handlers.save_pre.append(operators.save_handler)


def de_register_handlers():
    for handler in bpy.app.handlers.load_post:
        if handler.__name__ == 'load_handler':
            bpy.app.handlers.load_post.remove(handler)

    for handler in bpy.app.handlers.save_pre:
        if handler.__name__ == 'save_handler':
            bpy.app.handlers.save_pre.remove(handler)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.text_to_speech = bpy.props.PointerProperty(type=ui.TextToSpeechSettings)
    register_handlers()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.text_to_speech
    de_register_handlers()

if __name__ == '__main__':
    register()