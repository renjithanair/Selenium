import sys
import unittest
from selenium import webdriver

from constants import Constants
from driver.webdriver import Driver


class BaseTestCase(unittest.TestCase):

    def __call__(self, result=None):
        """
        Wrapper around default __call__ method to perform common test
        set up. This means that user-defined Test Cases aren't required to
        include a call to super().setUp().
        """
        testmethod = getattr(self, self._testMethodName)
        skipped = (
                getattr(self.__class__, "__unittest_skip__", False) or
                getattr(testmethod, "__unittest_skip__", False)
        )

        if not skipped:
            try:
                self._pre_setup()
            except Exception:
                result.addError(self, sys.exc_info())
                return
        super(BaseTestCase, self).__call__(result)
        if not skipped:
            try:
                self._post_teardown()
            except Exception:
                result.addError(self, sys.exc_info())
                return

    def _pre_setup(self):
        """Performs any pre-test setup."""
        pass

    def _post_teardown(self):
        """Perform any post-test things."""
        pass


class SeleniumTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = Driver(Constants.DRIVER_CHROME, Constants.DRIVER_INSTALLATION_PATH)
        cls.driver.instance.maximize_window()
        cls.driver.instance.implicitly_wait(30)
        # navigate to the application home page
        cls.driver.navigate(Constants.NAVIGATION_URL)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.instance.quit()
