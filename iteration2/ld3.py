import csv
file =open('data.csv', encoding='utf8') # reading the csv file using default open keyword
#csv_reader = csv.DictReader(file) # converting the file to dictionary type using csv dict reader

class Dataset2_Module():
    def Song_getter(self,b):
        csv_reader = csv.DictReader(file)
        song_names = []
        for rows in csv_reader:
            for ids in b:
                if rows['id'] == ids:
                    song_names.append(rows['name'])
        return song_names