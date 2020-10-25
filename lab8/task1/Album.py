from lab8.task1.Artist import Artist
from lab8.task1.Entity import Entity


class Album (Entity):
    title = ''
    songs = []
    artist: Artist = None

    def __init__(self, title):
        super().__init__()
        self.title = title
