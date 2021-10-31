import os

from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout


class ContentNavigationDrawer(MDBoxLayout):
    def __init__(self, **kwargs):
        # Load KV
        super().__init__(**kwargs)


Builder.load_file(f"{os.path.dirname(__file__)}/content_navigation_drawer.kv")
