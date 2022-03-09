# append dir to path for dev, for prod use from . import module
import sys
import os

dir = r'/home/magag/text_to_speech'
if os.name == 'nt':
    dir = r"C:\Users\marco\blender-text-to-speech"
sys.path.append(dir)

import bpy

import importlib
import blender_time as b_time
importlib.reload(b_time)
import caption as c
importlib.reload(c)

def import_cc(text, accent):
    print(".sbv file detected")
    captions = []
    line_counter = 0
    cc_text = ""
    cc_type = 1
    cc_time = 0
    start_time = 0
    end_time = 0

    for line in text:

        if len(line) > 0:

            if (line[0].isnumeric() and line.find(':') != -1 # timecode
                and line.find(',') != -1):

                start = line.split(",")[0]
                end = line.split(",")[1]
                hrs_start = int(start.split(":")[0])
                min_start = int(start.split(":")[1])
                sec_start = int(start.split(":")[2].split('.')[0])
                ms_start = int(start.split(":")[2].split('.')[1])

                hrs_end = int(end.split(":")[0])
                min_end = int(end.split(":")[1])
                sec_end = int(end.split(":")[2].split('.')[0])
                ms_end = int(end.split(":")[2].split('.')[1])

                start_time = b_time.Time(hrs_start, min_start, sec_start, ms_start)
                end_time = b_time.Time(hrs_end, min_end, sec_end, ms_end)

            elif line[0:2].find('>>') != -1: # person
                cc_type = 1
                cc_name = line[2:len(line)].split(":")[0]
                text_tmp = line[2:len(line)].split(":")[1]
                cc_text = text_tmp[1:len(text_tmp)]

            elif line[0] == '[': # event
                cc_type = 2
                cc_name = ''
                cc_text = line.split('[')[1].split(']')[0]
            
            elif(len(line) > 1): # plain text line
                
                if len(cc_text) == 0: # no previous line
                    cc_name = "noname"
                    cc_type = 0
                    cc_text = line

                    
                else: # second line
                    cc_text += " " + line

        else: # len(line == 0) equivalent of '\n'
            captions.append(c.Caption(cc_type, cc_name, cc_text, start_time, end_time, accent, 1))
            cc_text = ""

        line_counter += 1
        if line_counter == len(text): # on exit
            if len(cc_text) > 0:
                captions.append(c.Caption(cc_type, cc_name, cc_text, start_time, end_time, accent, 1))
    
    return(captions)
