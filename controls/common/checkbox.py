from controls.base.clickable import Clickable


class CheckBox(Clickable):
    def __init__(self, driver):
        Clickable.driver = driver

    def check(self, mode, value):
        _element_obj = Clickable.get_element(self, mode, value)
        if not _element_obj.is_selected():
            self.click(mode, value)

    def uncheck(self, mode, value):
        _element_obj = Clickable.get_element(self, mode, value)
        if _element_obj.is_selected():
            self.click(mode, value)

    def set(self, mode, value, flag):
        if flag:
            self.check(mode, value)
        else:
            self.uncheck(mode, value)

