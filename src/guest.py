class Guest:

    def __init__(self, name, budget, fav_song_title, fav_song_artist):
        self.name = name
        self.budget = budget
        self.fav_song_title = fav_song_title
        self.fav_song_artist = fav_song_artist

    def pay_room_entry(self, room):
        return self.budget - room.entry_price

    def pick_song(self):
        pass

    def cheer_loudly(self, room):
        if self.fav_song_title == room.song_played_title and self.fav_song_artist == room.song_played_artist:
            return f"Woohooo!"
        else:
            return f"Meh..."
