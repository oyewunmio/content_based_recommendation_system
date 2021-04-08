# importing packages containing classes
import cl_load_dataset as ld
import ld2
import ld3
import similarity_alt as sm
import importlib 

# initializing classes
data = ld.Dataset_Module()
data2 = ld2.Dataset2_Module()
data3 = ld3.Dataset2_Module()
sim = sm.Similarity_Module()

class Main():
    'class function meant for the collecting of values and parsing it to the other classes'
    def main(self):
        'Class method'
        try:
            purpose = input('Do you want to deal with similarity between Artists or Music Tracks.\nEnter A for Artist,\n M for Music Tracks\n B for music similiar to an artist\n')
            metric = str(input('Enter the metric to use for the similarities from the following\n[euclidean, cosine,pearson,jaccard,manhattan]\t'))
            print('\n')
            if purpose.lower() == 'm': # this runs only if the purpose is for the music similarites using ids
                check = input('Enter True if you want to check similarities between two music ids\nEnter False if you want to find the n similiar music to a target music\t')
                if check.lower() == 'false':
                    id1 = input('Enter the target music id\t')
                    n = int(input('Enter the value for n\t'))
                    music_sim=sim.music_similiar(data.Music_features(), id1, '', metric, 'False', n)
                    print('The list of music similiar to {} are {}'.format(id1, music_sim))

                elif check.lower() == 'true':
                    id1 = input('Enter target music id\t')
                    id2 = input('Enter the second music id\t')
                    music_sim=sim.music_similiar(data.Music_features(), id1,id2, metric, 'True',None)  
                    print('Similarity score between  musics is',music_sim)

                else:
                    raise Exception('Wrong value given')
            elif purpose.lower() == 'a':
                check = input('Enter True if you want to check similarities between two artists\nEnter False if you want to find the n similiar music to a target artist\t')
                if check.lower() == 'false':
                    id_1 = str([input('Enter the target artist\t')])
                    n = int(input('Enter the value for n\t'))
                    artist_sim = sim.artists_similiar(data.Artist_music(), id_1, '', metric,'False', n)
                    print('The list of artist similiar to {} are {}'.format(id_1, artist_sim))
                elif check.lower() == 'true':
                    id_1 = str([input('Enter the target artist\t')])
                    id_2 = str([input('Enter the second artist\t')])
                    artist_sim = sim.artists_similiar(data.Artist_music(),id_1, id_2, metric,'True', None)
                    print('Similarity score between  artists is',artist_sim)
                else:
                    raise Exception('Wrong value given')
            elif purpose.lower() == 'b':
                id_1 = str([input('Enter the target artist id\t')])
                n = int(input('Enter the value for n\t'))
                music_id = data2.Artist_tracks(id_1) # this gets the music id of the target artists. this helps us to look for the song similiar to that id'
                result = sim.artist_music_similiar(data.Music_features(),music_id, metric, n)
                song_names = []
                for i in range(len(result)):
                    song_names.append(result[i][0])
                song_name = data3.Song_getter(song_names) # converting the music id calculated to their respective their artists name
                print('The list of similar music to the artist are ',song_name)
            else:
                raise Exception('Wrong value given')
        except Exception as e: # catches all the exceptions and print them 
            raise Exception(e)

v = Main() 
try:
    v.main()
except Exception as e:
    print('\n Error found',e) # Incase an exception occurs, the modules are reloaded and executed again
    importlib.reload(ld)
    importlib.reload(ld2)
    importlib.reload(ld3)
    importlib.reload(sm)
    v.main() 