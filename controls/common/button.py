from controls.base.clickable import Clickable


class Button(Clickable):
    def __init__(self, driver):
        Clickable.driver = driver
