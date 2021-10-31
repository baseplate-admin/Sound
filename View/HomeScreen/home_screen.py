from typing import NoReturn
from kivy.properties import ObjectProperty

from .components import *
from View.base_screen import BaseScreenView


class HomeScreenView(BaseScreenView):
    """Implements the login start screen in the user application."""

    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

        self.model.add_observer(self)
        self.controller.fetch_songs()

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.ids.nav_drawer.set_state(self.model.state)
        if not self.model.music_loading:
            self.ids.home_widgets.add_widget(self.model.music_widget)


Builder.load_file(f"{os.path.dirname(__file__)}/home_screen.kv")
