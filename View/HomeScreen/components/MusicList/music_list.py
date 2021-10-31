import os

from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.metrics import dp

from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu


class MusicListWithDropdown(TwoLineAvatarIconListItem):
    right_text = StringProperty()

    left_icon = "github"
    right_icon = "dots-vertical"

    right_icon_background = get_color_from_hex("#000000")
    right_icon_color = get_color_from_hex("#ffffff")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_background = get_color_from_hex("#191b1f")

        menu_items = [
            {
                "text": f"Item ",
                "left_icon": "git",
                "viewclass": "Item",
                "height": dp(54),
                # "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            }
        ]

        self.menu = MDDropdownMenu(
            background_color=self.menu_background,
            caller=self.ids.music_list_icon_right,
            items=menu_items,
            width_mult=4,
            pos_hint={"center_y": 1},
        )

    def open_menu(self):
        self.menu.check_position_caller(None, None, None)
        self.menu.open()


Builder.load_file(f"{os.path.dirname(__file__)}/music_list.kv")
