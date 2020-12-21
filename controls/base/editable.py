
from controls.base.element import Element


class Editable(Element):
    def __init__(self, driver):
        Element.driver = driver

    def send_keys(self, mode, value, text):
        _element_obj = self.get_element(mode, value)
        _element_obj.send_keys(text)



