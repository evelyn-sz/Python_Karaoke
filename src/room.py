class Room:

    def __init__(self, room_name, entry_price, capacity, till, song_played_title, song_played_artist):
        self.room_name = room_name
        self.entry_price = entry_price
        self.capacity = capacity
        self.till = till
        self.song_played_title = song_played_title
        self.song_played_artist = song_played_artist
        self.guest_list= []

    def guest_count(self):
        return(len(self.guest_list))

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def collect_entry_fee(self):
        pass

    def play_song(self):
        pass

    def refuse_entry(self):
        pass

    def check_out_guest(self):
        pass

