
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
from sklearn.manifold import MDS
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import animation


# define function for reading in data
# note for MDS it takes a dissimilarity matrix
def populate_matrix(filename, matrix):
	infile = open(filename, "r")

	row = 0
	
	for line in infile:
		line = line.rstrip()
		data = line.split("\t")

		col = 0

		# loop through all the elements in the line
		for val in data:
			# need to do a smarter imputation of missing data 
			if val == 'NA':
				dist = 0.0
			elif float(val) == 0.0:
				dist = 0.0
			else:
				dist = (1.0/(float(val)**2))	
			
			matrix[row][col] = dist
			# enforce that matrix[i][j] == matrix[j][i] 
			matrix[col][row] = dist
	
			col = col + 1
		row = row + 1
	
	infile.close()
	return matrix


## import the output from step 1
# initialize the distance matrix
dist_matrix = np.zeros((1258,1258))
print("importing file" )
dist_matrix = populate_matrix("GSM1379427.matrix", dist_matrix)

# gut check that all the self-self interactions are zero
if sum(dist_matrix.diagonal()) != 0:
	print("WARNING: non-zero elements present in the diagonal")
else:
	print("Gut check passed")
	
# pre-process with a PCA to see if it improves the embedding
print("running PCA...")
PCA_matrix = PCA().fit(dist_matrix)

#run MDS
print("running MDS...")
data_embedded = MDS(n_components = 3, metric = False).fit_transform(PCA_matrix.components_)

# output embedded data
print("outputting results...")
np.savetxt("MDS_results.txt", data_embedded)

# output distance matrix and PCA matrix
np.savetxt("MDS_distance_matrix.txt", dist_matrix)
np.savetxt("MDS_PCA_matrix.txt", PCA_matrix.components_)

# generate a figure of the results
fig = plt.figure()
ax = plt.axes(projection='3d')

def init():
	#ax.scatter(*zip(*data_embedded), c=clrs,  marker='.')
	# chr1 data
	ax.scatter(data_embedded[0:557,0], data_embedded[0:557,1], data_embedded[0:557,2], c='purple', marker=',', alpha=0.5)
	
	# chr2 data
	ax.scatter(data_embedded[558:1011,0], data_embedded[558:1011,1], data_embedded[558:1011,2], c='orange', marker=',', alpha=0.5)
	
	# chr3 data
	ax.scatter(data_embedded[1012:1257,0], data_embedded[1012:1257,1], data_embedded[1012:1257,2], c='green', marker=',' , alpha=0.5)
	

	return fig,

def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,
	
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)                     
anim.save('MDS_basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])                               

plt.savefig("MDS_fig.png")