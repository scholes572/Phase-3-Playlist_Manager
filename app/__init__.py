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

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                print(f"Removed: {song}")
        print(f"Song'{title}' not found in playlist")     
                 
    def show_songs(self):
        if not self.songs:
            print("Playlist is empty. ")
        else:
            print (f"Playlist: {self.name}")
            for song in self.songs:
                print (f" - (song)")    
        

if __name__=="__main__":
    song1 = Song("Shape of You", "Ed Sheeran",4)
    song2 = Song("Blinding Lights", "The Weeknd",3)

    my_playlist = Playlist("Favourites")
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)

    print("Songs in playlist:")
    my_playlist.show_songs()