# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model import HomeScreenModel

from Controller import HomeScreenController

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    }
}
