import bpy
import os
import sys

from . import text_to_sound as tts

class Caption():
    def __init__(self, cc_type, name, text, start_time, end_time, accent, channel):
        self.cc_type = cc_type # 0 : default, 1 : person, 2 : event
        self.accent = accent
        self.name = name
        self.text = text
        self.start_time = start_time
        self.end_time = end_time
        self.frame_start = start_time.time_to_frame()
        self.channel = channel

        if text != -1:
            if self.frame_start != -1:
                self.sound_strip = tts.sound_strip_from_text(text, self.frame_start, accent, channel)
            else:
                self.sound_strip = tts.sound_strip_from_text(text, 0, accent, channel)
        else:
            self.sound_strip = ""

    def update_timecode(self):
        self.start_time.frame_to_time(self.sound_strip.frame_start)
        self.end_time.frame_to_time(self.sound_strip.frame_final_end)
        self.current_seconds = self.sound_strip.frame_start / bpy.context.scene.render.fps