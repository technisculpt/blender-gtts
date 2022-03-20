import bpy

class TextToSpeechSettings(bpy.types.PropertyGroup):
    persistent_string : bpy.props.StringProperty(name='Persistent String')
    string_field : bpy.props.StringProperty(name='Text')
    accent_enumerator : bpy.props.EnumProperty(
                name = "",
                description = "accent options for speakers",
                items=[ ('0',"English (Australia)",""),
                        ('1',"English (United Kingdom)",""),
                        ('2',"English (United States)",""),
                        ('3',"English (Canada)",""),
                        ('4',"English (India)",""),
                        ('5',"English (Ireland)",""),
                        ('6',"English (South Africa)",""),
                        ('7',"French (Canada)",""),
                        ('8',"French (France)",""),
                        ('9',"Mandarin (China Mainland)",""),
                        ('10',"Mandarin (Taiwan)",""),
                        ('11',"Portuguese (Brazil)",""),
                        ('12',"Portuguese (Portugal)",""),
                        ('13',"Spanish (Mexico)",""),
                        ('14',"Spanish (Spain)",""),
                        ('15',"Spanish (US)","")]
        )
    pitch : bpy.props.FloatProperty(
        name="Pitch",
        description="Speechify pitch",
        default=1.0,
        min=0.1, max=10.0,
        )
        

class TextToSpeech_PT(bpy.types.Panel):
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_label = 'Text To Speech'
    bl_category = 'Text To Speech'
    bl_idname = 'SEQUENCER_PT_text_to_speech'

    def draw(self, context):

        layout = self.layout
        scene = context.scene.text_to_speech

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'accent_enumerator', text='Accent')
        
        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'pitch', text='Pitch')

        box = layout.box()
        col = box.column(align=True)
        col.use_property_split = False
        col.prop(scene, 'string_field', text = '')
        col.operator('text_to_speech.speak', text = 'Speechify', icon='ADD')

        col = layout.column()
        layout.operator('text_to_speech.load', text = 'Load Captions File',  icon='IMPORT')

        col = layout.column()
        subrow = layout.row(align=True)
        subrow.operator('text_to_speech.export', text = 'Export Captions File', icon='EXPORT')


