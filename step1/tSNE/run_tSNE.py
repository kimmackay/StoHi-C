# StoHi-C Step 1: 3D embedding using tSNE
# This script takes a normalized whole-genome contact map as input and 
# embeds the genomic bins in 3D space using TSNE from the sklearn.manifold library
# Argument 1: the file name of the normalized whole-genome contact map
# Argument 2: the output file name for the XYZ coordinates
# Argument 3: the output file name for the distance matrix used by tSNE

# AUTHOR INFORMATION:
# Kimberly MacKay
# kimberly.mackay@usask.ca
# @mackayka (twitter)

# Authored on April 30, 2019

# LISCENSE INFORMATION
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 
# 3.0 Unported License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 
# PO Box 1866, Mountain View, CA 94042, USA.

# import relavent libraries
import numpy as np
from sklearn.manifold import TSNE
import time
import sys

# define function for reading in data
def populate_matrix(filename, matrix):
	infile = open(filename, "r")

	row = 0
	
	for line in infile:
		line = line.rstrip()
		data = line.split("\t")

		col = 0

		# loop through all the elements in the line
		for val in data: 
			if val == 'NA':
				dist = 0.0 
			elif float(val) == 0.0:
				dist = 0.0
			else:
				dist = 1.0/(float(val)**2)	
			
			matrix[row][col] = dist
			# enforce that matrix[i][j] == matrix[j][i] 
			matrix[col][row] = dist
	
			col = col + 1
		row = row + 1
	
	infile.close()
	return matrix

# grab command line arguments
input_file = sys.argv[1]
coord_file = sys.argv[2]
dist_file = sys.argv[3]

# initialize the distance matrix
dist_matrix = np.zeros((1258,1258))
#print("importing file..." )
dist_matrix = populate_matrix(input_file, dist_matrix)

#print("IF sum: " + str(np.sum(dist_matrix)))

# gut check that all the self-self interactions are zero
if sum(dist_matrix.diagonal()) != 0:
	print("WARNING: non-zero elements present in the diagonal")

#run TSNE
#https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
#print("running tSNE...")
start_time = time.time()

# parameters
# n_components = dimensionality
# perplexity = # of nearest neighbours
# early_exaggeration = determines how "close" nodes will be in the final embedding larger values = farther apart
# n_iter = maximum number of iterations for the optimization
# method = exact (alternative would be an approximation)
# init = run PCA and use those results as input to tSNE
data_embedded = TSNE(n_components = 3, perplexity=5.0, early_exaggeration=3.0, n_iter=5000, method='exact', init='pca').fit_transform(dist_matrix)

stop_time = time.time()

print("tSNE runtime: " + str(stop_time - start_time) + " seconds")

# output embedded data
np.savetxt(coord_file, data_embedded)

# output distance matrix
np.savetxt(dist_file, dist_matrix)
