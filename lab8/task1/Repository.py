import pandas as pd


class Repository:
    def __init__(self, connection_string):
        self.__connection_string = connection_string
        self.__songs = None
        self.__albums = None
        self.__artists = None

    def connect(self):
        self.__songs = pd.read_csv(self.__connection_string + '/songs.csv')
        self.__albums = pd.read_csv(self.__connection_string + '/albums.csv')
        self.__artists = pd.read_csv(self.__connection_string + '/artists.csv')
