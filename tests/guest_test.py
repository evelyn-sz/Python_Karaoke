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

    def test_guest_has_fav_song_title(self):
        self.assertEqual("Indifferent Suns", self.guest_1.fav_song_title)
        self.assertEqual("Selig", self.guest_2.fav_song_title)
        self.assertEqual("Three white horses", self.guest_3.fav_song_title)
        self.assertEqual("Spiriteaux", self.guest_4.fav_song_title)

    def test_guest_has_fav_song_artist(self):
        self.assertEqual("Dark Tranquillity", self.guest_1.fav_song_artist)
        self.assertEqual("Helium Vola", self.guest_2.fav_song_artist)
        self.assertEqual("Andrew Bird", self.guest_3.fav_song_artist)
        self.assertEqual("Tony Anderson", self.guest_4.fav_song_artist)
