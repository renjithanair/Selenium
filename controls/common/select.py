from selenium.webdriver.support.select import Select

from controls.base.clickable import Clickable


class SelectBox(Clickable):
    def __init__(self, driver):
        Clickable.driver = driver

    def select_by_index(self, mode, value, index):
        select = Select(self.get_element(mode, value))
        return select.select_by_index(index)

