import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Trio Sonata in D Minor", "Antonio Vivaldi", "classical")
        self.song_2 = Song("Eppur si muove", "Haggard", "orchestral death metal")
        self.song_3 = Song("Three white horses", "Andrew Bird", "indie")
        self.song_4 = Song("Spiriteaux", "Tony Anderson", "cinematic")

    def test_song_has_title(self):
        self.assertEqual("Trio Sonata in D Minor", self.song_1.title)
        self.assertEqual("Eppur si muove", self.song_2.title)
        self.assertEqual("Three white horses", self.song_3.title)
        self.assertEqual("Spiriteaux", self.song_4.title)

    def test_song_has_artist(self):
        self.assertEqual("Antonio Vivaldi", self.song_1.artist)
        self.assertEqual("Haggard", self.song_2.artist)
        self.assertEqual("Andrew Bird", self.song_3.artist)
        self.assertEqual("Tony Anderson", self.song_4.artist)

    def test_song_has_genre(self):
        self.assertEqual("classical", self.song_1.genre)
        self.assertEqual("orchestral death metal", self.song_2.genre)
        self.assertEqual("indie", self.song_3.genre)
        self.assertEqual("cinematic", self.song_4.genre)
