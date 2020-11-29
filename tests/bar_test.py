import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room
from src.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar_1 = Bar("Classical Bar", 50)
        self.bar_2 = Bar("Balkan Bar", 100)
        self.bar_3 = Bar("Acoustic Bar", 120)
        self.bar_4 = Bar("Chillout Bar", 80)
        self.guest_1 = Guest("Lou", 30, 30, "Indifferent Suns", "Dark Tranquillity")
        self.guest_2 = Guest("Milo", 21, 47, "Selig", "Helium Vola")
        self.guest_3 = Guest("Fin", 15, 50, "Three white horses", "Andrew Bird")
        self.guest_4 = Guest("Camyla", 17, 40, "Spiriteaux", "Tony Anderson")


    def test_bar_has_name(self):
        self.assertEqual("Classical Bar", self.bar_1.name)
        self.assertEqual("Balkan Bar", self.bar_2.name)
        self.assertEqual("Acoustic Bar", self.bar_3.name)
        self.assertEqual("Chillout Bar", self.bar_4.name)

    def test_bar_has_till(self):
        self.assertEqual(50, self.bar_1.till)
        self.assertEqual(100, self.bar_2.till)
        self.assertEqual(120, self.bar_3.till)
        self.assertEqual(80, self.bar_4.till)

    # def test_guest_is_over_18(self):
    #     self.assertEqual(True, self.bar_1.verify_age())