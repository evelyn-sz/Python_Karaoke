import unittest

from src.guest import Guest
from src.song import Song
# from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Trio Sonata in D Minor", "Antonio Vivaldi", "classical")
        self.song_2 = Song("Eppur si muove", "Haggard", "orchestral death metal")
        self.song_3 = Song("Three white horses", "Andrew Bird", "multiinstrumental")
        self.song_4 = Song("Spiriteaux", "Tony Anderson", "cinematic")
        self.guest_1 = Guest("Lou", 30, "Indifferent Suns", "Dark Tranquillity")
        self.guest_2 = Guest("Milo", 47, "Selig", "Helium Vola")
        self.guest_3 = Guest("Fin", 50, "Three white horses", "Andrew Bird")
        self.guest_4 = Guest("Camyla", 40, "Spiriteaux", "Tony Anderson")

    def test_guest_has_name(self):
        self.assertEqual("Lou", self.guest_1.name)
        self.assertEqual("Milo", self.guest_2.name)
        self.assertEqual("Fin", self.guest_3.name)
        self.assertEqual("Camyla", self.guest_4.name)

    def test_guest_has_budget(self):
        self.assertEqual(30, self.guest_1.budget)
        self.assertEqual(47, self.guest_2.budget)
        self.assertEqual(50, self.guest_3.budget)
        self.assertEqual(40, self.guest_4.budget)