import unittest
from classes import *

class TestTelevision(unittest.TestCase):

    def test_power(self):
        self.assetTrue(tv_1.power(), True)      #verify power is on

    def test_channel_up(self):
        self.assertTrue(channel_up(), True)     #verify channel increase is True

    def test_channel_down(self):
        self.assertTrue(channel_down(), True)   #verify channel decrease is True

    def test_volume_up(self):
        self.assertFalse(volume_up(), False)    #verify volume increse is False

    def test_volume_down(self):
        self.assertTrue(volume_down(), True)    #verify volume decrease is True
