import unittest
from time import sleep


class Test002(unittest.TestCase):
    def test002_001(self):
        sleep(5)
        print('test002_001')
    def test002_002(self):
        sleep(5)
        print('test002_002')