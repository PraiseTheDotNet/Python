from datetime import time

from lab8.task1.Album import Album
from lab8.task1.Artist import Artist
from lab8.task1.Entity import Entity


class Song (Entity):
    name = 'No title'
    album: Album = None
    year = 0
    duration = time(0, 0)

    def __init__(self):
        super().__init__()
