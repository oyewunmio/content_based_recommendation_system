#importing package
import csv

file =open('data.csv', encoding='utf8') # reading the csv file using default open keyword
csv_reader = csv.DictReader(file) # converting the file to dictionary type using csv dict reader

def Artist_features():
    'returns dictionary containing artist and other corresponding features'
    artist_features= {}
    for rows in csv_reader:
        artist_features[rows['artists']] = [float(rows['danceability']), float(rows['liveness']), int(rows['popularity']), float(rows['speechiness']), float(rows['energy']), float(rows['loudness'])] # note name is not given in artists similarities based on the belief that same artists would be similiar and different artists similarities could be computed by thier type of songs
    return artist_features

def Music_features():
    'returns dictionary containing music id and other respective features'
    music_features = {}
    for rows in csv_reader:
        music_features[rows['id']] = [float(rows['acousticness']), float(rows['danceability']), float(rows['energy']), float(rows['liveness']), float(rows['loudness']), float(rows['speechiness']), float(rows['tempo']), float(rows['valence'])]
    return music_features
    
