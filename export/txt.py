# append dir to path for dev, for prod use from . import module
import sys
import os
import bpy

def export(filepath, captions):
    try:
        with open(f"{filepath}.txt", "x") as f:

            for caption in range(len(captions)):

                if captions[caption].cc_type == 0: # default text

                    f.write(captions[caption].text + '\n')

                elif captions[caption].cc_type == 1: # person

                    f.write(">> " + captions[caption].name + ': ' + captions[caption].text + '\n')

                elif captions[caption].cc_type == 2: # event

                    f.write('[' + captions[caption].text + ']\n' )

                if caption < len(captions):
                    f.write('\n')

        return(True)

    except FileExistsError:
        print("File already exists")
        return(False)