import unittest

from constants import Constants
from controls.base import element
from controls.base.clickable import Clickable
from controls.base.element import Element
from controls.common.button import Button
from controls.common.checkbox import CheckBox
from controls.common.image import Image
from controls.common.label import Label
from controls.common.link import Link
from controls.common.select import SelectBox
from controls.common.textbox import TextBox
from tests.selenium_tests.testcase import SeleniumTestCase


class TestHomePage(SeleniumTestCase):
    def setUp(self):
        print("inside child")
        self.elementObj = Element(self.driver)
        self.button = Button(self.driver)
        self.textbox = TextBox(self.driver)
        self.link = Link(self.driver)
        self.image = Image(self.driver)
        self.label = Label(self.driver)
        self.select = SelectBox(self.driver)
        # self.checkbox = CheckBox(self.driver)

    def tearDown(self):
        super(TestHomePage, self).tearDownClass()

    def test_search_by_text(self):
        # get the search textbox
        # self.search_field = self.driver.instance.find_element_by_name("q")
        # self.search_field = self.elementObj.get_element(Constants.NAME, "q")

        # enter search keyword and submit
        # self.search_field.send_keys("Selenium WebDriver Interview questions")
        # self.search_field.submit()

        self.textbox.send_keys(Constants.NAME, "q", "Selenium WebDriver ")

        # self.search_btn = self.elementObj.get_element(Constants.NAME, "btnK")
        self.button.click(Constants.NAME, "btnK")

        # self.labelText = self.label.get_text(Constants.CLASS_NAME, "Qtsmnf tmDYm")
        # print(self.labelText)

        # self.selectItem = self.select.select_by_index(Constants.NAME, "group_adults", 1)
        # print(self.selectItem)

        # self.src = self.image.get_src(Constants.ID, "hplogo")
        # print(self.src)
        # self.assertTrue(self.src == "/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
        # self.link.click(Constants.LINK_TEXT, "മലയാളം")

        # get the list of elements which are displayed after the search
        # currently on result page usingfind_elements_by_class_namemethod

        # lists = self.driver.instance.find_elements_by_class_name("r")
        # lists = self.elementObj.get_element(Constants.CLASS_NAME, "r")

        # no = len(lists)
        print("1")
        # self.assertTrue(len(lists) == 0)

    # def test_click_checkbox(self):
    # print("here")
    # self.chk = self.driver.instance.find_element_by_name("love")
    # self.chk.click()
    # self.checkbox.set(Constants.NAME, "love", True)


if __name__ == '__main__':
    unittest.main()
