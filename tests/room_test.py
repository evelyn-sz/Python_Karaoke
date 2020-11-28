import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
        
    def setUp(self):
        self.song_1 = Song("Trio Sonata in D Minor", "Antonio Vivaldi", "classical")
        self.song_2 = Song("Eppur si muove", "Haggard", "orchestral death metal")
        self.song_3 = Song("Three white horses", "Andrew Bird", "multiinstrumental")
        self.song_4 = Song("Spiriteaux", "Tony Anderson", "cinematic")
        self.guest_1 = Guest("Lou", 30, "Indifferent Suns", "Dark Tranquillity")
        self.guest_2 = Guest("Milo", 47, "Selig", "Helium Vola")
        self.guest_3 = Guest("Fin", 50, "Three white horses", "Andrew Bird")
        self.guest_4 = Guest("Camyla", 40, "Spiriteaux", "Tony Anderson")
        self.room_1 = Room("String quartet", 20, 200, "{Song.title}", "{Song.artist}")
        self.room_2 = Room("Balkanarama", 14, 100, "{Song.title}", "{Song.artist}")
        self.room_3 = Room("Hopsasa", 16, 80, "{Song.title}", "{Song.artist}")
        self.room_4 = Room("Zen", 18, 90, "{Song.title}", "{Song.artist}")

    def test_room_has_room_name(self):
        self.assertEqual("String quartet", self.room_1.room_name)
        self.assertEqual("Balkanarama", self.room_2.room_name)
        self.assertEqual("Hopsasa", self.room_3.room_name)
        self.assertEqual("Zen", self.room_4.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(20, self.room_1.capacity)
        self.assertEqual(14, self.room_2.capacity)
        self.assertEqual(16, self.room_3.capacity)
        self.assertEqual(18, self.room_4.capacity)

    def test_room_has_till(self):
        self.assertEqual(200, self.room_1.till)
        self.assertEqual(100, self.room_2.till)
        self.assertEqual(80, self.room_3.till)
        self.assertEqual(90, self.room_4.till)