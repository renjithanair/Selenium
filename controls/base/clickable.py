from controls.base.element import Element


class Clickable(Element):
    def __init__(self, driver):
        Element.driver = driver
        print("inside clickable")
        # self.element = element

    def click(self, mode, value):
        _element_obj = self.get_element(mode, value)
        _element_obj.click()


