from kivymd.app import MDApp
from kivy.lang import Builder

kv='''
BoxLayout:
    orientation: "vertical"
    MDBoxLayout:
        id: head
        adaptive_height: True
        height: "150dp"
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source: "res/background_header.jpg"
        canvas:
            Color:
                rgba: 1,1,1,1
            Ellipse:
                size: 110, 110
                pos: root.width/2-55, head.pos[1]-55
        canvas.after:
            Ellipse:
                source: "res/profil_picture.jpeg"
                size: 100, 100
                pos: root.width/2-50, head.pos[1]-50
    Widget:
        height: "160dp"
    MDLabel:
        text: "Gabriel Angela"
        halign: "center"
        font_style: "H6"
    MDLabel:
        padding_x: "20dp"
        text: "This community is for discussing all things Kivy. As with all communities, we have a few rules to keep things friendly."
        halign: "center"
    Widget:
        height: "2dp"
    MDRaisedButton:
        text: "FOLLOW"
        pos_hint: {"center_x": .5}
    Widget:
        height: "2dp"
    GridLayout:
        cols: 3
        MDLabel:
            text: "8282"
            font_style: "Subtitle2"
            halign: "center"
        MDLabel:
            text: "5445"
            font_style: "Subtitle2"
            halign: "center"
        MDLabel:
            text: "9.2"
            font_style: "Subtitle2"
            halign: "center"
        MDLabel:
            text: "Followers"
            halign: "center"
        MDLabel:
            text: "Following"
            halign: "center"
        MDLabel:
            text: "Score"
            halign: "center"
    Widget:
    Widget:
    Widget:
'''

class PolygonApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

PolygonApp().run()