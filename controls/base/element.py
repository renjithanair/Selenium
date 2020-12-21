from constants import Constants


class Element:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        print('Constructor invoked')

    def get_element(self, mode, value):

        if mode == Constants.NAME:
            return self.driver.instance.find_element_by_name(value)
        elif mode == Constants.ID:
            return self.driver.instance.find_element_by_id(value)
        elif mode == Constants.CLASS_NAME:
            return self.driver.instance.find_elements_by_class_name(value)  # single elemnet method not found
        elif mode == Constants.LINK_TEXT:
            return self.driver.instance.find_element_by_link_text(value)

    def get_text(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.get_text()

    def get_value(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.get_attribute("value")

    def get_attribute(self, mode, value, attribute_name):
        _element_obj = self.get_element(mode, value)
        return _element_obj.get_attribute(attribute_name)

    def is_displayed(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.is_displayed()

    def is_enabled(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.is_enabled()

    def is_selected(self, mode, value):
        _element_obj = self.get_element(mode, value)
        return _element_obj.is_enabled()
