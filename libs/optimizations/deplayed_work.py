from typing import List, Callable
from kivy.clock import Clock


def delayed_work(func: Callable, items: List, delay: int = 0):
    """
    This module helps to unfreeze kivy Clock.
    |> That way the UI doesn't freeze when adding new widgets

    What it does:
    |> Apply the func() on each item contained in items
    """
    if not items:
        return

    def _delayed_work(*l):
        item = items.pop()
        if func(item) is False or not len(items):
            return False
        Clock.schedule_once(_delayed_work, delay)

    Clock.schedule_once(_delayed_work, delay)
