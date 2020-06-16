from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

kv='''
#:import Snackbar kivymd.uix.snackbar.Snackbar
BoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "Now Playing"
        right_action_items: [["playlist-music", lambda x: Snackbar(text="Playlist").show()]]
    BoxLayout:
        size_hint_y: .6
        FitImage:
            source: "res/imaginedragon.jpg"
    BoxLayout:
        size_hint_y: .2
        orientation: "vertical"
        MDSlider:
            id: slider
            min: 0
            max: 100
            hint: False
        MDBoxLayout:
            adaptive_height: True
            orientation: "horizontal"
            MDIcon:
                halign: "center"
                icon: "repeat"
            MDBoxLayout:
                adaptive_height: True
                adaptive_weidht: True
                orientation: "vertical"
                MDLabel:
                    text: "Bad Liar"
                    font_style: "Subtitle1"
                    halign: "center"
                    size_hint_y: None
                    height: "20dp"
                MDLabel:
                    height: "20dp"
                    size_hint_y: None
                    text: "Imagine Dragons"
                    font_style: "Subtitle2"
                    halign: "center"
            MDIcon:
                halign: "center"
                icon: "shuffle"
        MDSeparator:
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            MDIcon:
                halign: "center"
                icon: "skip-previous"
            MDIcon:
                halign: "center"
                icon: "play"
            MDIcon:
                halign: "center"
                icon: "skip-next"
              
'''

class MusicApp(MDApp):

    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        Clock.schedule_interval(self.prog, 1)

    def prog(self, *args):
        if self.root.ids.slider.value >= 99:
            self.root.ids.slider.value = 0
        else:
            self.root.ids.slider.value += 1

MusicApp().run()