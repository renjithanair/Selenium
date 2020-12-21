from controls.base.clickable import Clickable


class Image(Clickable):
    def __init__(self, driver):
        Clickable.driver = driver

    def get_src(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.get_attribute("src")