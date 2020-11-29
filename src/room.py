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

    def check_out_guest(self, guest_name):
        # for guest in self.guest_list:
        #     if guest_name == guest.name:
        self.guest_list.remove(guest_name)

    def search_guest(self, guest_name):
        for guest in self.guest_list:
            if guest_name == guest.name:
                return True
        else:
                return False

    def collect_entry_fee(self):
        return self.till + self.entry_price

    def play_song(self):
        return f"Currently playing: {self.song_played_title} by {self.song_played_artist}"

    def check_capacity(self):
        if len(self.guest_list) >= self.capacity:
            return  f"The room had reached its capacity. Please try again later"
        else:
            return f"Please come in."

