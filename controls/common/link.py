from controls.base.clickable import Clickable


class Link(Clickable):
    def __init__(self, driver):
        Clickable.driver = driver
