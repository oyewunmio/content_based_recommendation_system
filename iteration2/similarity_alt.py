# importing packages/ Libraries
import numpy as np
from scipy.stats import pearsonr # used in the pearson similarity
from scipy.spatial.distance import cosine # used in calculating the cosine similarity
from scipy.spatial.distance import cityblock # used for the manhattan similarity
from scipy.spatial.distance import euclidean # used for the euclidean similarity
from scipy.spatial.distance import jaccard # used for the jaccard similarity
import sys

class Similarity_Module():
	def __init__(self):
		pass
	
	def euclidean_similarity(self,a, id_1, id_2):
		'computes the euclidean distance between music or artists'
		try:
			point1 = np.array(a.get(id_1)) # retrieving the features for the respective id and converting it to a numpy array
			point2 = np.array(a.get(id_2))
			return euclidean(point1, point2)	
		except KeyError:
			print('Artists/Music id not found..Check inputs')

	def cosine_similarity(self,a, id_1, id_2):
		'computes the cosine distance between music or artists..cosine similarity is majorly used in document similarity'
		try:
			point1 = np.array(a.get(id_1))# retrieving the features for the respective id and converting it to a numpy array
			point2 = np.array(a.get(id_2))
			return 1- cosine(point1, point2) # note cos_sim that this is the cosine distance returned ..so the similarity is the distance minus from 1
		except KeyError:
			print('Artists/Music id not found..Check inputs')

	def pearson_similarity(self,a, id_1, id_2):
		'computes the pearson correlation between the music or artists'
		try:
			point1 = np.array(a.get(id_1)) # retrieving the features for the respective id and converting it to a numpy array
			point2 = np.array(a.get(id_2))
			corr, _ = pearsonr(point1, point2)
			return corr
		except KeyError:
			print('Artists/Music id not found..Check inputs')
	
	def jaccard_similarity(self,a, id_1, id_2):
		' measures the similarity between two sets of data.The higher the number, the more similar the two sets of data.'
		try:
			point1 = a.get(id_1) # retrieving the features for the respective id and converting it to a numpy array
			point2 = a.get(id_2)
			return (1 - jaccard(point1, point2)) #jaccard function returns the jaccard distance, the similarity is the remainder when distance removed from one 
		except Exception as e:
			print(e)
	
	def manhattan_similarity(self,a, id_1, id_2):
		'measures the distance between the two points measured along axes at right angles'
		try:
			point1 = np.array(a.get(id_1)) #retrieving the features for the respective id and converting it to a numpy array
			point2 = np.array(a.get(id_2))
			return cityblock(point1, point2)
		except KeyError:
			print('Artists/Music id not found..Check inputs')


	def artists_similiar(self, a, id_1,id_2, metric, flag,n):
		'returns the n list of artists similiar to the target artist ..note this is based on the metric given'
		# note that the id_1 is the target artist id we checking similarities for
		result = {}
		if flag == 'True': # this means the person is interested in finding the similarities between two artist 
			if metric.lower() == 'manhattan':
				v = self.manhattan_similarity(a, id_1,id_2)
			elif metric.lower() == 'jaccard':
				v = self.jaccard_similarity(a, id_1, id_2)
			elif metric.lower() == 'euclidean':
				v = self.euclidean_similarity(a, id_1, id_2)
			elif metric.lower() == 'cosine':
				v = self.cosine_similarity(a, id_1, id_2)
			elif metric.lower() == 'pearson':
				v = self.pearson_similarity(a, id_1, id_2)
			return v
		else:
			for keys in a.keys(): # else the person is interested in finding the n similiar to the target artist.
				if metric .lower()== 'manhattan':
					score = self.manhattan_similarity(a, id_1, keys) 
					result[keys] = score
				elif metric.lower() == 'cosine':
					score = self.cosine_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'euclidean':
					score = self.euclidean_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'jaccard':
					score = self.jaccard_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'pearson':
					score = self.pearson_similarity(a, id_1, keys)
					result[keys] = score
			if metric.lower() == 'cosine' or metric.lower() == 'pearson' or metric.lower() == 'jaccard':
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1], reverse=True)) # setting reverse to True makes the sorted to sort from 1 to the lowest, since the closer to one The closer the cosine value to 1, the smaller the angle and the greater the match between vectors
			else:
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1]))
			# to get the first n items from the sorted dictionary
			return list(sorted_dict.items())[:n]

	def music_similiar(self, a, id_1, id_2, metric, flag, n):
		'returns the n list of music similiar to the target music ..note this is based on the metric given'
		# note that the id_1 is the target music id we checking similarities for
		# for checking similarities between two track songs
		result = {}
		if flag == 'True': # this means the person is interested in finding the similarities between two music tracks
			if metric.lower() == 'manhattan':
				v = self.manhattan_similarity(a, id_1,id_2)
			elif metric.lower() == 'jaccard':
				v = self.jaccard_similarity(a, id_1, id_2)
			elif metric.lower() == 'euclidean':
				v = self.euclidean_similarity(a, id_1, id_2)
			elif metric.lower() == 'cosine':
				v = self.cosine_similarity(a, id_1, id_2)
			elif metric.lower() == 'pearson':
				v = self.pearson_similarity(a, id_1, id_2)
			return v
		else:
			for keys in a.keys(): # iterating through all the keys and using it to find the most similiar musics to the target music
				if metric.lower() == 'manhattan':
					score = self.manhattan_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'cosine':
					score = self.cosine_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'euclidean':
					score = self.euclidean_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'jaccard':
					score = self.jaccard_similarity(a, id_1, keys)
					result[keys] = score
				elif metric.lower() == 'pearson':
					score = self.pearson_similarity(a, id_1, keys)
					result[keys] = score
			if metric.lower() == 'cosine' or metric.lower() == 'pearson' or metric.lower() == 'jaccard':
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1], reverse=True)) # setting reverse to True makes the sorted to sort from 1 to the lowest, since the closer to one The closer the cosine value to 1, the smaller the angle and the greater the match between vectors
			else:
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1]))

			# to get the first n items from the sorted dictionary
			return list(sorted_dict.items())[:n]

			
	def artist_music_similiar(self,c,music_id,metric,n):
		'returns the n list of music similiar to a target artists'
		# note that the id_1 is the target artist we checking music similarities for
		result = {}
		for keys in c.keys():
			if metric.lower() == 'manhattan':
				score = self.manhattan_similarity(c, music_id, keys)
				result[keys] = score
			elif metric.lower() == 'cosine':
				score = self.cosine_similarity(c, music_id, keys)
				result[keys] = score
			elif metric.lower() == 'euclidean':
				score = self.euclidean_similarity(c, music_id, keys)
				result[keys] = score
			elif metric.lower() == 'jaccard':
				score = self.jaccard_similarity(c, music_id, keys)
				result[keys] = score
			elif metric.lower() == 'pearson':
				score = self.pearson_similarity(c, music_id, keys)
				result[keys] = score
		if metric.lower() == 'cosine' or metric.lower() == 'pearson' or metric.lower() == 'jaccard':
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1], reverse=True)) # setting reverse to True makes the sorted to sort from 1 to the lowest, since the closer to one, the smaller the angle and the greater the match between vectors
		else:
				sorted_dict = dict(sorted(result.items(), key=lambda item: item[1]))
		# to get the first n items from the sorted dictionary
		return list(sorted_dict.items())[:n]

