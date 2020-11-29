import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
        
    def setUp(self):
        self.song_1 = Song("Trio Sonata in D Minor", "Antonio Vivaldi", "classical")
        self.song_2 = Song("Eppur si muove", "Haggard", "orchestral death metal")
        self.song_3 = Song("Three white horses", "Andrew Bird", "indie")
        self.song_4 = Song("Spiriteaux", "Tony Anderson", "cinematic")
        self.guest_1 = Guest("Lou", 30, "Indifferent Suns", "Dark Tranquillity")
        self.guest_2 = Guest("Milo", 47, "Selig", "Helium Vola")
        self.guest_3 = Guest("Fin", 50, "Three white horses", "Andrew Bird")
        self.guest_4 = Guest("Camyla", 40, "Spiriteaux", "Tony Anderson")
        self.room_1 = Room("String quartet", 11, 20, 200, self.song_1.title, self.song_1.artist)
        self.room_2 = Room("Balkanarama", 7, 14, 100, self.song_2.title, self.song_2.artist)
        self.room_3 = Room("Hopsasa", 8, 16, 80, self.song_3.title, self.song_3.artist)
        self.room_4 = Room("Zen", 9, 18, 90, self.song_4.title, self.song_4.artist)

    def test_room_has_room_name(self):
        self.assertEqual("String quartet", self.room_1.room_name)
        self.assertEqual("Balkanarama", self.room_2.room_name)
        self.assertEqual("Hopsasa", self.room_3.room_name)
        self.assertEqual("Zen", self.room_4.room_name)

    def test_room_has_entry_price(self):
        self.assertEqual(11, self.room_1.entry_price)
        self.assertEqual(7, self.room_2.entry_price)
        self.assertEqual(8, self.room_3.entry_price)
        self.assertEqual(9, self.room_4.entry_price)

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

    def test_room_has_song_played_title(self):
        self.assertEqual("Trio Sonata in D Minor", self.room_1.song_played_title)
        self.assertEqual("Eppur si muove", self.room_2.song_played_title)
        self.assertEqual("Three white horses", self.room_3.song_played_title)
        self.assertEqual("Spiriteaux", self.room_4.song_played_title)

    def test_room_has_song_played_artist(self):
        self.assertEqual("Antonio Vivaldi", self.room_1.song_played_artist)
        self.assertEqual("Haggard", self.room_2.song_played_artist)
        self.assertEqual("Andrew Bird", self.room_3.song_played_artist)
        self.assertEqual("Tony Anderson", self.room_4.song_played_artist)

    def test_room_starts_with_no_guests(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual("Lou", self.room_1.guest_list[0].name)
        self.assertEqual(1, self.room_1.guest_count())

