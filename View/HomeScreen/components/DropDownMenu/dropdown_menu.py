import os

from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarIconListItem


class Item(OneLineAvatarIconListItem):
    primary_color = get_color_from_hex("#b6b6b7")
    text_color = primary_color
    left_icon = StringProperty()
    theme_text_color = "Custom"


Builder.load_file(f"{os.path.dirname(__file__)}/dropdown_menu.kv")
