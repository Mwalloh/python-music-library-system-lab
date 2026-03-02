class Song:
    """ Class Attributes """
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    """ Increments the value of 'count' by one """
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    """ Adds any new genres to 'genres' -> No duplicates """
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    """ Adds any new artists to 'artists' -> No duplicates """      
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
    """ Updates 'genre_count' and increments genre key by 1, adds 'genre' if it doesn't exist """
    @classmethod 
    def add_to_genre_count(cls, genre):
        genre_cnt = 0
        genre_keys = cls.genre_count.keys()
        if genre not in genre_keys:
            cls.genre_count[genre] = genre_cnt + 1
        elif genre in genre_keys:
            cls.genre_count[genre] += 1
    
    """ Updates 'artist_count' and increments artist key by 1, adds 'artist' if they don't exist """
    @classmethod
    def add_to_artists_count(cls, artist):
        artist_cnt = 0
        artist_keys = cls.artist_count.keys()
        if artist not in artist_keys:
            cls.artist_count[artist] = artist_cnt + 1
        elif artist in artist_keys:
            cls.artist_count[artist] += 1
                
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)