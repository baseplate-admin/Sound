import importlib

from libs import delayed_work
from typing import NoReturn


from kivy.network.urlrequest import UrlRequest
from kivy.utils import get_color_from_hex


from kivymd.uix.list import MDList

from Model import HomeScreenModel

import View.HomeScreen.home_screen
from View.HomeScreen.components import *


# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.HomeScreen.home_screen)


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model: HomeScreenModel = model  # Model.home_screen.HomeScreenModel
        self.view = View.HomeScreen.home_screen.HomeScreenView(
            controller=self, model=self.model
        )

        self.result = None
        self.result_items: int = 15
        self.result_items_to_add: int = 10

        self.md_list = MDList()

        self.scroll_widget = self.view.ids.home_widgets

    def fetch_songs(self, *args):
        UrlRequest(
            "https://jsonplaceholder.typicode.com/todos", self.fetch_songs_success
        )

    def create_widgets(self, item):
        primary_color = get_color_from_hex("#b6b6b7")
        secondary_color = get_color_from_hex("#6f7c82")

        # Each object is I
        music_list = MusicListWithDropdown(
            text=f"{item}",
            right_text="5.10",
            secondary_text="None",
            theme_text_color="Custom",
            secondary_theme_text_color="Custom",
            text_color=primary_color,
            secondary_text_color=secondary_color,
            on_press=lambda _: self.music_list_button_press(item),
        )
        self.md_list.add_widget(music_list)

    def fetch_songs_success(self, req, result) -> NoReturn:
        # Read the file. If theres no file create it and then save it.
        # This way we can check if we have to render widgets
        self.result = result
        __result = [ele for ele in reversed(self.result[0 : self.result_items])]

        delayed_work(self.create_widgets, __result)

        self.model.music_widget = self.md_list
        self.model.music_loading = False

    def music_list_button_press(self, id: int) -> NoReturn:
        print(id)

    def on_scroll_start(self) -> NoReturn:
        if self.scroll_widget.scroll_y <= 0.1:
            self.result_items += self.result_items_to_add
            __result = [
                ele
                for ele in reversed(
                    self.result[
                        self.result_items - self.result_items_to_add : self.result_items
                    ]
                )
            ]
            delayed_work(self.create_widgets, __result)

    def on_scroll_end(self):
        if self.scroll_widget.scroll_y <= 0.0:
            for i in self.md_list.children[0:10]:
                self.md_list.remove_widget(i)

    def on_press_navbar_menu_icon(self) -> NoReturn:
        """Called when the `Menu` icon is pressed."""
        possible_states = ["open"]
        self.model.state = possible_states[0]

    def get_view(self) -> View.HomeScreen.home_screen.HomeScreenView:
        return self.view
