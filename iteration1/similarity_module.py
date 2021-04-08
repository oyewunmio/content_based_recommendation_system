
def similarity(a, id1, id2, function):
    'checks the similarites between music or artist based on a provided similarity function'
    try:
        if function.lower() == 'manhattan':
            Score = manhattan_similarity(a, id1, id2)
        elif function.lower() == 'jaccard':
            Score = jaccard_similarity(a, id1, id2)
        elif function.lower() == 'pearson':
            Score = pearson_similarity(a, id1, id2)
        elif function.lower() == 'cosine':
            Score = cosine_Similarity(a, id1, id2)
        elif function.lower() == 'euclidean':
            Score = euclidean_similarity(a, id1, id2)
        else:
            raise Exception('Sorry no valuable similarity function provided')
        return Score
    except Exception as e:
        print(e)

def euclidean_similarity(a, id_1, id_2):
    'computes the euclidean distance between music or artists'
    try:
        features1 = a.get(id_1) # retrieving the features for the respective id
        features2 = a.get(id_2)
        # calculating Euclidean distance which is the sum of the square component-wise differences 
        distance = sum([(a - b) ** 2 for a, b in zip(features1, features2)])
        distance_squared = distance ** 0.5 
        return distance_squared
    except KeyError:
        print('Artists/Music id not found..Check inputs')

def cosine_Similarity(a, id_1, id_2):
    'computes the cosine distance between music or artists..cosine similarity is majorly used in document similarity'
    try:
        features1 = a.get(id_1)# retrieving the features for the respective id
        features2 = a.get(id_2)
        # finding the dot and norm for calculating the cosine distance
        dot_product = sum(a*b for a, b in zip(features1, features2))    
        norm_features1 = sum(a*a for a in features1) ** 0.5
        norm_features2 = sum(a*a for a in features2) ** 0.5
        cosine_distance = dot_product / (norm_features1*norm_features2)
        return cosine_distance
    except KeyError:
        print('Artists/Music id not found..Check inputs')

def pearson_similarity(a, id_1, id_2):
    'computes the pearson correlation between the music or artists'
    xy = []
    xx = []
    yy = []
    try:
        feature1 = a.get(id_1) # retrieving the features for the respective id 
        feature2 = a.get(id_2)
        for i in range(len(feature1)):
            xy.append(feature1[i] * feature2[i])
            xx.append(feature1[i] * feature1[i])
            yy.append(feature2[i] * feature2[i])
        # pearson formula 
        numerator = (len(feature1) * sum(xy)) - sum(feature1)*sum(feature2)
        denominator = (((len(feature1) * sum(xx)) - (sum(feature1)**2)) * ((len(feature1) * sum(yy)) - (sum(feature2)**2))) ** 0.5
        cofficient  = numerator / denominator 
        return cofficient
    except KeyError:
        print('Artists/Music id not found..Check inputs')

def jaccard_similarity(a, id_1, id_2):
    ' measures the similarity between two sets of data.The higher the number, the more similar the two sets of data.'
    try:
        feature1 = a.get(id_1) # retrieving the features for the respective id
        feature2 = a.get(id_2)

        # calculating jaccard similarity which is defined as the cardinality of the intersection of sets divided by the cardinality of the union of the sample sets
        intersections = len(list(set(feature1).intersection(feature2)))
        union = (len(feature1) + len(feature2)) - intersections
        return float(intersections) / union # jaccard similarity which is no of observations in both sets / number in either sets
    except Exception as e:
        print(e)

def manhattan_similarity(a, id_1, id_2):
    'measures the distance between the two points measured along axes at right angles'
    try:
        feature1 = a.get(id_1) #retrieving the features for the respective id
        feature2 = a.get(id_2)
        #calculating the manhattan distance by finding the absolute sum of the difference between the x-coordinates  and y-coordinates of each of the points. 
        return sum(abs(a-b) for a,b in zip(feature1, feature2))
    except KeyError:
        print('Artists/Music id not found..Check inputs')


