# importing packages
import csv

file =open('data.csv', encoding='utf8') # reading the csv file using default open keyword
csv_reader = csv.DictReader(file) # converting the file to dictionary type using csv dict reader

class Dataset_Module():
    def __init__(self):
        # constructor class
        pass

    def Artist_music(self):
        'returns dictionary containing artist and other corresponding features'
        artist_music = {}
        for rows in csv_reader:
            artist_music[rows['artists']] = [float(rows['danceability']), float(rows['liveness']), int(rows['popularity']), float(rows['speechiness']), float(rows['energy']), float(rows['loudness']), float(rows['tempo']), float(rows['valence'])] # note name is not given in artists similarities based on the belief that same artists would be similiar and different artists similarities could be computed by thier type of songs
        return artist_music

    def Music_features(self):
        'returns dictionary containing music id and other respective features'
        music_features = {}
        for rows in csv_reader:
            music_features[rows['id']] = [float(rows['acousticness']), float(rows['danceability']), float(rows['energy']), float(rows['liveness']), float(rows['loudness']), float(rows['speechiness']), float(rows['tempo']), float(rows['valence'])]
        return music_features

