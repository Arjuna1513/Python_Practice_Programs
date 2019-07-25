import unittest
import pytest
from selfself.Custom_Logger import CustomLogger
import logging
# from tests.conftest import *

class PM_Login_tests(unittest.TestCase):
    log = CustomLogger.custom_logger(logging.INFO)
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = 100


    def test_pm_valid_login(self):
        self.log.info(self.lp)
        print(self.lp)
        # self.driver.close()


