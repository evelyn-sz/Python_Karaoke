class Room:

    def __init__(self, room_name, capacity, till, song_played_title, song_played_artist):
        self.room_name = room_name
        self.capacity = capacity
        self.till = till
        self.song_played_title = song_played_title
        self.song_played_artist = song_played_artist

    def check_in_guest(self):
        pass

    def play_song(self):
        pass

    def refuse_entry(self):
        pass

    def check_out_guest(self):
        pass