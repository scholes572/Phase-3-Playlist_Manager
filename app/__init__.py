class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} min)" 


class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def show_songs(self):
        for i, song in enumerate(self.songs, 1):
            print(f"{i}.{song}")

if __name__=="__main__":
    song1 = Song("Shape of You", "Ed Sheeran",4)
    song2 = Song("Blinding Lights", "The Weeknd",3)

    my_playlist = Playlist("Favourites")
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)

    print("Songs in playlist:")
    my_playlist.show_songs()