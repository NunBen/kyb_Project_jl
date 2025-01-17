import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('==============setUp==============')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('===============teardown============')
        sleep(3)
        self.driver.close_app()

if __name__ == '__main__':
    unittest.main()
