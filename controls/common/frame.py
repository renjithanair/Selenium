from controls.base.element import Element


class Frame(Element):
    def __init__(self, driver):
        Element.driver = driver

    def switch_to_frame(self, name):
        self.driver.switch_to_frame(name)
