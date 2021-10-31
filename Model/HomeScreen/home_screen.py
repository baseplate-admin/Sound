from typing import NoReturn

from Model.base_model import BaseScreenModel


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """

    def __init__(self) -> NoReturn:
        self._state: str = ""
        self._music_widget = None
        self._music_loading: bool = True
        self._observers: object = []

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> NoReturn:
        possible_states = ["open"]
        if value not in possible_states:
            raise ValueError(
                f"Check your value. It should one of {possible_states}. Not {value}"
            )

        self._state = value
        self.notify_observers()

    @property
    def music_widget(self):
        return self._music_widget

    @music_widget.setter
    def music_widget(self, value) -> NoReturn:
        self._music_widget = value
        self.notify_observers()

    @property
    def music_loading(self) -> bool:
        return self._music_loading

    @music_loading.setter
    def music_loading(self, value: bool) -> NoReturn:
        self._music_loading = value
        self.notify_observers()

    def add_observer(self, observer) -> NoReturn:
        if observer not in self._observers:  # Additional Protection
            self._observers.append(observer)

    def remove_observer(self, observer) -> NoReturn:
        if observer in self._observers:  # Additional Protection
            self._observers.remove(observer)

    def notify_observers(self) -> NoReturn:
        for x in self._observers:
            x.model_is_changed()
