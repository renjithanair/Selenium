from selenium import webdriver

from constants import Constants


class Driver:

    def __init__(self, driver_type, path):
        if driver_type == Constants.DRIVER_CHROME:
            # self.instance = webdriver.Chrome(path)
            self.instance = webdriver.Chrome()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")