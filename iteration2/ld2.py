# importing packages
import csv
import random 

file =open('data.csv', encoding='utf8') # reading the csv file using default open keyword

class Dataset2_Module():
    def Artist_tracks(self,a):
        'This compares the artist given and return the equivalent music id'
        csv_reader = csv.DictReader(file)
        artist_music_identifier = []
        for rows in csv_reader:
            if rows['artists'] == a:
                artist_music_identifier.append(rows['id'])
        return artist_music_identifier[random.randrange(0,len(artist_music_identifier))] # this picks a randomized music id from the given artist 